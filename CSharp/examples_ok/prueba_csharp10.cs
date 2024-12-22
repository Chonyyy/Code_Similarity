using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;

// 1. Record structs
public record struct Point(int X, int Y);

// 2. Improvements of structure types
public struct ImprovedStruct
{
    public int Value { get; set; }
}

// 3. Interpolated string handlers
public class InterpolatedStringHandlerDemo
{
    public static void Main()
    {
        var name = "Alice";
        var greeting = new Greeting($"Hello!");
        // var greeting = new Greeting($"Hello, {name}!");
        Console.WriteLine(greeting.Message);
    }
}

public class Greeting
{
    public string Message { get; }

    public Greeting(string message) => Message = message;
}

// 4. Global using directives
// This can be placed at the top of the file or in a separate file.
global using System;
global using System.Collections.Generic;

// 5. File-scoped namespace declaration
namespace MyNamespace; // This applies to the entire file

// 6. Extended property patterns
public class Car
{
    public string Make { get; set; }
    public string Model { get; set; }
    public int Year { get; set; }
}

public static void PrintCarDetails(Car car)
{
    if (car is { Make: "Tesla", Model: "Model S", Year: > 2020 })
    {
        // Console.WriteLine($"Car is a recent Tesla Model S: {car.Year}");
        Console.WriteLine($"Car is a recent Tesla Model S: ");
    }
}

// 7. Lambda expressions can have a natural type
Func<int, int, int> add = (x, y) => x + y;

// 8. Lambda expressions can declare a return type
Func<int, int, int> multiply = (int x, int y) => x * y;

// 9. Attributes can be applied to lambda expressions
[Obsolete("This lambda is obsolete")]
Func<int, int> obsoleteLambda = x => x + 1;

// 10. Const strings can be initialized using string interpolation
// const string greetingMessage = $"Hello, {nameof(MyNamespace)}!";
const string greetingMessage = $"Hello!";

// 11. Sealed modifier on ToString in a record type
public sealed record Person(string FirstName, string LastName)
{
    public override string ToString() => $"name";
}

// 12. Warnings for definite assignment and null-state analysis are more accurate

public void CheckValue(int? value)
{
    if (value is not null)
    {
        Console.WriteLine($"Value");
    }
}

// 13. Allow both assignment and declaration in the same deconstruction
(int x, int y) = (1, 2);
// Console.WriteLine($"Deconstructed values: x = {x}, y = {y}");

// 14. Allow AsyncMethodBuilder attribute on methods
[AsyncMethodBuilder(typeof(MyAsyncMethodBuilder))]
public static async Task MyAsyncMethod()
{
    await Task.Delay(1000);
}

// Custom AsyncMethodBuilder for demonstration purposes
public struct MyAsyncMethodBuilder
{
    public static MyAsyncMethodBuilder Create() => new MyAsyncMethodBuilder();
    
    public void Start<TState>(ref TState state) {}
    
    public void SetResult() {}
    
    public void SetException(Exception exception) {}
    
    public Task Task => Task.CompletedTask;
}

// 15. CallerArgumentExpression attribute
public void LogMessage(string message, [CallerArgumentExpression("message")] string expression = "")
{
    // Console.WriteLine($"Message: {message}, Expression: {expression}");
}

// Testing the features in Main method.
public static void Main(string[] args)
{
    // Test Record Structs
    var point = new Point(10, 20);
    // Console.WriteLine($"Point: X={point.X}, Y={point.Y}");

    // Test Improvements of Structure Types
    var improvedStruct = new ImprovedStruct { Value = 42 };
    // Console.WriteLine($"Improved Struct Value: {improvedStruct.Value}");

    // Test Extended Property Patterns
    var car = new Car { Make = "Tesla", Model = "Model S", Year = 2021 };
    PrintCarDetails(car);

    // Test Lambda Expressions with Natural Types and Return Types
    // Console.WriteLine($"Addition Result: {add(3, 5)}");
    // Console.WriteLine($"Multiplication Result: {multiply(3, 5)}");

    // Test Const Strings with Interpolation
    Console.WriteLine(greetingMessage);

    // Test Sealed Modifier on ToString in a Record Type
    var person = new Person("John", "Doe");
    Console.WriteLine(person.ToString());

    // Test Warnings for Definite Assignment and Null-State Analysis 
    CheckValue(10);

    // Test Deconstruction Assignment
    (int a, int b) = (5, 10);
    // Console.WriteLine($"Deconstructed Assignment: a={a}, b={b}");

    // Call Async Method (for demonstration purposes)
    MyAsyncMethod().Wait();

    // Test CallerArgumentExpression attribute 
    LogMessage("This is a test message.");
}
