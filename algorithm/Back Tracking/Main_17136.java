import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_17136 { //백준 17136 색종이 붙이기

	static int map[][], answer;
	static int[] paper;
	
	public static void main(String[] args) throws IOException {
		init();
		
		dfs(0,0,0);
		
		if (answer == Integer.MAX_VALUE) {
			System.out.println(-1);
		} else {
			System.out.println(answer);
		}
	}//main
	
	private static void dfs(int x, int y, int cnt) {
		if (x >= 9 && y > 9) { //9,10 에 닿으면 종료
			answer = Math.min(answer, cnt);
			return;
		}
		
		if (y > 9) {
			dfs(x+1, 0, cnt);
			return;
		}
		
		if (answer <= cnt) { //가지치기 : 이미 나온 최솟값보다 커지면 더 볼필요 없음
			return;
		}
		
		
		
		if (map[x][y] == 1) {
			for (int i = 5; i >= 1; i--) {
				//종이가 남아있고 1~5 칸까지를 붙일 수 있으면
				if (paper[i] > 0 && checkPaperByN(x,y,i)) {
					//재귀 태우기
					paper[i]--; //종이 쓴거 체크하고
					attach(x,y,i,0);//색종이 붙이고(0으로 만들고)
					dfs(x, y+1, cnt+1);//재귀
					attach(x,y,i,1);//색종이 떼고(다시 1로)
					paper[i]++;//종이 체크 해제하고
				}
			}
		} else {
			 dfs(x, y+1, cnt);
		}
	}//dfs
	
	private static void attach(int x, int y, int n, int k) {
		for (int i = x; i < x+n; i++) {
			for (int j = y; j < y+n; j++) {
				map[i][j] = k;
			}
		}
	}//attach
	
	
	private static boolean checkPaperByN(int x, int y, int k) {
		
		for (int i = x; i < x+k; i++) {
			for (int j = y; j < y+k; j++) {
				if (i < 0 || i >= 10 || j < 0 || j >= 10 || map[i][j] == 0) {
					return false;
				}
			}
		}
		return true;
	}//checkPaperByN
	
	private static void init() throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		map = new int[10][10];
		for (int i = 0; i < 10; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < 10; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		paper = new int[6];
		Arrays.fill(paper, 5);
		answer = Integer.MAX_VALUE;
	}
}//class
