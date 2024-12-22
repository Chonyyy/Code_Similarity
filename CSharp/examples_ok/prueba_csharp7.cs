using System;
using System.Collections.Generic;
using System.Threading.Tasks;

class Program
{
    static async Task Main(string[] args)
    {
        Console.WriteLine("C# 7 Features Demo");

        // 1. Out variables
        if (int.TryParse("123", out int result))
        {
            // Console.WriteLine($"Parsed number: {result}");
        }

        // 2. Pattern matching
        object obj = "Hello, World!";
        if (obj is string str)
        {
            // Console.WriteLine($"Pattern matched string: {str}");
        }

        // 3. Tuples and deconstruction
        var tuple = ("Alice", 25);
        // Console.WriteLine($"Name: {tuple.Item1}, Age: {tuple.Item2}");

        (string name, int age) = tuple; // Deconstruction
        // Console.WriteLine($"Deconstructed Name: {name}, Age: {age}");

        // 4. Local functions
        int Add(int x, int y) => x + y;
        // Console.WriteLine($"Local function result: {Add(3, 5)}");

        // 5. Ref returns and locals
        int[] numbers = { 1, 2, 3 };
        ref int refToFirst = ref GetFirstElement(numbers);
        refToFirst = 42; // Modifies the original array

        // 6. Generalized async return types
        var asyncResult = await GetValueAsync();

        // 7. Expression-bodied members
        var person = new Person("John", "Doe");
        Console.WriteLine(person.FullName);

        // 8. Throw expressions
        string message = GetMessage(null); // Throws an exception if null

        // 9. Default literal
        int defaultInt = default;
        // Console.WriteLine($"Default literal value for int: {defaultInt}");
    }

    static ref int GetFirstElement(int[] array) => ref array[0];

    static async Task<int> GetValueAsync()
    {
        await Task.Delay(100);
        return 42;
    }

    static string GetMessage(string input) => input ?? throw new ArgumentNullException(nameof(input));
}

public class Person
{
    public string FirstName { get; }
    public string LastName { get; }

    public Person(string firstName, string lastName) =>
        (FirstName, LastName) = (firstName, lastName); // Tuple deconstruction

    public string FullName => $"{FirstName} {LastName}"; // Expression-bodied property
}
