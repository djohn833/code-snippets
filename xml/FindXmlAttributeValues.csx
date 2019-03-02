using System.Xml.Linq;

var scriptArgs = Env.ScriptArgs;

var elemName = scriptArgs[0];
var attrName = scriptArgs[1];
var filename = scriptArgs[2];

var doc = XDocument.Load(filename);

foreach (var node in doc.Root.Descendants(elemName))
{
    var attribute = node.Attributes(attrName).FirstOrDefault();
    if (attribute != null)
        Console.WriteLine("{0}: {1}", attrName, attribute.Value);
}
