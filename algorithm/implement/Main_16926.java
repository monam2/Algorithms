import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
	static int n,m,r;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		StringBuilder sb = new StringBuilder();		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		int[][] map = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		int count = Math.min(n, m)/2; // 더 작은거/2 번 해야함 (바깥쪽, 안쪽, 더 안쪽...)
		
		for (int k = 0; k < r; k++) { //전체 돌리는 횟수 r
			for (int i = 0; i < count; i++) { //속으로 들어가는 횟수
				
				//왼쪽 윗줄 값 임시 보관
				int temp = map[i][i];
				
				//윗줄을 왼쪽으로 밀기
				for (int j = i; j < m-i-1; j++) {
					map[i][j] = map[i][j+1];
				}
				
				//오른쪽 줄 위로 밀기
				for (int j = i; j < n-i-1; j++) {
					map[j][m-1-i] = map[j+1][m-1-i];
				}
				
				//아랫쪽줄 오른쪽으로 밀기
				for (int j = m-i-1; j >= i+1 ; j--) {
					map[n-i-1][j] = map[n-i-1][j-1];
				}
				
				//왼쪽줄을 아래로 밀기
				for (int j = n-i-1; j >= i+2; j--) {
					map[j][i] = map[j-1][i];
				}
				
				map[i+1][i] = temp;
			}
		}
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				sb.append(map[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb.toString());
	}//end main
}//end class
