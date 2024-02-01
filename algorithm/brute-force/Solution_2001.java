import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Solution_2001 {
	
	public static void main(String[] args) throws Exception, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());
			
			int[][] graph = new int[n][n];
			for (int i = 0; i < graph.length; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < graph.length; j++) {
					graph[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			int max = 0;
			for (int i = 0; i < graph.length-m+1; i++) {
				for (int j = 0; j < graph.length-m+1; j++) {
					int total = 0;
					for (int k = i; k < m+i; k++) {
						for (int l = j; l < m+j; l++) {
							total += graph[k][l];
							
						}
					}
					max = Math.max(max, total);
				}
			}
			System.out.println("#" + t + " " + max);
			
			
		}// end for
	}//end main
}//end class
