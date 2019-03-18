param (
    [string]$Directory = $(throw "Directory parameter is required.")
)

# Set these as needed
$dllPattern = "*.dll"
$allowedDllReferences = @()

$projectFiles = Get-ChildItem $Directory -Recurse -Include *.csproj

ForEach ($projectFile in $projectFiles) {
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
