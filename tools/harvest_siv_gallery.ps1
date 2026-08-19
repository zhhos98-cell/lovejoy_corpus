<#
.SYNOPSIS
    Download a sequential Archives nationales SIV JPEG range and merge it to one PDF.

.DESCRIPTION
    The SIV gallery exposes stable image URLs of the form:

      https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_XXXXX_L-medium.jpg

    Once the first and last sequential image IDs for a gallery have been established,
    this script downloads the range with retries, skips already-valid files, checks
    the resulting count, and merges the JPEGs in numeric order into a PDF using img2pdf.

    Designed during the Marillier / Lovejoy Project 2 sweep on 2026-08-19.

.EXAMPLE
    .\tools\harvest_siv_gallery.ps1 `
        -StartImage 6736 `
        -EndImage 7118 `
        -Name "EPHE_FRAN0464_06736_07118"

.EXAMPLE
    .\tools\harvest_siv_gallery.ps1 `
        -StartImage 7119 `
        -EndImage 7553 `
        -Name "EPHE_FRAN0464_07119_07553"

.NOTES
    Recovered ranges as of 2026-08-19:

    Range A (383 views):
      first  = FRAN_0464_06736_L-medium.jpg
      last   = FRAN_0464_07118_L-medium.jpg
      first direct URL:
      https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_06736_L-medium.jpg
      last direct URL:
      https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07118_L-medium.jpg

    Range B (435 views):
      first  = FRAN_0464_07119_L-medium.jpg
      last   = FRAN_0464_07553_L-medium.jpg
      gallery URL:
      https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/consultation/multimedia/Galerie.action?irId=FRAN_IR_061975&udId=c-4djk5r1n8--72f9e5zjfghl
      first direct URL:
      https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07119_L-medium.jpg
      last direct URL:
      https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07553_L-medium.jpg
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [int]$StartImage,

    [Parameter(Mandatory = $true)]
    [int]$EndImage,

    [Parameter(Mandatory = $true)]
    [string]$Name,

    [string]$DownloadRoot = "$HOME\Downloads",

    [int]$DelayMilliseconds = 500,

    [int]$Retries = 3,

    [int]$MinimumBytes = 10000
)

$ErrorActionPreference = "Stop"

if ($EndImage -lt $StartImage) {
    throw "EndImage must be greater than or equal to StartImage."
}

$Expected = $EndImage - $StartImage + 1
$OutDir   = Join-Path $DownloadRoot $Name
$PdfOut   = Join-Path $DownloadRoot "$Name.pdf"
$Log      = Join-Path $OutDir "download_log.txt"
$Manifest = Join-Path $OutDir "manifest.tsv"

New-Item -ItemType Directory -Force -Path $OutDir | Out-Null

"gallery_index`timage_id`tfilename`turl" | Set-Content -Encoding UTF8 $Manifest

Write-Host ""
Write-Host "SIV gallery harvest"
Write-Host "-------------------"
Write-Host "Images:    $StartImage .. $EndImage"
Write-Host "Expected:  $Expected"
Write-Host "Directory: $OutDir"
Write-Host "PDF:       $PdfOut"
Write-Host ""

