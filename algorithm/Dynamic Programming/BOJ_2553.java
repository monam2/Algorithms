import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2553 {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		int[] dp = new int[20001];
		
		dp[0] = 1;
		dp[1] = 1;
		dp[2] = 2;
		dp[3] = 6;
		dp[4] = 4;
		
		for (int i = 5; i < n+1; i++) {
			if (i % 5 == 0) {
				int value = i / 5;
				dp[i] = ((int) Math.pow(2,  value%4)*dp[value])% 10;
			}
			else {
				int before = (i/5)*5;
				int total = 1;
				
				for (int j = i; j > before; j--) {
					total *= (j % 10);
				}
				total *= dp[before];
				dp[i] = total % 10;
			}
		}
		System.out.println(dp[n]);
	}//main
}//class
