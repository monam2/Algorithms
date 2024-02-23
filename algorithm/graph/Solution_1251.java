import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Solution_1251 { //swea 1251 하나로
	static class Edge implements Comparable<Edge>{
		int from, to;
		double weight;

		public Edge(int from, int to, double weight) {
			super();
			this.from = from;
			this.to = to;
			this.weight = weight;
		}

		@Override
		public int compareTo(Edge o) {
			return (int)(Double.compare(this.weight, o.weight));
		}
	}//end class Edge
	static class Node {
		int x,y,no;

		public Node(int x, int y, int no) {
			super();
			this.x = x;
			this.y = y;
			this.no = no;
		}
	}//end class Node
	//---------------------------------------------------------
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;
	
	static int T, n;
	static int[] xs, ys;
	static int[] parents;
	static double E;
	
	static Node[] nodeList;
	static List<Edge> edgeList;
	//statics
	
	public static void main(String[] args) throws IOException {
		T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			
			n = Integer.parseInt(br.readLine());
			
			xs = new int[n];
			ys = new int[n];
			nodeList = new Node[n];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++) {
				xs[i] = Integer.parseInt(st.nextToken());
			}
			
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < n; i++) {
				ys[i] = Integer.parseInt(st.nextToken());
			}
			
			E = Double.parseDouble(br.readLine());
			for (int i = 0; i < n; i++) {
				nodeList[i] = new Node(xs[i], ys[i], i);
			}
			
			//간선의 정보를 저장하는 함수
			makeEdge();
			
			Collections.sort(edgeList);
			
			makeSet();
			
			int cnt = 0;
			double weight = 0;
			for (Edge edge : edgeList) {
				if (!union(edge.from, edge.to)) continue;
				weight += edge.weight;
				cnt++;
				if (cnt==nodeList.length-1) break;
			}
			
			System.out.println("#" + t + " " + Math.round(weight));
			
		}//end for T
	}//end main
	
	private static boolean union(int a, int b) {
		int rootA = find(a);
		int rootB = find(b);
		
		if (rootA == rootB) return false;
		parents[rootB] = rootA;
		return true;
	}
	
	private static int find(int x) {
		if (parents[x]==x) return x;
		return parents[x] = find(parents[x]);
	}//end find
	
	private static void makeSet() {
		parents = new int[nodeList.length];
		for (int i = 0; i < nodeList.length; i++) {
			parents[i] = i;
		}
	}//end makeSet
	
	private static void makeEdge() {
		edgeList = new ArrayList<>();
		for (int i = 0; i < nodeList.length-1; i++) {
			for (int j = i+1; j < nodeList.length; j++) {
				edgeList.add(
						new Edge(nodeList[i].no,
								nodeList[j].no,
								E*(Math.pow(nodeList[i].x-nodeList[j].x, 2) +
										Math.pow(nodeList[i].y-nodeList[j].y, 2))));
				edgeList.add(
						new Edge(nodeList[j].no,
								nodeList[i].no,
								E*(Math.pow(nodeList[j].x-nodeList[i].x, 2) +
										Math.pow(nodeList[j].y-nodeList[i].y, 2))));
			}
		}
	}//end makeEdge()
}//end class
