using System;

namespace MyNamespace{
class Program
{
    const bool b = true;
    public delegate void Callback(string message);  
    static void Main()
    {
        Tuple<string, int, string> person = new Tuple<string, int, string>("Steve", 56, "Jobs");

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
        var cuadrados = numeros.Select(x => x * x);
        var pares = numeros.Where(x => x % 2 == 0);
        var grupos = numeros.GroupBy(x => x % 2 == 0? "Pares" : "Impares");
        var estudiantes = new List<string> { "Juan", "Ana", "Carlos" };
        var cursos = new List<string> { "Matemáticas", "Historia", "Ciencias" };

        // var inscripciones = estudiantes.Join(cursos, est => est, curso => curso, (est, curso) => $"{est} está inscrito en {curso}");
        A a = new A();
        for (int i = 0; i < 2; i++)
        {
            Console.WriteLine("" + i);
        }
        var frutas = new List<string> { "manzana", "banana", "naranja", "kiwi" };

        var ordenadas = frutas.OrderBy(x => x);
        
        while (true)
        {
            break;
        }
        // Console.WriteLine("a");
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
    enum Level
    {
        Low,
        Medium,
        High
    }
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
        return a;
    }
}
class Person
{
  private string name;
  public string Name 
  {
    get { return name; }
    set { name = value; } 
  }
}

}