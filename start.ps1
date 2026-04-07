# --- 📸 AI-Picture-Tager (Catppuccin Macchiato) ---
Write-Host "--- 📸 AI-Picture-Tager (Wizard) ---" -ForegroundColor Cyan

# 1. Check Virtual Environment
if (Test-Path ".\virtual-env") {
    Write-Host "[Info] Activating your virtual environment..." -ForegroundColor Blue
    .\virtual-env\Scripts\activate.ps1
}

# 2. Check & Install Rich/AI Libraries
Write-Host "[Check] Verifying dependencies and theme engine..." -ForegroundColor Cyan
$ready = python -c "import rich; import torch; print('READY')" 2>$null

if ($ready -ne "READY") {
    Write-Host "[Warning] Missing AI components. Installing now..." -ForegroundColor Yellow
    pip install rich torch transformers pillow rawpy pyexiv2
} else {
    Write-Host "[Success] All systems are GO!" -ForegroundColor Green
}

# 3. Get User Input (Robust Cleaning)
Write-Host "`n📁 Please paste the path to your folder or specific photo:" -ForegroundColor Magenta
$raw = Read-Host "Path"
# Clean up: Remove newlines, carriage returns, trailing spaces, and quotes
$targetPath = $raw.Replace("`n", "").Replace("`r", "").Trim().Trim('"')

# 4. Run with Style
if ($targetPath -and (Test-Path "$targetPath")) {
    $absPath = (Resolve-Path "$targetPath").Path
    Write-Host "🚀 Processing: $absPath" -ForegroundColor Green
    python main.py "$absPath" --threshold 0.05 --recursive
} else {
    Write-Host "❌ Error: Could not find that path! Please check the spelling or paste again." -ForegroundColor Red
}

Write-Host "`n--- Analysis Complete ---" -ForegroundColor Cyan
