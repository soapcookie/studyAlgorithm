package week_1;
import java.util.*;
import java.io.*;
public class boj_11720 {
    public static void main(String[] args) throws IOException {
//        Scanner sc = new Scanner(System.in);
//
//        int n = sc.nextInt();
//        int sum=0;
//        String str = sc.next();
//
//        for(int i =0; i<n; i++){
//            sum+=str.charAt(i)-'0';
//            //sum+=str.charAt(i)-48;
//        }

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int sum=0;
        String[] str = br.readLine().split("");
        br.close();

        for(int i=0;i<n;i++){
            sum+=Integer.parseInt(str[i]);
        }

        System.out.println(sum);


    }
}

