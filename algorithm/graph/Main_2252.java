import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main_2252 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;
	static StringBuilder sb = new StringBuilder();
	static ArrayList<Integer> q = new ArrayList<>();
	static int n, m, arr[];
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		arr = new int[n+1];
		
		ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
		for (int i = 0; i < n+1; i++) {
			graph.add(new ArrayList<Integer>());
		}

		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			graph.get(a).add(b);
			arr[b]++;
		}

		ArrayDeque<Integer> q = new ArrayDeque<>();
		for (int i = 1; i < arr.length; i++) {
			if (arr[i]==0) q.offer(i);
		}
		
		while (!q.isEmpty()) {
			int v = q.pollFirst();
			sb.append(v).append(" ");
			
			for (int i = 0; i < graph.get(v).size(); i++) {
				arr[graph.get(v).get(i)]--; //진입 간선 수를 줄이고
				//진입 간선 수가 0이면 큐에 넣어야함
				if (arr[graph.get(v).get(i)]==0) q.offer(graph.get(v).get(i));
			}
		}
		
		System.out.println(sb.toString());
	}//end main
}//end class
