import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class BOJ_1182 { //백준 1182 부분 수열의 합
	private static int n, m, arr[], cnt;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		cnt = 0;
		dfs(0, 0, false);
		System.out.println(cnt);
	}// main

	private static void dfs(int idx, int sum, boolean include) {
		if (idx == n) {
			if (sum == m && include) {
				cnt++;
			}
			return;
		}

		dfs(idx + 1, sum + arr[idx], true);
		dfs(idx + 1, sum, include);
	}// dfs
}// class
