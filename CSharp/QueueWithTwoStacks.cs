using System;
using System.Collections.Generic;
using System.IO;
class Solution {
    static void Main(String[] args) {
        MyQueue myQueue = new MyQueue();
        int queries = int.Parse(Console.ReadLine());
        for(int i=1; i<=queries; i++)
        {
            string queryCmd = Console.ReadLine();
            var query = queryCmd.Split(' ');
            var cmd = query[0];
            if (cmd.Equals("1"))
                myQueue.Enqueue(int.Parse(query[1]));
            else if (cmd.Equals("2"))
                myQueue.Dequeue();
            else if (cmd.Equals("3"))
                Console.WriteLine(myQueue.GetFront());
        }
    }
}

internal class MyQueue
{
    private Stack<int> stack1;
    private Stack<int> stack2;
    private int front;

    public MyQueue()
    {
        stack1 = new Stack<int>();
        stack2 = new Stack<int>();
        front = 0;
    }
    public void Enqueue(int val)
    {
        if(stack1.Count == 0)
            front = val;
        stack1.Push(val);
    }

    public int Dequeue()
    {
        if (stack2.Count == 0) {
            while(stack1.Count > 0)
                stack2.Push(stack1.Pop());
        }
        return stack2.Pop();
    }

    public int GetFront()
    {
        if(stack2.Count > 0)
            return stack2.Peek();

        return front;
    }
}
