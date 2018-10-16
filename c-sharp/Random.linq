<Query Kind="Statements" />

// Int in range
var random = new Random();
Console.WriteLine(random.Next(1, 21));

// Random bytes
var bytes = new byte[16];
random.NextBytes(bytes);
Console.WriteLine(string.Join(", ", bytes.Select(b => b.ToString("x2"))));