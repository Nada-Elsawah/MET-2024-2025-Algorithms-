using System;
using System.Collections.Generic;

class ScheduleGraph
{
    private int NumCourses;
    private List<int>[] Graph;

    public ScheduleGraph(int numCourses)
    {
        NumCourses = numCourses;
        Graph = new List<int>[numCourses];
        for (int i = 0; i < numCourses; i++)
        {
            Graph[i] = new List<int>();
        }
    }

    public void AddEdge(int u, int v)
    {
        Graph[u].Add(v);
        Graph[v].Add(u);
    }

    public int[] GenerateSchedule()
    {
        int[] result = new int[NumCourses]; // The color schedule for each course
        bool[] availableColors = new bool[NumCourses];

        for (int i = 0; i < NumCourses; i++)
        {
            result[i] = -1;
        }

        result[0] = 0; // First course gets the first color

        for (int u = 1; u < NumCourses; u++)
        {
            foreach (int i in Graph[u])
            {
                if (result[i] != -1)
                {
                    availableColors[result[i]] = true;
                }
            }

            int color = -1;
            for (int cr = 0; cr < NumCourses; cr++)
            {
                if (!availableColors[cr])
                {
                    color = cr;
                    break;
                }
            }

            result[u] = color;

            foreach (int i in Graph[u])
            {
                if (result[i] != -1)
                {
                    availableColors[result[i]] = false;
                }
            }
        }

        return result;
    }
}

class Program
{
    static void Main(string[] args)
    {
        // Collecting user data (number of courses, student groups, etc.)
        Console.Write("Enter the number of courses: ");
        int numCourses = int.Parse(Console.ReadLine());

        Console.Write("Enter the number of student groups (as edges between courses): ");
        int numEdges = int.Parse(Console.ReadLine());

        ScheduleGraph graph = new ScheduleGraph(numCourses);

        for (int i = 0; i < numEdges; i++)
        {
            Console.Write("Enter the courses that share students (two courses): ");
            string[] input = Console.ReadLine().Split(' ');
            int u = int.Parse(input[0]);
            int v = int.Parse(input[1]);
            graph.AddEdge(u, v);
        }

        int[] schedule = graph.GenerateSchedule();
        for (int i = 0; i < schedule.Length; i++)
        {
            Console.WriteLine($"Course {i} will have the exam on day {schedule[i] + 1}");
        }
    }
}

