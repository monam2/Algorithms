import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main_5972 { //백준 5972 택배 배송
	
	private static class Node implements Comparable<Node>{
		int end, cost;

		public Node(int end, int cost) {
			super();
			this.end = end;
			this.cost = cost;
		}

		@Override
		public int compareTo(Node o) {
			// TODO Auto-generated method stub
			return Integer.compare(this.cost, o.cost);
		}
	}
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	static int n,m,min;
	static ArrayList<ArrayList<Node>> graph;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		graph = new ArrayList<>();
		for (int i = 0; i < n+1; i++) {
			graph.add(new ArrayList<Node>());
		}
		
		for (int i = 0; i < m; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			graph.get(a).add(new Node(b, c));
			graph.get(b).add(new Node(a, c));
		}
		
		min = Integer.MAX_VALUE;
		
		System.out.println(dijkstra()[n]);
	}//end
	
	private static int[] dijkstra() {
		int[] d = new int[n+1];
		for (int i = 0; i < n+1; i++) {
			d[i] = Integer.MAX_VALUE;
		}
		d[1] = 0;
		
		PriorityQueue<Node> pq = new PriorityQueue<Node>();
		pq.offer(new Node(1, 0));
		
		while(!pq.isEmpty()) {
			int curV = pq.peek().end;
			int cost_StartToCur = pq.poll().cost;
			
			//이미 더 최소비용인 경로가 있으면
			if (d[curV] < cost_StartToCur) continue; 
			
			for (int i = 0; i < graph.get(curV).size(); i++) {
				int nextV = graph.get(curV).get(i).end;
				int cost_StartToNext = cost_StartToCur + graph.get(curV).get(i).cost;
				
				if (d[nextV] > cost_StartToNext) {
					d[nextV] = cost_StartToNext;
					pq.offer(new Node(nextV, cost_StartToNext));
				}
			}
		}
		return d;
	}//dijkstra
}//class
