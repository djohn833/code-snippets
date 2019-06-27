<Query Kind="Program">
  <GACReference>Newtonsoft.Json, Version=10.0.0.0, Culture=neutral, PublicKeyToken=30ad4fe6b2a6aeed</GACReference>
  <Namespace>Newtonsoft.Json</Namespace>
  <Namespace>System.Data</Namespace>
</Query>

void Main()
{
	// Create two DataTable instances.
    DataTable table1 = new DataTable("patients");
    table1.Columns.Add("name");
    table1.Columns.Add("id");
    table1.Rows.Add("sam", 1);
    table1.Rows.Add("mark", 2);

    DataTable table2 = new DataTable("medications");
    table2.Columns.Add("id");
    table2.Columns.Add("medication", typeof(DateTime));
	table2.Rows.Add(3, DBNull.Value);
    table2.Rows.Add(1, new DateTime(2018, 9, 12));
    table2.Rows.Add(2, new DateTime(2018, 9, 11));

    // Create a DataSet and put both tables in it.
    DataSet set = new DataSet("office");
    set.Tables.Add(table1);
    set.Tables.Add(table2);
	
	Console.WriteLine(set.Tables[1].Columns[1]);

	var json = JsonConvert.SerializeObject(set, Newtonsoft.Json.Formatting.Indented, new JsonSerializerSettings
	{
		TypeNameHandling = TypeNameHandling.All
	});
	Console.WriteLine(json);
	
	var set2 = JsonSerializer.Create().Deserialize<DataSet>(new JsonTextReader(new StreamReader(new MemoryStream(Encoding.UTF8.GetBytes(json)))));
	Console.WriteLine(set2.Tables[1].Columns[1]);
	
	dynamic set3 = new
	{
		Tables = new dynamic[][]
		{
			new dynamic[]
			{
				new { name = "sam", id = 1 },
				new { name = "mark", id = 2 },
			},
			new dynamic[]
			{
				new { id = 3, date = DBNull.Value },
				new { id = 1, date = new DateTime(2018, 9, 12) },
				new { id = 2, date = new DateTime(2018, 9, 11) }
			}
		}
	};
	
	json = JsonConvert.SerializeObject(set3, Newtonsoft.Json.Formatting.Indented, new JsonSerializerSettings
	{
		TypeNameHandling = TypeNameHandling.All
	});
	Console.WriteLine(json);
}

// Define other methods and classes here