import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_1389 { // BOJ 1389 케빈 베이컨의 6단계 법칙
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		int[][] graph = new int[n + 1][n + 1];
		for (int i = 1; i < n + 1; i++) {
			Arrays.fill(graph[i], Integer.MAX_VALUE / 2);
			graph[i][i] = 0;
		}

		for (int i = 1; i < m + 1; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			graph[a][b] = 1;
			graph[b][a] = 1;
		}

		for (int mid = 1; mid < n + 1; mid++) {
			for (int start = 1; start < n + 1; start++) {
				for (int end = 1; end < n + 1; end++) {
					if (graph[start][end] > graph[start][mid] + graph[mid][end] && start != end) {
						graph[start][end] = graph[start][mid] + graph[mid][end];
					}
				}
			}
		}
		
		int kevinBacon = Integer.MAX_VALUE;
		int result = 0;
		for (int i = 1; i < n+1; i++) {
			int kevinN = 0;
			for (int j = 1; j < n+1; j++) {
				kevinN += graph[i][j];
			}
			
			if (kevinN < kevinBacon) {
				kevinBacon = kevinN;
				result = i;
			}
		}
		
		System.out.println(result);
	}// main
}// class
