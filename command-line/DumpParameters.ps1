param (
    [string]$A,
    [string]$B,
    [string]$C,
    [string]$D,
    [string]$E
)

$ParameterList = (Get-Command -Name $MyInvocation.InvocationName).Parameters;
ForEach ($key in $ParameterList.keys)
{
    $var = Get-Variable -Name $key -ErrorAction SilentlyContinue;
    If ($var) {
        Write-Host "$($var.name): $($var.value)"
    }
}
