import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_1010 { // 백준 1010 다리 놓기
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			st = new StringTokenizer(br.readLine());
			int m = Integer.parseInt(st.nextToken());
			int n = Integer.parseInt(st.nextToken());
			
			int[][] dp = new int[n+1][m+1];
			for (int i = 0; i <= n; i++) {
				for (int j = 0, end=Math.min(i, m); j <= end; j++) {
					if (j==0 || j==i) dp[i][j] = 1;
					else dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
				}
			}
			System.out.println(dp[n][m]);
		}
	}
}
