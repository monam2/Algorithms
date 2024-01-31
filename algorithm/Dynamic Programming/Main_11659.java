import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main { //구간 합 구하기 4
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		int[] nums = new int[n+1];
		
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i < n+1; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		
		int[][] pts = new int[m][2];
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			pts[i][0] = Integer.parseInt(st.nextToken());
			pts[i][1] = Integer.parseInt(st.nextToken());
		}
		//로직 시작
		
		//DP로 해야할듯? 점화식은
		//dp[0] = arr[0]
		//dp[n] = dp[n-1] + arr[n]
		//답 : dp[right] - dp[left]
		
		int[] dp = new int[n+1];
		dp[1] = nums[0];
		for (int i = 1; i < dp.length; i++) {
			dp[i] = dp[i-1] + nums[i];
		}
//		System.out.println(Arrays.toString(dp));
		for (int i = 0; i < m; i++) {
			int left = pts[i][0];
			int right = pts[i][1];
			System.out.println(dp[right]-dp[left]);
		}
		
		
		
		//시간초과
//		for (int i = 0; i < m; i++) {
//			int left = pts[i][0];
//			int right = pts[i][1];
//			int total = 0;
//			for (int j = left; j < right+1; j++) {
//				total += nums[j];
//			}
//			System.out.println(total);
//		}
	}
}
