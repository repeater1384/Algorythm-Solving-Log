using System;
using static System.Console;

class HelloWorld
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        
        string[] strNums = Console.ReadLine().Split(' ');
        int[] intNums = new int[N];

        for(int i = 0; i < N; i++)
        {
            intNums[i] = int.Parse(strNums[i]);
        }

        Array.Sort(intNums);
        Console.WriteLine($"{intNums[0]} {intNums[N-1]}");

    }
}
