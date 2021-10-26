function Get-LocalIP {
    $iplocal = Get-NetIPAddress -AddressFamily IPv4
    Write-Output "IP Local: $iplocal"
}

function Get-PublicIP {
    $ippublica = Invoke-WebRequest ifconfig.me -UseBasicParsing | Select -ExpandProperty Content
    Write-Output "IP Publica: $ippublica"
}

function Use-RedNmap {
    $ip = Get-NetIPAddress -AddressFamily IPv4
    $ipaddress = $ip.IPAddress
    $nmap = nmap.exe $ipaddress
    Write-Output "Nmap completado: "$ipaddress $nmap
}

function Use-SiteNmap {
    $url = 'alkapone.tv'
    $nmap1 = nmap.exe $url
    Write-Output "`n" "Nmap completado: "$url $nmap1
}

Get-LocalIP | Out-File -FilePath ./Escaneo.txt
Get-PublicIP | Out-File -FilePath ./Escaneo.txt -Append
Use-RedNmap | Out-File -FilePath ./Escaneo.txt -Append
Use-SiteNmap | Out-File -FilePath ./Escaneo.txt -Append

$txt = '.\Escaneo.txt'
$ENCODED1 = [Convert]::ToBase64String((Get-Content $txt -Encoding Byte)) | Out-File -FilePath ./EncodedTxt.txt
Write-Output "Proceso terminado"
