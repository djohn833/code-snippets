param (
    [string]$A,
    [string]$B,
    [string]$C,
    [string]$D,
    [string]$E
)

# From https://stackoverflow.com/questions/21559724/getting-all-named-parameters-from-powershell-including-empty-and-set-ones/21560957
$ParameterList = (Get-Command -Name $MyInvocation.InvocationName).Parameters;
ForEach ($key in $ParameterList.keys)
{
    $var = Get-Variable -Name $key -ErrorAction SilentlyContinue;
    If ($var) {
        Write-Host "$($var.name): $($var.value)"
    }
}
