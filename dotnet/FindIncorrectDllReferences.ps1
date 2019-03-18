param (
    [string]$Directory = $(throw "Directory parameter is required.")
)

# Configurable variables. Set these as needed
$dllPattern = "*.dll"
$allowedDllReferences = @()
# End configurable variables.

ForEach ($projectFile in Get-ChildItem $Directory -Recurse -Include *.csproj) {
    $matches = Select-String $projectFile -Pattern $dllPattern |
        Where-Object { $allowedDllReferences -notcontains $_.Matches[0].Groups[1] }

    If ($matches)
    {
        Write-Host $projectFile
        
        ForEach ($match in $matches) {
            Write-Host -NoNewline "`t"
            Write-Host $match.Matches[0]
        }
    }
}
