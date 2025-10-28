param (
    [string]$Target = "8.8.8.8",
    [int]$Port = 53
)

$logFile = "network_log.txt"

function Log {
    param([string]$message)
    Add-Content $logFile "$(Get-Date) - $message"
    Write-Output $message
}


if (Test-Connection $Target -Count 1 -Quiet) {
    Log "Ping to $Target successful"
} else {
    Log "Ping to $Target failed"
}


try {
    $tcp = New-Object System.Net.Sockets.TcpClient
    $tcp.Connect($Target, $Port)
    Log "Port $Port on $Target is open"
} catch {
    Log "Port $Port on $Target is closed"
} finally {
    if ($tcp) { $tcp.Close() }
}