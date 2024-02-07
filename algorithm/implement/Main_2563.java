import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main_2563_강창우 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		int[][] white = new int[101][101];  //100*100 이차원 배열
		int n = Integer.parseInt(br.readLine());
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			int x = Integer.parseInt(st.nextToken());
			int y = Integer.parseInt(st.nextToken());

			for (int q = x; q < x+10; q++) { //색종이가 있는 칸은 1로 바꿈
				for (int w = y; w < y+10; w++) {
					white[q][w]=1;
				}
			}
		}
		int count = 0;
		for (int i = 1; i < white.length; i++) { //색종이가 있는 부분 갯수 세기 -> 겹쳐도 상관x
			for (int j = 1; j < white.length; j++) {
				if (white[i][j]>=1) count++;
			}
		}
		System.out.println(count);
	}//end main
}//end class
