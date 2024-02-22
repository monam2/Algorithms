import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;

public class Solution_1238 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;
	
	static int T = 10;
	static int n, m, a, b;
	static boolean visited[];
	static ArrayList<ArrayList<Integer>> graph;
	static ArrayList<Integer> result = null;
	
	//statics
	
	public static void main(String[] args) throws IOException {
		for (int t = 1; t <= T; t++) {
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			
			graph = new ArrayList<ArrayList<Integer>>();
			for (int i = 0; i <= 100; i++) {
				graph.add(new ArrayList<Integer>());
			}
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n/2; i++) {
				a = Integer.parseInt(st.nextToken());
				b = Integer.parseInt(st.nextToken());
				graph.get(a).add(b);
			}
			visited = new boolean[graph.size()];
			
			System.out.println("#" + t + " " + bfs(m));
		}//end for T
	}//end main
	
	private static int bfs(int v) {
		int lv = 0;
		int beforeLV = 0;
		ArrayDeque<int[]> q = new ArrayDeque<int[]>();
		q.offer(new int[] {v, lv});
		visited[v] = true;
		result = new ArrayList<Integer>();
		
		
		while (!q.isEmpty()) {
			v = q.peek()[0];
			lv = q.peek()[1];
			q.poll();
			
			if (lv > beforeLV) {
				result = new ArrayList<Integer>();
				result.add(v);
				beforeLV = lv;
			} else if (lv == beforeLV) {
				result.add(v);
			}
			
			for (Integer i : graph.get(v)) {
				if(visited[i]) continue;
				
				q.offer(new int[] {i, lv+1});
				visited[i] = true;
			}
		}
		
		return Collections.max(result);
	}//end bfs
}//end class
