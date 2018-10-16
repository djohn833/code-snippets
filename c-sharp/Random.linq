<Query Kind="Statements" />

var random = new Random();

Console.WriteLine(random.Next(1, 21));

var bytes = new byte[16];
random.NextBytes(bytes);
Console.WriteLine(string.Join(", ", bytes.Select(b => b.ToString("x2"))));