using System;
    
class Program
{
    const bool b = true;
    static void Main()
    {
        suma = 2 + 5;
        // Console.WriteLine("a");
        List<int> numeros = new List<int>() { 1, 2, 3, 4, 5 };
        Math.pow(5,2);
        Dictionary<string, string> personas = new Dictionary<string, string>()
        {
            {"Juan", "Desarrollador"}
        };
        var conteo = numeros.Count();
        var suma = numeros.Sum();
        public delegate void Callback(string message);  
        enum Level
        {
            Low,
            Medium,
            High
        }
        // var cuadrados = numeros.Select(x => x * x);
        // var pares = numeros.Where(x => x % 2 == 0);
        // var grupos = numeros.GroupBy(x => x % 2 == 0? "Pares" : "Impares");
        // var estudiantes = new List<string> { "Juan", "Ana", "Carlos" };
        // var cursos = new List<string> { "Matemáticas", "Historia", "Ciencias" };

        // var inscripciones = estudiantes.Join(cursos, est => est, curso => curso, (est, curso) => $"{est} está inscrito en {curso}");
        // A a = new A();
        // for (int i = 0; i < 2; i++)
        // {
            // Console.WriteLine("" + i);
        // }
        // var frutas = new List<string> { "manzana", "banana", "naranja", "kiwi" };

        // var ordenadas = frutas.OrderBy(x => x);
        
        // while (true):
        //     break;
        Console.WriteLine("a");
        try
        {
            Console.WriteLine("a");
        }
        catch (Exception ex)
        {
            Console.WriteLine("Error inesperado: {ex.Message}");
        }
    }
}
abstract class A
{
    public abstract void Run();
}
public interface B
{
    void Run();
}
sealed class B
{
    public int b(int a)
    {
        return a
    }
}

// public class CLA
// {
    // const int a = 7;
    // public readonly string ReadOnlyProperty;
    // public static volatile bool stopThread = false;
    // public static extern int MessageBox(IntPtr hWnd, string text, string caption, uint type);
    // private bool Lala(int a, string s){
    //     return a;
    // }
    // async bool Lalaa(int a, string s){
    //     return a;
    // }
    // static void SumaDeDos(out int resultado, out int primerNumero, out int segundoNumero)
    // {
    //     primerNumero = 5;
    //     segundoNumero = 10;
    //     resultado = primerNumero + segundoNumero;
    // }
    // public virtual double CalculateArea()
    // {
    //     return 0;
    // }
    // public override string GetShapeType()
    // {
    //     return "This is a rectangle";
    // }
    // public async Task MainAsync()
    // {
    //     await Task.Delay(1000); // Espera 1 segundo
    //     Console.WriteLine("¡Operación asíncrona completada!");
    // }
// }
// public unsafe class UnsafeExample{}
// public partial class Program{}

// sealed class Singleton {
//     private static Singleton _instance;

//     private Singleton() { }

//     public static Singleton Instance {
//         get {
//             if (_instance == null) {
//                 _instance = new Singleton();
//             }
//             return _instance;
//         }
//     }
// }
