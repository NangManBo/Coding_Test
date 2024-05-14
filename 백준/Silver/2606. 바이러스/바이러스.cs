using System;
using System.Collections.Generic;

namespace Baekjoon
{

    class Program
    {
        static int firstNum, secondNum;
        static int count;
	      static public int[,] map = new int[101, 101]; // 숫자 담을 배열
        static public bool[] visited = new bool[101]; // 해당 번호를 지나갔는지 안지나갔는지

        static public Queue<int> q = new Queue<int>();

        static void Reset()
        {
            for (int i = 1; i <= firstNum; i++)
            {
                visited[i] = false; // 방문 모두다 false
            }
        }

        static void BFS()
        {
            q.Enqueue(1); // 문제에서는 1번에 대해 연결 되어서 있는 것들 찾기 때문에 1
            visited[1] = true;

            while (q.Count != 0)
            {
                int x = q.Dequeue();
                count++;
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
            firstNum = Convert.ToInt32(Console.ReadLine());//처음 컴퓨터 갯수
            secondNum = Convert.ToInt32(Console.ReadLine());//컴퓨터가 직접 연결된 수

            for (int i = 0; i < secondNum; i++)//연결된 컴퓨터 수 만
            {
                int[] arr = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
                map[arr[0], arr[1]] = 1;
                map[arr[1], arr[0]] = 1;
            }

            Reset();
            BFS();
            Console.WriteLine(count - 1);
        }
    }
}