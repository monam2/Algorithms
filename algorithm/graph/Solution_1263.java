import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_1263 { //SWEA 1263 사람 네트워크2
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t < T+1; t++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int[][] graph = new int[n+1][n+1];
			for (int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
					if (graph[i][j]==0 && i!=j) {
						graph[i][j] = 999999;
					}
				}
			}
			
			for (int k = 1; k < n+1; k++) {
				for (int a = 1; a < n+1; a++) {
					if (a==k) continue;
					for (int b = 1; b < n+1; b++) {
						if (a==b || k==b) continue;
						graph[a][b] = Math.min(graph[a][b], graph[a][k] + graph[k][b]);
					}
				}
			}
			
			int result = Integer.MAX_VALUE;
			for (int i = 1; i < n+1; i++) {
				int total = 0;
				for (int j = 1; j < n+1; j++) {
					total += graph[i][j];
				}
				result = Math.min(result, total);
			}
			
			System.out.println("#"+t+" " +result);
			
			
		}//for T
	}//main
}//class
