using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            int num = Int32.Parse(Console.ReadLine());

            for (int i = 1; i <= num; i++)
            {
                for (int blank = num; blank > i; blank--)
                {
                    Console.Write(" ");
                }
                for (int star = 0; i > star; star++)
                {
                    Console.Write("*");
                }
                Console.WriteLine();
            }
        }
    }
}