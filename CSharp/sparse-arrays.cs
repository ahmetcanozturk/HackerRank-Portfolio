using System;
using System.Collections.Generic;

/*
    * solution to the HackerRank problem "Sparse Arrays"
    * https://www.hackerrank.com/challenges/sparse-arrays/problem
*/
class Solution {

    static int[] matchingStrings(string[] strings, string[] queries) {
        int[] result = new int[queries.Length];
        for(int i=0; i<result.Length; i++) {
            result[i] = 0;
            for(int j = 0; j < strings.Length; j++)
                if(strings[j].Equals(queries[i]))
                    result[i] += 1;
        }
        return result;
    }

    static void Main(string[] args) {

        int stringsCount = Convert.ToInt32(Console.ReadLine());

        string[] strings = new string [stringsCount];

        for (int i = 0; i < stringsCount; i++) {
            string stringsItem = Console.ReadLine();
            strings[i] = stringsItem;
        }

        int queriesCount = Convert.ToInt32(Console.ReadLine());

        string[] queries = new string [queriesCount];

        for (int i = 0; i < queriesCount; i++) {
            string queriesItem = Console.ReadLine();
            queries[i] = queriesItem;
        }

        int[] res = matchingStrings(strings, queries);

        Console.WriteLine(string.Join("\n", res));
    }
}
