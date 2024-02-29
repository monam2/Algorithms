import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_10971 { //백준 10971 외판원 순회2
	static int n, map[][], min;
	static boolean visited[];

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		n = Integer.parseInt(br.readLine());

		map = new int[n][n];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < n; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		min = Integer.MAX_VALUE;
		visited = new boolean[n];
		dfs(0,new int[n]);
		System.out.println(min);
	}//main

	private static void dfs(int idx, int[] arr) {
		if (idx==n) {
			int sum = 0;
			for (int i = 1; i < n; i++) {
				if (map[arr[i-1]][arr[i]]==0) return;
				sum += map[arr[i-1]][arr[i]];
			}
			if (map[arr[n-1]][arr[0]]==0) return;
			sum += map[arr[n-1]][arr[0]];

			min = Math.min(min, sum);
			return;
		}
		for (int i = 0; i < n; i++) {
			if (visited[i]) continue;
			visited[i] = true;
			arr[idx] = i;
			dfs(idx+1, arr);
			visited[i] = false;
		}
	}//dfs
}//class
