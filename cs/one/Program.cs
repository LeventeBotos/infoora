using System;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int Felsoresz(int y, int x, int a)
            {
                int ret = 0;
                return ret;
            }
            void Valami(int a, int b, int c = 0, int p = 1, int q = 1)
            {
                int x = a;
                int y = b;
                int r = 0;
                while (x != y)
                {
                    if (x < y)
                    {
                        r = Felsoresz(y, x, a);

                    }
                    else
                    {
                        r = Felsoresz(x, y, a)
                    }

                }
                Console.WriteLine(a + b);
            }
            Valami(7, 11);
        }
    }

}