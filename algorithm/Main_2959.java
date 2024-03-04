import java.util.Arrays;
import java.util.Scanner;

public class Main_2959 { //백준 2959 거북이
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int arr[] = new int[4];
        for(int i=0; i<4; i++){
            arr[i] = sc.nextInt();
        }
        Arrays.sort(arr);
        
        int width = arr[3] - arr[3] + arr[2];
        int height = arr[1] - arr[1] + arr[0];
        
        System.out.println(width * height);
    }
}
