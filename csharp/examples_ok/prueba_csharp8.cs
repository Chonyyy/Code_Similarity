using System;
using System.Collections.Generic;
using System.Threading.Tasks;

#nullable enable

// Ejemplo de miembros de solo lectura
struct Point
{
    public int X, Y;

    public readonly void ResetX() => X = 0; // Esto causará un error si se intenta modificar
}

// Ejemplo de métodos de interfaz predeterminados
public interface IShape
{
    double Area();
    void Draw() => Console.WriteLine("Drawing a shape.");
}

public class Circle : IShape
{
    public double Area() => Math.PI * 2 * 2; // Radio 2
}

// Ejemplo de expresiones switch
public class Program
{
    public static void Main()
    {
        // Miembros de solo lectura
        Point p = new Point { X = 5, Y = 10 };
        // p.ResetX(); // Descomentar causará error: No se puede modificar 'X' en un método readonly

        // Métodos de interfaz predeterminados
        IShape shape = new Circle();
        shape.Draw(); // Salida: Drawing a shape.

        // Expresiones switch
        string fruit = "Apple";
        string result = fruit switch
        {
            "Apple" => "This is an apple.",
            "Banana" => "This is a banana.",
            _ => "Unknown fruit."
        };
        Console.WriteLine(result); // Salida: This is an apple.

        // Patrones de propiedades
        PrintName(new Person { Name = "Alice" });

        // Patrones de tupla
        var tuple = (1, "apple");
        if (tuple is (1, var fruitName))
        {
            Console.WriteLine(fruitName); // Salida: apple
        }

        // Declaraciones using
        using var stream = new System.IO.MemoryStream();
        
        // Funciones locales estáticas
        OuterMethod();

        // Estructuras ref descartables (ejemplo simplificado)
        DisposableRefStruct drs = new DisposableRefStruct();
        
        // Tipos de referencia anulables
        Person personWithNullName = new Person { Name = null }; 
        Console.WriteLine(personWithNullName.Name); // Salida: (null)

        // Secuencias asincrónicas
        AsyncExample().GetAwaiter().GetResult();

        // Índices y rangos
        int[] numbers = { 1, 2, 3, 4, 5 };
        var lastNumber = numbers[^1]; // Accede al último elemento.
        var subArray = numbers[1..4]; // Obtiene un rango desde el índice 1 hasta el índice 3.
        
        Console.WriteLine($"Last number: {lastNumber}"); // Salida: Last number: 5
        Console.WriteLine($"SubArray: {string.Join(", ", subArray)}"); // Salida: SubArray: 2, 3, 4

        // Asignación combinada con null-coalescing
        string? name = null;
        name ??= "Default Name"; 
        Console.WriteLine(name); // Salida: Default Name.
    }

    static void PrintName(object obj)
    {
        if (obj is Person { Name: var name })
        {
            Console.WriteLine(name);
        }
    }

    static void OuterMethod()
    {
        static void InnerStaticMethod()
        {
            Console.WriteLine("Static local function.");
        }

        InnerStaticMethod();
    }

    public static async IAsyncEnumerable<int> GetNumbersAsync()
    {
        for (int i = 0; i < 5; i++)
        {
            await Task.Delay(100); // Simula trabajo asincrónico.
            yield return i;
        }
    }

    static async Task AsyncExample()
    {
        await foreach (var number in GetNumbersAsync())
        {
            Console.WriteLine(number);
        }
    }
}

// Estructura ref descartable
ref struct DisposableRefStruct : IDisposable
{
    public void Dispose() 
    { 
         Console.WriteLine("Disposed."); 
         /* liberar recursos */ 
    }
}

// Clase para el ejemplo de tipos anulables
public class Person
{
    public string? Name { get; set; } // Puede ser nulo.
}
