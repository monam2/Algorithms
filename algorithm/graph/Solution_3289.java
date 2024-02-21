import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Solution_3289 {
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;
	static StringBuilder sb = null;;
	static int T,n,m,graph[];
	public static void main(String[] args) throws IOException {
		T = Integer.parseInt(br.readLine());
		
		for (int t = 0; t < T; t++) {
			sb = new StringBuilder();
			sb.append("#").append(t+1).append(" ");
			st = new StringTokenizer(br.readLine());
			n = Integer.parseInt(st.nextToken());
			m = Integer.parseInt(st.nextToken());
			graph = new int[n+1];
			for (int i = 1; i < n+1; i++) {
				graph[i] = i;
			}
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int command = Integer.parseInt(st.nextToken());
				int a = Integer.parseInt(st.nextToken());
				int b = Integer.parseInt(st.nextToken());
				
				if (command==0) { //0일 때
					//두 노드가 이미 같은 합집합인지 확인해야함
					if (findSet(a)!=findSet(b)) {
						graph[findSet(b)] = findSet(a);
					}
				} else { //1일 때
					//합집합인지 확인
					if (findSet(a)==findSet(b)) sb.append(1);
					else sb.append(0);
				}
			}
			System.out.println(sb);
		}//end for T
	}//end main
	
	//합집합인지(서로소x)인지 확인
	private static int findSet(int x) {
		if (x==graph[x]) return x;
		else return graph[x] = findSet(graph[x]);
	}
}//end class
