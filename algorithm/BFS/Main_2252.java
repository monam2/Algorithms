import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class Main_2252 {

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;
	static int n,m,map[][], time, removed;
	static boolean[][] visited;
	static int[] dx = {-1,0,1,0};
	static int[] dy = {0,1,0,-1};
	static Set<int[]> willRemove = null;
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		map = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		time = 1;
		
		while (true) {
			willRemove = new HashSet<>();
			visited = new boolean[n][m];
			//map 탐색해서 지울 위치 파악 -> set에 저장
			bfs(0,0);
			
			//set의 좌표들을 지우기(0으로)
			removed = 0;
			remove();
			
			//map에 1이 남아있는지 파악하기 -> 1이 없으면 종료
 
			if (!one()) { //1이 안남아 있으면 종료
				break;
			}

			time++;
			
			// -> 이때, 종료 후 set의 갯수를 셀 거임
		}
		System.out.println(time);
		System.out.println(removed);
	}//end main
	
	//map에 1이 남아있는지 파악하는 함수
	private static boolean one() {
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (map[i][j]==1) { //1이 있으면 종료
					return true;
				}
			}
		}
		return false; //1이 없으면 false 리턴
	}
	
	//remove : set 속의 좌표들을 지우는 함수
	private static void remove() {
		for (int[] arr : willRemove) {
			map[arr[0]][arr[1]] = 0;
			removed++;
		}
	}
	
	//BFS를 수행해서 nxny가 1이면 set에 추가하는 함수
	private static void bfs(int x, int y) {
		ArrayDeque<int[]> q = new ArrayDeque<>();
		visited[x][y] = true;
		q.add(new int[] {x,y});
		
		while (!q.isEmpty()) {
			int[] temp = q.pollFirst();
			x = temp[0];
			y = temp[1];
			
			for (int d = 0; d < 4; d++) {
				int nx = x + dx[d];
				int ny = y + dy[d];
				if (0<=nx&&nx<n && 0<=ny&&ny<m) {
					//다음칸이 0이라면 큐에 넣기
					if (map[nx][ny]==0 && !visited[nx][ny]) {
						visited[nx][ny] = true;
						q.add(new int[] {nx, ny});
					}
					
					//다음칸이 1이라면 set에 넣기
					if (map[nx][ny]==1 && !visited[nx][ny]) {
						visited[nx][ny] = true;
						willRemove.add(new int[] {nx, ny});
					}
				}
			}
		}
	}//end bfs
	
}//end class
