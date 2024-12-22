using System;
using System.Collections.Generic;
using System.Numerics;

class Program
{
    static void Main()
    {
        // 1. Raw string literals
        var json = """
        {
            "name": "John Doe",
            "age": 30,
            "city": "New York"
        }
        """;
        Console.WriteLine(json);

        // 2. Generic math support
        Console.WriteLine(Add(5, 3));
        Console.WriteLine(Add(5.5, 3.3));

        // 3. Generic attributes
        var myClass = new MyClass();

        // 4. UTF-8 string literals
        ReadOnlySpan<byte> utf8 = "Hello, world!"u8;

        // 5. Newlines in string interpolation expressions
        // var name = "Alice";
        // var greeting = $"Hello, {name
        //     .ToUpper()
        //     .Trim()}!";
        // Console.WriteLine(greeting);

        // 6. List patterns
        int[] numbers = { 1, 2, 3, 4, 5 };
        if (numbers is [1, 2, .. var rest])
        {
            // Console.WriteLine($"The rest: {string.Join(", ", rest)}");
        }

        // 7. File-local types
        Logger.Log("This is a log message");

        // 8. Required members
        var person = new Person { Name = "John", Age = 30 };

        // 9. Auto-default structs
        var point = new Point();
        // Console.WriteLine($"Default Point: ({point.X}, {point.Y})");

        // 10. Pattern match Span<char> on a constant string
        Span<char> text = "Hello, world!".AsSpan();
        if (text is "Hello, world!")
        {
            Console.WriteLine("Matched!");
        }

        // 11. Extended nameof scope
        var numbersList = new List<int>();
        Console.WriteLine(nameof(numbersList.Count));

        // 12. Numeric IntPtr
        IntPtr ptr = 42;
        Console.WriteLine(ptr + 1);

        // 13. ref fields and scoped ref
        var refPoint = new RefPoint();
        int x = 10, y = 20;
        refPoint.X = ref x;
        refPoint.Y = ref y;
        // Console.WriteLine($"RefPoint: ({refPoint.X}, {refPoint.Y})");
    }

    public static T Add<T>(T a, T b) where T : INumber<T>
    {
        return a + b;
    }
}

[GenericAttribute<int>(42)]
public class MyClass { }

public class GenericAttribute<T> : Attribute
{
    public T Value { get; }
    public GenericAttribute(T value) => Value = value;
}

file class Logger
{
    public static void Log(string message) => Console.WriteLine(message);
}

public class Person
{
    public required string Name { get; set; }
    public required int Age { get; set; }
}

public struct Point
{
    public int X { get; set; }
    public int Y { get; set; }
    
    public Point() { }
}

ref struct RefPoint
{
    public ref int X;
    public ref int Y;
}
