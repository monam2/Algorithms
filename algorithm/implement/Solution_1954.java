import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Iterator;
import java.util.Scanner;

public class Solution_1954 {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int n = Integer.parseInt(br.readLine());
			int[][] graph = new int[n][n];

			int[] temp = {0,0};
			ArrayDeque<int[]> q = new ArrayDeque<int[]>();
			q.offer(temp);
			int[] dx = {-1,0,1,0};
			int[] dy = {0,1,0,-1};
			
			graph[0][0] = 1;
			int d = 1;
			while (q.size()>0) {
				
				int[] tem = q.poll();
				int x = tem[0];
				int y = tem[1];

				int nx = x + dx[d];
				int ny = y + dy[d];
				
				// 1. 범위 안에 있고 앞으로 갈 수 있는 경우
				// 2. 범위 안에 있으나, 앞이 막혀서 못가는 경우
				// 3. x,y 둘 중 하나가 범위를 벗어나는 경우
				
				if (0<=nx&&nx<n && 0<=ny&&ny<n && graph[nx][ny]==0) {
					graph[nx][ny] = graph[x][y]+1;
					int[] temp2 = {nx,ny};
					q.offer(temp2);
				} else if (0<=nx&&nx<n && 0<=ny&&ny<n && graph[nx][ny]!=0) {
					//모든 칸이 다 찼으면 종료. 아니면 방향 전환
					boolean isZero = false;
					for (int i = 0; i < graph.length; i++) {
						for (int j = 0; j < graph.length; j++) {
							if (graph[i][j]==0) {
								isZero = true;
								break;
							}
						}
						if (isZero) break;
					}
					//방향 전환
					if (isZero) {
						d = (d+1)%4;
						nx = x + dx[d];
						ny = y + dy[d];
						graph[nx][ny] = graph[x][y] + 1;
						int[] temp2 = {nx, ny};
						q.offer(temp2);
					} else break; //0이 없으면 종료		
					
				} else if (0>nx || nx>=n || 0>ny || ny>=n) {
					// 범위를 벗어나는 경우 -> 방향전환
					d = (d+1)%4;
					nx = x + dx[d];
					ny = y + dy[d];
					if (0<=nx&&nx<n && 0<=ny&&ny<n) {
						if (graph[nx][ny] != 0) break;
					//방향전환 했는데 이미 차있는 칸이라면
					graph[nx][ny] = graph[x][y]+1;
					int[] temp2 = {nx, ny};
					q.offer(temp2);
					}
					
				}
			} //end while
			System.out.println("#" +t );
			for (int i = 0; i < graph.length; i++) {
				for (int j = 0; j < graph.length; j++) {
					System.out.print(graph[i][j] + " ");
				}
				System.out.println();
			}
		} //end for -> t
		br.close();
	}// end main
}// end class
