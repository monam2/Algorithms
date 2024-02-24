import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_1018 { //백준 1018 체스판 다시 칠하기
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;
	static int n, m;
	static char[][] map;
	static char[][] case1 = {
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'}
	};
	static char[][] case2 = {
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'},
			{'W','B','W','B','W','B','W','B'},
			{'B','W','B','W','B','W','B','W'}
	};
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		
		map = new char[n][m];
		for (int i = 0; i < n; i++) {
			String input = br.readLine();
			for (int j = 0; j < m; j++) {
				map[i][j] = input.charAt(j);
			}
		}
		
		
		int min = Integer.MAX_VALUE;
		for (int i = 0; i < n-7; i++) {
			for (int j = 0; j < m-7; j++) {
				int case1Cnt = 0;
				int case2Cnt = 0;
				
				for (int k = 0; k < 8; k++) {
					for (int l = 0; l < 8; l++) {
						if (case1[k][l] != map[k+i][l+j]) case1Cnt++;
						if (case2[k][l] != map[k+i][l+j]) case2Cnt++;
					}
				}
				int result = Math.min(case1Cnt, case2Cnt);
				min = Math.min(min, result);
			}
		}
		
		
		System.out.println(min);
		
		
	}//end main
}//end class