for ($i = $StartImage; $i -le $EndImage; $i++) {

    $galleryIndex = $i - $StartImage + 1
    $id   = "{0:D5}" -f $i
    $file = "FRAN_0464_${id}_L-medium.jpg"
    $url  = "https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/$file"
    $out  = Join-Path $OutDir $file

    "$galleryIndex`t$id`t$file`t$url" | Add-Content -Encoding UTF8 $Manifest

    if (Test-Path $out) {
        $existingLength = (Get-Item $out).Length
        if ($existingLength -ge $MinimumBytes) {
            Write-Host "[$galleryIndex/$Expected] SKIP $file"
            continue
        }
        Remove-Item $out -Force -ErrorAction SilentlyContinue
    }

    $ok = $false

    for ($try = 1; $try -le $Retries; $try++) {
        try {
            Write-Host "[$galleryIndex/$Expected] GET  $file  try=$try"

            Invoke-WebRequest `
                -Uri $url `
                -OutFile $out `
                -Headers @{
                    "User-Agent" = "Mozilla/5.0"
                    "Referer"    = "https://www.siv.archives-nationales.culture.gouv.fr/"
                } `
                -TimeoutSec 60

            if ((Test-Path $out) -and ((Get-Item $out).Length -ge $MinimumBytes)) {
                $ok = $true
                Add-Content -Encoding UTF8 $Log "OK`t$galleryIndex`t$id`t$url"
                break
            }

            Remove-Item $out -Force -ErrorAction SilentlyContinue
            throw "Downloaded file is missing or smaller than $MinimumBytes bytes."
        }
        catch {
            Add-Content -Encoding UTF8 $Log "FAIL`ttry=$try`t$galleryIndex`t$id`t$($_.Exception.Message)"
            if (Test-Path $out) {
                Remove-Item $out -Force -ErrorAction SilentlyContinue
            }
            Start-Sleep -Seconds (2 * $try)
        }
    }

    if (-not $ok) {
        Write-Warning "FAILED after $Retries attempts: $file"
    }

    Start-Sleep -Milliseconds $DelayMilliseconds
}

Write-Host ""
Write-Host "Validating downloaded JPEGs..."

$Images = Get-ChildItem -Path $OutDir -Filter "FRAN_0464_*_L-medium.jpg" |
    Sort-Object Name

$Bad = @($Images | Where-Object Length -lt $MinimumBytes)

Write-Host "Downloaded: $($Images.Count)"
Write-Host "Expected:   $Expected"

if ($Bad.Count -gt 0) {
    Write-Warning "$($Bad.Count) suspiciously small file(s):"
    $Bad | Select-Object Name, Length | Format-Table
}

if ($Images.Count -ne $Expected) {
    Write-Warning "Image count does not match expected count. Re-run the script; valid existing files will be skipped."
    Write-Warning "PDF merge is being skipped until the range is complete."
    exit 2
}

if ($Bad.Count -gt 0) {
    Write-Warning "Small files detected. Re-run before merging."
    exit 3
}

# Locate a Python launcher.
$Python = $null
if (Get-Command py -ErrorAction SilentlyContinue) {
    $Python = "py"
}
elseif (Get-Command python -ErrorAction SilentlyContinue) {
    $Python = "python"
}
else {
    throw "Python was not found. Install Python, then re-run the script."
}

# Install img2pdf if necessary. It streams JPEGs into PDF without loading hundreds
# of decoded images into memory, which is preferable for archival batches.
& $Python -c "import img2pdf" 2>$null
if ($LASTEXITCODE -ne 0) {
    Write-Host "img2pdf not found; installing it for the current Python environment..."
    & $Python -m pip install img2pdf
    if ($LASTEXITCODE -ne 0) {
        throw "Could not install img2pdf."
    }
}

$MergeScript = Join-Path $OutDir "_merge_img2pdf.py"

@'
from pathlib import Path
import img2pdf
import sys

folder = Path(sys.argv[1])
pdf_out = Path(sys.argv[2])

files = sorted(folder.glob("FRAN_0464_*_L-medium.jpg"))
if not files:
    raise SystemExit("No JPEG files found.")

print(f"Merging {len(files)} JPEGs into {pdf_out}")

with pdf_out.open("wb") as fh:
    fh.write(img2pdf.convert([str(p) for p in files]))

print("PDF merge complete.")
'@ | Set-Content -Encoding UTF8 $MergeScript

Write-Host ""
Write-Host "Creating PDF..."
& $Python $MergeScript $OutDir $PdfOut

if ($LASTEXITCODE -ne 0 -or -not (Test-Path $PdfOut)) {
    throw "PDF merge failed."
}

Write-Host ""
Write-Host "DONE"
Write-Host "JPEG directory: $OutDir"
Write-Host "Manifest:       $Manifest"
Write-Host "Log:            $Log"
Write-Host "PDF:            $PdfOut"
