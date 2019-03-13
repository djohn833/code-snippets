<Query Kind="Program">
  <Namespace>Newtonsoft.Json</Namespace>
</Query>

void Main()
{
	var json = @"{""foo"": 42, ""bar"": 37}";
	
	var dictionary = JsonSerializer.Create().Deserialize<IDictionary<string, object>>(new JsonTextReader(new StreamReader(new MemoryStream(Encoding.UTF8.GetBytes(json)))));
	Console.WriteLine(dictionary);
}

// Define other methods and classes here