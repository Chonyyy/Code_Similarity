using System;
using System.Collections.Generic;
using System.Runtime.CompilerServices;

// Top-level statements
Console.WriteLine("C# 9.0 Features Demo");
var a = new MyPartialClass();
// 1. Records
record Person(string FirstName, string LastName);

public record Libro(string Titulo, string Autor)
{
    public bool Disponible { get; set; } = true;
}

// 2. Init-only setters
class Car
{
    public string Model { get; init; }
    public int Year { get; init; }
}

// 3. Pattern matching enhancements
static string GetWeatherDisplay(int temperature) => temperature switch
{
    < 0 => "Freezing",
    >= 0 and < 20 => "Cool",
    >= 20 and < 30 => "Warm",
    >= 30 => "Hot",
};

// 4. Native sized integers
nint nativeInt = 42;
nuint nativeUnsignedInt = 42u;
// Console.WriteLine($"Native Int: {nativeInt}, Native Unsigned Int: {nativeUnsignedInt}");

// 5. Function pointers (unsafe context required)
unsafe
{
    delegate*<int, int, int> functionPointer = &Add;
}

static int Add(int a, int b) => a + b;

// 6. Module initializers
[ModuleInitializer]
internal static void Initialize()
{
    Console.WriteLine("Module initialized");
}

// 7. Partial methods with new features
partial class MyPartialClass
{
    public partial int MyMethod();
}

partial class MyPartialClass
{
    public partial int MyMethod() => 42;
}

var partialClassInstance = new MyPartialClass();
// Console.WriteLine($"Partial Method Result: {partialClassInstance.MyMethod()}");

// 8. Target-typed new expressions
List<string> names = new() { "Alice", "Bob", "Charlie" };
Console.WriteLine(string.Join(", ", names)); // Alice, Bob, Charlie

// 9. Static anonymous functions
var adder = static (int a, int b) => a + b;
// Console.WriteLine($"Static Anonymous Function Result: {adder(5, 3)}");

// 10. Target-typed conditional expressions
int? maybe = null;
var definitely = maybe ?? 0;
// Console.WriteLine($"Target-Typed Conditional Expression Result: {definitely}");

// 11. Covariant return types
class Animal
{
    public virtual Animal GetOffspring() => new Animal();
}

class Dog : Animal
{
    public override Dog GetOffspring() => new Dog();
}

Dog dog = new Dog();
Animal offspring = dog.GetOffspring();
// Console.WriteLine($"Covariant Return Type: {offspring.GetType().Name}"); // Dog

// 12. Pattern matching with 'not' pattern
static bool IsNotNull(object obj) => obj is not null;
Console.WriteLine(IsNotNull("Hello")); // True
Console.WriteLine(IsNotNull(null)); // False

// 13. Extension GetEnumerator support for foreach loops
var customCollection = new CustomCollection<int>(new[] { 1, 2, 3 });
foreach (var item in customCollection)
{
    Console.WriteLine($"Custom Collection Item: ");
}

// Custom collection with GetEnumerator extension method support.
public class CustomCollection<T>
{
    private readonly T[] _items;

    public CustomCollection(T[] items) => _items = items;

    public IEnumerator<T> GetEnumerator() => ((IEnumerable<T>)_items).GetEnumerator();
}

// 14. Lambda discard parameters
Func<int, int, int> multiply = (_, y) => y * 2;
// Console.WriteLine($"Lambda Discard Parameters Result: {multiply(5, 3)}");

// 15. Attributes on local functions
void LocalFunctionExample()
{
    // [Obsolete("This local function is obsolete")]
    static void LocalFunction()
    {
        Console.WriteLine("Local function with attribute");
    }

    LocalFunction();
}
LocalFunctionExample();

// Helper Methods for Unsafe Code Example
unsafe static void UnsafeExample()
{
    delegate*<int, int, int> functionPointer = &Add;
}
