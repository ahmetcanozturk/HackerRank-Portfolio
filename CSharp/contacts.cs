using System;
using System.Collections.Generic;
using System.Linq;
/*
    * solution to the HackerRank problem "Contacts"
    * https://www.hackerrank.com/challenges/contacts/problem
    * Ahmetcan Ozturk
*/
class Solution {
    static int[] contacts(string[][] queries) {
        var results = new List<int>();
        var dict = new Dictionary<string, int>();
        for (int i = 0; i < queries.Length; i++)
        {
            string[] data = queries[i];
            if (data[0].Equals("add"))
            {
                for (int j = 1; j <= data[1].Length; j++)
                {
                    string sub = data[1].Substring(0, j);
                    if (!dict.ContainsKey(sub))
                        dict.Add(sub, 1);
                    else
                        dict[sub] = dict[sub] + 1;
                }
            }
            else
            {
                if (!dict.ContainsKey(data[1]))
                    results.Add(0);
                else
                    results.Add(dict[data[1]]);
            }
        }

        return results.ToArray();
    }

    static void Main(string[] args) {
        int queriesRows = Convert.ToInt32(Console.ReadLine());

        string[][] queries = new string[queriesRows][];

        for (int queriesRowItr = 0; queriesRowItr < queriesRows; queriesRowItr++) {
            queries[queriesRowItr] = Console.ReadLine().Split(' ');
        }

        int[] result = contacts(queries);

        Console.WriteLine(string.Join("\n", result));
    }
}
