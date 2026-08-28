import csv
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

BASE = "https://gallica.bnf.fr/services/engine/search/sru"

MAX_RECORDS_PER_QUERY = 500
PAGE_SIZE = 50
SLEEP_SECONDS = 0.6

QUERIES = [
    # Lovejoy corpus / mentions
    ('lovejoy_exact_arthur_o', '(gallica all "Arthur O. Lovejoy")'),
    ('lovejoy_exact_arthur_oncken', '(gallica all "Arthur Oncken Lovejoy")'),
    ('lovejoy_exact_a_o', '(gallica all "A. O. Lovejoy")'),
    ('lovejoy_creator', '(dc.creator all "Lovejoy" or dc.contributor all "Lovejoy")'),
    ('lovejoy_all', '(gallica all "Lovejoy")'),

    # Early Buddhist / comparative religion line
    ('upadana', '(gallica all "upadana")'),
    ('upadisesa', '(gallica all "upadisesa")'),
    ('paticca_samuppada', '(gallica all "paticca-samuppada")'),
    ('sankhya_buddhism', '(gallica all "Sankhya" and gallica all "Buddhism")'),
    ('bouddhisme_samkhya', '(gallica all "bouddhisme" and gallica all "samkhya")'),

    # Primitive / primitivism source ecology
    ('primitivism', '(gallica all "primitivism")'),
    ('primitivisme', '(gallica all "primitivisme")'),
    ('primitive_religion', '(gallica all "primitive religion")'),
    ('religion_primitive', '(gallica all "religion primitive")'),
    ('philosophie_primitive', '(gallica all "philosophie primitive")'),
    ('mana', '(gallica all "mana" and gallica all "religion")'),

    # Rousseau / state of nature / noble savage cluster
    ('etat_de_nature', '(gallica all "état de nature")'),
    ('state_of_nature', '(gallica all "state of nature")'),
    ('bon_sauvage', '(gallica all "bon sauvage")'),
    ('sauvage_de_bon_sens', '(gallica all "sauvage de bon sens")'),
    ('homme_naturel', '(gallica all "homme naturel")'),
    ('age_dor', '(gallica all "âge d\'or")'),

    # Authors / texts around Lovejoy-Boas primitivism project
    ('lahontan_sauvage', '(gallica all "Lahontan" and gallica all "sauvage")'),
    ('dialogues_curieux_lahontan', '(gallica all "Dialogues curieux" and gallica all "Lahontan")'),
    ('bougainville_diderot', '(gallica all "Bougainville" and gallica all "Diderot")'),
    ('supplement_bougainville', '(gallica all "Supplément au voyage de Bougainville")'),
    ('discours_inegalite', '(gallica all "Discours sur l\'origine de l\'inégalité")'),
    ('rousseau_inegalite', '(gallica all "Rousseau" and gallica all "inégalité")'),
]

NS = {
    "zs": "http://www.loc.gov/zing/srw/",
    "dc": "http://purl.org/dc/elements/1.1/",
    "srw_dc": "info:srw/schema/1/dc-schema",
}


def fetch_xml(query, start_record=1, maximum_records=50):
    params = {
        "operation": "searchRetrieve",
        "version": "1.2",
        "maximumRecords": str(maximum_records),
        "startRecord": str(start_record),
        "collapsing": "false",
        "query": query,
    }
    url = BASE + "?" + urllib.parse.urlencode(params, safe='():/" ')
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "GallicaLovejoyPrimitiveHarvester/0.1"}
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read(), url


def text_list(elem, tag):
    vals = []
    for x in elem.findall(".//dc:" + tag, NS):
        if x.text:
            vals.append(re.sub(r"\s+", " ", x.text).strip())
    return vals


def extract_ark(identifiers):
    for ident in identifiers:
        m = re.search(r"(ark:/12148/[A-Za-z0-9]+)", ident)
        if m:
            return m.group(1)
        m = re.search(r"(https?://gallica\.bnf\.fr/ark:/12148/[A-Za-z0-9]+)", ident)
        if m:
            return m.group(1).replace("https://gallica.bnf.fr/", "").replace("http://gallica.bnf.fr/", "")
    return ""


