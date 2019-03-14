param (
    [string]$Directory = $(throw "Directory parameter is required."),
    [string[]]$Files = $(throw "Files parameter is required.")
)

tf checkout (gci $Directory -Recurse -Include $Files | Resolve-Path -Relative)
