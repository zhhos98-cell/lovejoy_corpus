import csv
import json
import re
import time
import urllib.parse
import urllib.request

YEAR_MIN = 1885
YEAR_MAX = 1970

QUERIES = [
    "Arthur O. Lovejoy",
    "A. O. Lovejoy",
    "Arthur Oncken Lovejoy",
    "Arthur Lovejoy",
    "Lovejoy Buddhistic",
    "Lovejoy upadana",
    "Lovejoy primitive philosophy",
    "Lovejoy primitivism",
    "Lovejoy related ideas",
    "Lovejoy great chain of being",
]


def fetch_json(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "LovejoyMetadataHarvester/0.1"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def clean(s):
    if not s:
        return ""
    return re.sub(r"\s+", " ", str(s)).strip()


def norm_title(s):
    s = clean(s).lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def get_openalex(query):
    rows = []
    for page in range(1, 4):
        params = {
            "search": query,
            "per-page": 100,
            "page": page,
            "filter": f"from_publication_date:{YEAR_MIN}-01-01,to_publication_date:{YEAR_MAX}-12-31",
        }
        url = "https://api.openalex.org/works?" + urllib.parse.urlencode(params)
        data = fetch_json(url)
        results = data.get("results", [])
        if not results:
            break

        for w in results:
            title = clean(w.get("title"))
            authors = []
            for a in w.get("authorships", []):
                au = a.get("author", {})
                authors.append(clean(au.get("display_name")))

            hay = (title + " " + " ".join(authors)).lower()
            if "lovejoy" not in hay:
                continue

            source_names = []
            urls = []
            for loc in w.get("locations", []) or []:
                src = loc.get("source") or {}
                if src.get("display_name"):
                    source_names.append(src.get("display_name"))
                if loc.get("landing_page_url"):
                    urls.append(loc.get("landing_page_url"))

            rows.append({
                "database": "OpenAlex",
                "year": w.get("publication_year", ""),
                "title": title,
                "authors": "; ".join([a for a in authors if a]),
                "type": w.get("type", ""),
                "journal_or_source": "; ".join(sorted(set(source_names))),
                "volume": "",
                "issue": "",
                "pages": "",
                "doi": w.get("doi", ""),
                "url": w.get("id", ""),
                "other_urls": "; ".join(sorted(set(urls))),
                "query": query,
            })

        time.sleep(0.5)

    return rows


def get_crossref(query):
    rows = []
    for offset in range(0, 300, 100):
        params = {
            "query.bibliographic": query,
            "rows": 100,
            "offset": offset,
            "filter": f"from-pub-date:{YEAR_MIN}-01-01,until-pub-date:{YEAR_MAX}-12-31",
        }
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode(params)
        data = fetch_json(url)
        items = data.get("message", {}).get("items", [])
        if not items:
            break

        for item in items:
            title = clean(" ".join(item.get("title", []) or []))
            authors = []
            for a in item.get("author", []) or []:
                authors.append(clean((a.get("given", "") + " " + a.get("family", "")).strip()))

            hay = (title + " " + " ".join(authors) + " " + query).lower()
            if "lovejoy" not in hay:
                continue

            year = ""
            for k in ["published-print", "published-online", "issued"]:
                dp = item.get(k, {}).get("date-parts")
                if dp and dp[0]:
                    year = dp[0][0]
                    break

            rows.append({
                "database": "Crossref",
                "year": year,
                "title": title,
                "authors": "; ".join([a for a in authors if a]),
                "type": item.get("type", ""),
                "journal_or_source": clean(" ".join(item.get("container-title", []) or [])),
                "volume": item.get("volume", ""),
                "issue": item.get("issue", ""),
                "pages": item.get("page", ""),
                "doi": item.get("DOI", ""),
                "url": item.get("URL", ""),
                "other_urls": "",
                "query": query,
            })

        time.sleep(0.5)

    return rows


def dedupe(rows):
    seen = {}
    for r in rows:
        title_key = norm_title(r["title"])
        year_key = str(r["year"])
        doi_key = clean(r["doi"]).lower()

        if doi_key:
            key = ("doi", doi_key)
        else:
            key = ("title_year", title_key, year_key)

        if not title_key:
            continue

        if key not in seen:
            seen[key] = r
        else:
            old = seen[key]
            if len(str(r)) > len(str(old)):
                seen[key] = r

    return sorted(seen.values(), key=lambda x: (str(x["year"]), norm_title(x["title"])))


def write_csv(filename, rows):
    fields = [
        "database", "year", "title", "authors", "type",
        "journal_or_source", "volume", "issue", "pages",
        "doi", "url", "other_urls", "query"
    ]
    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow(r)


all_rows = []

for q in QUERIES:
    print("Searching OpenAlex:", q)
    try:
        all_rows.extend(get_openalex(q))
    except Exception as e:
        print("OpenAlex error:", q, e)

    print("Searching Crossref:", q)
    try:
        all_rows.extend(get_crossref(q))
    except Exception as e:
        print("Crossref error:", q, e)

deduped = dedupe(all_rows)

write_csv("lovejoy_metadata_raw.csv", all_rows)
write_csv("lovejoy_metadata_deduped.csv", deduped)

print("Done.")
print("Raw:", len(all_rows))
print("Deduped:", len(deduped))
print("Files written:")
print("  lovejoy_metadata_raw.csv")
print("  lovejoy_metadata_deduped.csv")
