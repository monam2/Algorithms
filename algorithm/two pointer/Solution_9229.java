import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;
 
public class Solution_9229 {
    public static void main(String[] args) throws IOException {
         
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
         
        int T = Integer.parseInt(br.readLine());
        for (int t = 1; t <= T; t++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
             
            ArrayList<Integer> arr = new ArrayList<>();
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                arr.add(Integer.parseInt(st.nextToken()));
            }
             
            Collections.sort(arr);
             
            int left = 0;
            int right = n-1;
            ArrayList<Integer> result = new ArrayList<>();
            while (left<right) {
                int sum = arr.get(left) + arr.get(right);
                if (sum<=m) {
                    result.add(sum);
                    left++;
                } else {
                    right--;
                }
            }
            int max = 0;
            for (Integer integer : result) {
                max = Math.max(max,  integer);
            }
            if (max==0) System.out.println("#"+t+ " " + -1);
            else System.out.println("#"+t+ " " + max);
        }
    }//end main
}// end class
