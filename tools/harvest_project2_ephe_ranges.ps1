<#
Run the two Archives nationales SIV image ranges recovered during the
2026-08-19 Project 2 sweep. Each range is downloaded and merged to PDF by
harvest_siv_gallery.ps1.

Recovered direct-image sequences:

Range A — 383 views
  https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_06736_L-medium.jpg
  ...
  https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07118_L-medium.jpg

Range B — 435 views
  gallery:
  https://www.siv.archives-nationales.culture.gouv.fr/siv/rechercheconsultation/consultation/multimedia/Galerie.action?irId=FRAN_IR_061975&udId=c-4djk5r1n8--72f9e5zjfghl

  https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07119_L-medium.jpg
  ...
  https://www.siv.archives-nationales.culture.gouv.fr/mm/media/download/FRAN_0464_07553_L-medium.jpg

Output PDFs:
  ~/Downloads/EPHE_FRAN0464_06736_07118.pdf
  ~/Downloads/EPHE_FRAN0464_07119_07553.pdf
#>

$Here = Split-Path -Parent $MyInvocation.MyCommand.Path
$Harvester = Join-Path $Here "harvest_siv_gallery.ps1"

if (-not (Test-Path $Harvester)) {
    throw "Cannot find harvester: $Harvester"
}

& $Harvester `
    -StartImage 6736 `
    -EndImage 7118 `
    -Name "EPHE_FRAN0464_06736_07118"

if ($LASTEXITCODE -ne 0) {
    throw "Range A failed. Re-run after checking the log in Downloads."
}

& $Harvester `
    -StartImage 7119 `
    -EndImage 7553 `
    -Name "EPHE_FRAN0464_07119_07553"

if ($LASTEXITCODE -ne 0) {
    throw "Range B failed. Re-run after checking the log in Downloads."
}

Write-Host ""
Write-Host "Both Project 2 SIV ranges completed."
