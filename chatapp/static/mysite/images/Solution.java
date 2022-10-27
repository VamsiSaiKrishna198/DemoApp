import java.util.Scanner;
class solution
{
    public static void main(String args[])
    {
        Scanner in=new Scanner(System.in);
        int t;
        t=in.nextInt();
        while(t>0)
        {
            int m=in.nextInt();
            int n=in.nextInt();
            int p=in.nextInt();
            int a[][]=new int[m][n];
            for(int i=0;i<m;i++)
            {
              for(int j=0;j<n;j++)
              {
                  a[i][j]=in.nextInt();
              }
            }
            System.out.println(""+p);
            int sum=0;
            for(int i=0;i<n;i++)
            {
                for(int j=0;j<m;j++)
                {
                    if(a[j][i]>a[p][i])
                    {
                        sum=sum+a[j][i]-a[p][i];
                    }
                }
            }
            System.out.println(""+sum);
            t=t-1;
        }

    }
}