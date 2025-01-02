using System;


using Point = (int X, int Y);

public class Program
{
    public struct InlineArrayStruct
    {
        public int[5] Values;
    }
    public static void Main()
    {
        // 1. Primary Constructors
        var person = new Person("Alice", 30);
        Console.WriteLine($"{person.Name}, {person.Age}");

        // 2. Collection Expressions
        var numbers = new[] { 1, 2, 3 };
        var moreNumbers = new[] { 4, 5, ..numbers };
        Console.WriteLine(string.Join(", ", moreNumbers));
        
        var numbers = [1, 2, 3];
        var moreNumbers = [4, 5, ..numbers];


        // 3. Inline Arrays
        var fixedArray = new FixedArrayStruct();
        fixedArray.Values[0] = 10;
        Console.WriteLine(fixedArray.Values[0]);

        var inlineArray = new InlineArrayStruct();
        inlineArray.Values[0] = 10;


        // 4. Optional Parameters in Lambda Expressions
        Func<int, int> add = (x, y = 5) => x + y;
        Console.WriteLine(add(3,4));

        // 5. Ref Readonly Parameters
        int number = 42;
        PrintValue(ref number);

        // 6. Alias Any Type
        StringAlias greeting = "Hello, World!";
        Console.WriteLine(greeting);

        
        Point p = (10, 20);

    }
    // 7. Experimental Attribute (conceptual example)
    [Experimental("ExperimentalFeatures")]
    public class ExperimentalClass
    {
        public void ExperimentalMethod() => Console.WriteLine("This is experimental");
    }

    // Classes and methods for examples:
    //  Primary Constructors
    public class Person(string name, int age)
    {
        public string Name { get; } = name;
        public int Age { get; } = age;
    }

    public struct FixedArrayStruct
    {
        public int[] Values = new int[5];
    }

    // Ref Readonly Parameters
    public static void PrintValue(ref readonly int value)
    {
        Console.WriteLine(value);
    }

    // Ref Readonly Parameters in lambdas
    Func<ref readonly int, int> doubleValue = (ref readonly int x) => x * 2;
    int value = 5;

    // Experimental Attribute
    [Experimental("This feature is experimental.")]
    public static void ExperimentalFeature()
    {
        Console.WriteLine("This is an experimental feature.");
        Console.WriteLine(doubleValue(ref value)); // Output: 10
    }
}

