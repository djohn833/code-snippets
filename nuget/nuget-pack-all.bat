@ECHO OFF

for /r %%f in (*.nuspec) do nuget pack -OutputDirectory "%1" "%%f"
