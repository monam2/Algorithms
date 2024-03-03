import java.util.*;

public class Main_2506 {
    public static void main(String args[]) {
        Scanner s=new Scanner(System.in);
        int n=s.nextInt();
        int sum=0;
        int count=0;
        for(int i=0;i<n;i++){
            int a=s.nextInt();
            if(a==1){
                count++;
                sum+=count;
            }
            else count=0;
        }
        System.out.print(sum);
    }
}
