import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Solution_1861 {
	public static void main(String[] args) throws IOException {
		/*
		 * 이동 조건
		 * 1. 범위 내
		 * 2. 현재 값보다 1 클것
		 * 3. 방문하지 않은 곳
		 */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {
			int n = Integer.parseInt(br.readLine());
			int[][] map = new int[n][n];
			for (int i = 0; i < n; i++) {
				st = new StringTokenizer(br.readLine());
				for (int j = 0; j < n; j++) {
					map[i][j] = Integer.parseInt(st.nextToken());
				}
			}
			
			int maxRoomCnt = 0;
			int nowRoom = n*n;

			int[] dx = {-1,0,1,0};
			int[] dy = {0,1,0,-1};

			for (int i = 0; i < map.length; i++) {
				for (int j = 0; j < map.length; j++) {
					boolean[][] visited = new boolean[n][n];
					visited[i][j] = true; //시작점 방문처리
					ArrayDeque<int[]> q = new ArrayDeque<>();
					q.offer(new int[] {i,j,1}); //x,y,탐색한 방갯수

					while (!q.isEmpty()) {
						int[] temp = q.pollFirst();
						int x = temp[0];
						int y = temp[1];
						int roomCnt = temp[2];
						
						if (roomCnt > maxRoomCnt) {
							maxRoomCnt = roomCnt;
							nowRoom = map[i][j];
						} else if (roomCnt == maxRoomCnt) {
							nowRoom = Math.min(nowRoom, map[i][j]);
						}
						
						for (int k = 0; k < 4; k++) {
							int nx = x + dx[k];
							int ny = y + dy[k];
							//범위내 & 미방문 & 현재 방보다 1 큰 방이면
							if (0<=nx&&nx<n && 0<=ny&&ny<n && !visited[nx][ny] && map[nx][ny]==map[x][y]+1) {
								visited[nx][ny] = true;
								q.offer(new int[] {nx,ny,roomCnt+1});
							}
						}
					}//end while
				}
			}//end bf
			
			System.out.println("#" + t + " " + nowRoom + " " + maxRoomCnt);

		}//end tc
	}//end main
}//end class
