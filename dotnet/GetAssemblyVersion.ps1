param (
    [string]$AssemblyFile = $(throw "AssemblyFile parameter is required.")
)

# Get assembly version without loading and locking the file.
# From https://elegantcode.com/2009/12/22/powershell-load-assembly-without-locking-file/
[System.Reflection.AssemblyName]::GetAssemblyName($AssemblyFile).Version.ToString()
