using System;
using System.Collections.Generic;
using System.Linq;
/*
    * solution to the HackerRank problem "Balanced Brackets"
    * https://www.hackerrank.com/challenges/balanced-brackets/problem
*/
class Solution {
    static string isBalanced(string s)
    {
        var stack = new List<char>();
        char[] brackets = new char[] { '{','}','(', ')', '[', ']' };
        char[] cArr = s.ToCharArray();
        bool match = true;
        int i = 0;
        int k;
        if (brackets.ToList().IndexOf(cArr[0]) % 2 == 1)
            match = false;
        while (match && i < cArr.Length)
        {
            k = brackets.ToList().IndexOf(cArr[i]);
            if (k % 2 == 0)
                stack.Add(cArr[i]);
            else
            {
                if (stack != null && stack.Any())
                {
                    match = stack.Last() == brackets[k - 1];
                    stack.RemoveAt(stack.Count() - 1);
                }
            }
            i++;
        }
        if (stack.Any())
            match = false;
        return match ? "YES" : "NO";
    }
        
    static void Main(String[] args) {
        int t = Convert.ToInt32(Console.ReadLine());

        for (int tItr = 0; tItr < t; tItr++) {
            string s = Console.ReadLine();

            string result = isBalanced(s);

            Console.WriteLine(result);
        }
    }
}