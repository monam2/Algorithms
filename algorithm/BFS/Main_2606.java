import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_2606 { //백준 2606 바이러스

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int n, m;
	static ArrayList<ArrayList<Integer>> graph;
	static boolean[] visited;
	static ArrayDeque<Integer> q;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		m = Integer.parseInt(br.readLine());
		
		graph = new ArrayList<ArrayList<Integer>>();
		
		for (int i = 0; i <= n; i++) {
			graph.add(new ArrayList<Integer>());
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			graph.get(a).add(b);
			graph.get(b).add(a);
		}
		
		visited = new boolean[n+1];
		visited[1] = true;
		System.out.println(bfs(1));
		
	}//end main
	
	private static int bfs(int v) {
		q = new ArrayDeque<>();
		q.offer(v);
		
		int cnt = 0;
		
		while (!q.isEmpty()) {
			v = q.poll();
			
			for (int i = 0; i < graph.get(v).size(); i++) {
				int temp = graph.get(v).get(i);
				
				if (!visited[temp]) {
					cnt++;
					visited[temp] = true;
					q.offer(temp);
				}
			}
		}
		
		return cnt;
	}
}//end class
