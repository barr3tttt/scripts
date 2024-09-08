#Select Devices > Manage > Download Agent
#Select the Site from the dropdown 
#Copy the token and replace the xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx for the $RMMAgentToken
#Copy the URL and replace the URLHERE for the $DownloadPath

#!ps
#timeout=900000

#maxlength=9000000

$RMMAgentToken = "de4b5998-79ed-4114-9680-a7c534215e4b"

$SoftwarePath = "C:\Windows\Temp\ConnectWiseRMM"

$DownloadPath = "https://prod.setup.itsupport247.net/windows/BareboneAgent/32/JC141Site1(JC141Co)_Windows_OS_ITSPlatform_TKNde4b5998-79ed-4114-9680-a7c534215e4b/MSI/setup"
   
$Filename = "ConnectWise_RMM_Windows_OS_ITSPlatform_TKN$($RMMAgentToken).msi"
   
$SoftwareFullPath = "$($SoftwarePath)\$Filename"
	[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
   
$wc = New-Object System.Net.WebClient
   
if (!(Test-Path $SoftwarePath)) {md $SoftwarePath}

   Set-Location $SoftwarePath

   if ((Test-Path $SoftwareFullPath)) {Remove-Item $SoftwareFullPath}

   $wc.DownloadFile($DownloadPath, $SoftwareFullPath)
msiexec.exe /i $($SoftwareFullPath) /qn /norestart