#YET TO BE SOLVED

'''
Print right-angled triangle pattern. See example for more details.

Input Format

First line of input contains a single integer N - the size of the triangle.

Constraints

1 <= N <= 50

Output Format

For the given integer, print the right-angled triangle pattern.

Sample Input 0

5
Sample Output 0

1
2 6
3 7 10
4 8 11 13
5 9 12 14 15
Explanation 0

Self Explanatory
'''
import java.io.*;
import java.util.*;

public class Solution {
 public static void main(String[] args)
 {
     Scanner sc=new Scanner(System.in);
     int l=sc.nextInt();
     int i=1, j=0, k=0, m=0;
     System.out.print(i+" ");
     System.out.println("");
     for(i=2;i<=l;i++)
     {
         System.out.print(i+" ");
         k=l-1;
         m=i;
         for(j=1;j<i;j++)
         {
             m=m+k;
             System.out.print(m+" ");
             k--;
         }
         System.out.println("");
     }
 }
}
