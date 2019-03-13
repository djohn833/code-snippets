<Query Kind="Program" />

void Main()
{
	foreach (var dll in Directory.GetFiles(@"SearchPath", "*.dll"))
	{
		var assembly = Assembly.LoadFile(dll);
		
		//foreach (var type in assembly.GetTypes().Where(t => t.GetInterfaces().Any(i => i.FullName == "Telerik.Windows.Documents.FormatProviders.IDocumentFormatProvider")))
		foreach (var type in assembly.GetTypes().Where(t => t.GetInterfaces().Any(i => i.FullName == "Telerik.Windows.Documents.FormatProviders.Html.IConfigurableHtmlFormatProvider")))
		{
			Console.WriteLine("{0}\t{1}", dll, type.FullName);
		}
	}
}

// Define other methods and classes here
