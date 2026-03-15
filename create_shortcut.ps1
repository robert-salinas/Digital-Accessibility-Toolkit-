$sLinkFile = "$env:USERPROFILE\Desktop\DAT-Toolkit.lnk" 
$sTargetFile = "$PSScriptRoot\run_app.bat" 
$sIconFile = "$PSScriptRoot\assets\icon.ico" # Asegurate de tener un icono ahí (Opcional)
$WshShell = New-Object -ComObject WScript.Shell 
$Shortcut = $WshShell.CreateShortcut($sLinkFile) 
$Shortcut.TargetPath = $sTargetFile 
if (Test-Path $sIconFile) {
    $Shortcut.IconLocation = $sIconFile 
}
$Shortcut.WorkingDirectory = $PSScriptRoot 
$Shortcut.Save()
Write-Host "[OK] Acceso directo 'DAT-Toolkit' creado en el Escritorio." -ForegroundColor Green
