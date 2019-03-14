param (
    # e.g., {http://schemas.telerik.com/2008/xaml/presentation}RadDatePicker
    [string]$ElementName = $(throw "ElementName parameter is required."),
    # e.g., Width
    [string]$AttributeName = $(throw "AttributeName parameter is required."),
    [string]$FileName = $(throw "FileName parameter is required.")
)

[Reflection.Assembly]::LoadWithPartialName("System.Xml.Linq") | Out-Null

$document = [System.Xml.Linq.XDocument]::Load($FileName)

ForEach ($node in $document.Root.Descendants($ElementName)) {
    $attribute = [Linq.Enumerable]::FirstOrDefault($node.Attributes($AttributeName))
    If ($attribute) {
        Write-Host "${AttributeName}: $($attribute.Value)"
    }
}
