// using System;

namespace MyNamespace1{

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
    static void SumaDeDos(out int resultado, out int primerNumero, out int segundoNumero)
    {
        primerNumero = 5;
        segundoNumero = 10;
        resultado = primerNumero + segundoNumero;
    }
    public virtual double CalculateArea()
    {
        return 0;
    }
    public override string GetShapeType()
    {
        return "This is a rectangle";
    }
    public async Task MainAsync()
    {
        await Task.Delay(1000); // Espera 1 segundo
        Console.WriteLine("¡Operación asíncrona completada!");
    }
}
public unsafe class UnsafeExample{}
public partial class Program{}

sealed class Singleton {
    private static Singleton _instance;

    private Singleton() { }

    public static Singleton Instance {
        get {
            if (_instance == null) {
                _instance = new Singleton();
            }
            return _instance;
        }
    }
}
}