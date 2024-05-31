using System;
            
class Program
{
    const bool b = true;
    static void Main()
    {
        A a = new A();
        // for (int i = 0; i < 2; i++)
        // {
        //     Console.WriteLine("" + i);
        // }
        
        // while (true):
        //     break;

        // try
        // {
        //     Console.WriteLine("a");
        // }
        // catch (Exception ex)
        // {
        //     Console.WriteLine("Error inesperado: {ex.Message}");
        // }
    }
}
// abstract class A
// {
//     public abstract void Run();
// }
// public interface B
// {
//     void Run();
// }
// sealed class B
// {
//     public int b(int a)
//     {
//         return a
//     }
// }

public class CLA
{
    const int a = 7;
    public readonly string ReadOnlyProperty;
    public static volatile bool stopThread = false;
    public static extern int MessageBox(IntPtr hWnd, string text, string caption, uint type);
    private bool Lala(int a, string s){
        return a;
    }
    async bool Lalaa(int a, string s){
        return a;
    }
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
}
public unsafe class UnsafeExample{}
public partial class Program{}

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
