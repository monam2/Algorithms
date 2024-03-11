import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_2096 {	//백준 2096 내려가기
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		int n = Integer.parseInt(br.readLine());
		int[][] maxDp = new int[n][3];
		int[][] minDp = new int[n][3];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			if (i==0) {
				for (int j = 0; j < 3; j++) {
					maxDp[i][j] = Integer.parseInt(st.nextToken());
					minDp[i][j] = maxDp[i][j];
				}
			}
			else {
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				int c = Integer.parseInt(st.nextToken());
				maxDp[i][0] = a + Math.max(maxDp[i-1][0], maxDp[i-1][1]);
				maxDp[i][1] = b + Math.max(Math.max(maxDp[i-1][0], maxDp[i-1][1]), maxDp[i-1][2]);
				maxDp[i][2] = c + Math.max(maxDp[i-1][2], maxDp[i-1][1]);
				
				minDp[i][0] = a + Math.min(minDp[i-1][0], minDp[i-1][1]);
				minDp[i][1] = b + Math.min(Math.min(minDp[i-1][0], minDp[i-1][1]), minDp[i-1][2]);
				minDp[i][2] = c + Math.min(minDp[i-1][2], minDp[i-1][1]);
			}
		}
		int max = 0;
		int min = 1_000_000;
		for (int i = 0; i < 3; i++) {
			max = Math.max(max, maxDp[n-1][i]);
			min = Math.min(min, minDp[n-1][i]);
		}
		System.out.println(max +" " + min);
	}//main
}//class
