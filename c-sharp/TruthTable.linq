<Query Kind="Statements" />

var values = new [] { "false", " true" };

var query =
	from a in values
	from b in values
//	from c in values
//	from d in values
	select new[] { a, b };

foreach (var row in query)
	Console.WriteLine(string.Join(", ", row) + ", ");
