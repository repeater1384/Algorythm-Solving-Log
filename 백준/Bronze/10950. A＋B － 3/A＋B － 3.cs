using System;

class HelloWorld
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        for(int i = 0; i < N; i++)
        {
            string[] temp = Console.ReadLine().Split(' ');
            int a = int.Parse(temp[0]);
            int b = int.Parse(temp[1]);
            Console.WriteLine(a + b);
        }
        
    }
}