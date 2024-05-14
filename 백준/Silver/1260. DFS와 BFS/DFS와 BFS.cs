using System;
using System.Collections.Generic;

namespace Baekjoon
{
    class Program
    {
        static int firstNum, secondNum, startNum;
        static public int[,] map = new int[1001, 1001];
        static public bool[] visited = new bool[1001];

        static public Queue<int> q = new Queue<int>();

        static void Reset()
        {
            for (int i = 1; i <= firstNum; i++)
            {
                visited[i] = false;

            }
        }
        static void DFS(int startNum)
        {
            visited[startNum] = true;

            Console.Write(startNum + " ");
            for (int i = 1; i <= firstNum; i++)
            {
                if (map[startNum, i] == 1 && visited[i] == false)
                {
                    DFS(i);
                }
            }
        }
        static void BFS(int startNum)
        {
            q.Enqueue(startNum);
            visited[startNum] = true;

            while (q.Count != 0)
            {
                int x = q.Dequeue();
                Console.Write(x + " ");
                for (int i = 1; i <= firstNum; i++)
                {
                    if (map[x, i] == 1 && visited[i] == false)
                    {
                        q.Enqueue(i);
                        visited[i] = true;

                    }
                }
            }
        }

        static void Main(string[] args)
        {
            int[] inputArr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
            firstNum = inputArr[0];
            secondNum = inputArr[1];
            startNum = inputArr[2];

            for (int i = 0; i < secondNum; i++)
            {
                int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
                map[arr[0], arr[1]] = 1;
                map[arr[1], arr[0]] = 1;
            }

            Reset();
            DFS(startNum);
            Console.WriteLine();
            Reset();
            BFS(startNum);

        }
    }
}