def parse_records(xml_bytes, query_label, query_string, request_url):
    root = ET.fromstring(xml_bytes)
    total_el = root.find(".//zs:numberOfRecords", NS)
    total = int(total_el.text) if total_el is not None and total_el.text and total_el.text.isdigit() else 0

    rows = []
    for rec in root.findall(".//zs:record", NS):
        data = rec.find(".//zs:recordData", NS)
        if data is None:
            continue

        titles = text_list(data, "title")
        creators = text_list(data, "creator")
        contributors = text_list(data, "contributor")
        dates = text_list(data, "date")
        types = text_list(data, "type")
        languages = text_list(data, "language")
        publishers = text_list(data, "publisher")
        subjects = text_list(data, "subject")
        identifiers = text_list(data, "identifier")
        descriptions = text_list(data, "description")

        ark = extract_ark(identifiers)
        gallica_url = "https://gallica.bnf.fr/" + ark if ark else ""

        rows.append({
            "query_label": query_label,
            "query_string": query_string,
            "total_for_query": total,
            "title": " | ".join(titles),
            "creator": " | ".join(creators),
            "contributor": " | ".join(contributors),
            "date": " | ".join(dates),
            "type": " | ".join(types),
            "language": " | ".join(languages),
            "publisher": " | ".join(publishers),
            "subject": " | ".join(subjects),
            "description": " | ".join(descriptions),
            "ark": ark,
            "gallica_url": gallica_url,
            "identifiers": " | ".join(identifiers),
            "request_url": request_url,
        })

    return total, rows


def norm_key(row):
    title = re.sub(r"[^a-z0-9]+", " ", row["title"].lower()).strip()
    ark = row["ark"].strip()
    date = row["date"].strip()[:4]
    if ark:
        return ("ark", ark)
    return ("title_date", title, date)


def write_csv(path, rows):
    fields = [
        "query_label", "query_string", "total_for_query",
        "title", "creator", "contributor", "date", "type",
        "language", "publisher", "subject", "description",
        "ark", "gallica_url", "identifiers", "request_url"
    ]
    with open(path, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k, "") for k in fields})


def main():
    all_rows = []
    summary = []

    for label, query in QUERIES:
        print(f"Query: {label} :: {query}")
        start = 1
        total_seen = None
        query_rows = []

        while True:
            try:
                xml_bytes, request_url = fetch_xml(query, start_record=start, maximum_records=PAGE_SIZE)
                total, rows = parse_records(xml_bytes, label, query, request_url)
            except Exception as e:
                print("  ERROR:", e)
                break

            if total_seen is None:
                total_seen = total
                print(f"  total reported: {total_seen}")

            if not rows:
                break

            query_rows.extend(rows)
            all_rows.extend(rows)

            if len(query_rows) >= min(MAX_RECORDS_PER_QUERY, total_seen):
                break

            start += PAGE_SIZE
            time.sleep(SLEEP_SECONDS)

        summary.append({
            "query_label": label,
            "query_string": query,
            "total_reported": total_seen if total_seen is not None else 0,
            "records_collected": len(query_rows),
        })

    deduped = {}
    for r in all_rows:
        k = norm_key(r)
        if k not in deduped:
            deduped[k] = r
        else:
            old = deduped[k]
            old["query_label"] += " ; " + r["query_label"]
            old["query_string"] += " ; " + r["query_string"]

    deduped_rows = sorted(
        deduped.values(),
        key=lambda r: (r.get("date", ""), r.get("title", ""))
    )

    write_csv("gallica_lovejoy_primitive_raw.csv", all_rows)
    write_csv("gallica_lovejoy_primitive_deduped.csv", deduped_rows)

    with open("gallica_query_summary.csv", "w", newline="", encoding="utf-8-sig") as f:
        fields = ["query_label", "query_string", "total_reported", "records_collected"]
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for s in summary:
            w.writerow(s)

    print("Done.")
    print("Raw records:", len(all_rows))
    print("Deduped records:", len(deduped_rows))
    print("Files written:")
    print("  gallica_lovejoy_primitive_raw.csv")
    print("  gallica_lovejoy_primitive_deduped.csv")
    print("  gallica_query_summary.csv")


if __name__ == "__main__":
    main()
