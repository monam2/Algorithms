import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main_16935 {
		static int n, m, r;
		static int[][] map;
	
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		StringBuilder sb = new StringBuilder();
		
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		r = Integer.parseInt(st.nextToken());
		
		map = new int[n][m];
		for (int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		int[] commands = new int[r];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < commands.length; i++) {
			commands[i] = Integer.parseInt(st.nextToken());
		}
		
		for (int i : commands) {
			if (i==1) first();
			if (i==2) second();
			if (i==3) third();
			if (i==4) fourth();
			if (i==5) fifth();
			if (i==6) sixth();
		}		
//		fourth();
		
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				sb.append(map[i][j]).append(" ");
			}
			sb.append("\n");
		}
		System.out.println(sb.toString());

	}//end main
	
	
	private static void first() { //완료
		int[][] newMap = new int[map.length][map[0].length];
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				newMap[i][j] = map[map.length-1-i][j];
			}
		}
		map = newMap;
	}
	
	private static void second() {//완료
		int[][] newMap = new int[map.length][map[0].length];
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				newMap[i][j] = map[i][map[0].length-1-j];
			}
		}
		map = newMap;
	}
	//0,7 -> 7,5가 됨 
	private static void third() {//완료
		int[][] newMap = new int[map[0].length][map.length];
		for (int i = 0; i < map[0].length; i++) {
			for (int j = 0; j < map.length; j++) {
				newMap[i][j] = map[map.length-j-1][i];
			}
		}
		map = newMap;
	}
	private static void fourth() {//완료
		int[][] newMap = new int[map[0].length][map.length];
		for (int i = 0; i < map[0].length; i++) {
			for (int j = 0; j < map.length; j++) {
				newMap[i][j] = map[j][map[0].length-i-1];
			}
		}
		map = newMap;
	}
	private static void fifth() {
		int miniMap1[][] = new int[map.length/2][map[0].length/2];
		int miniMap2[][] = new int[map.length/2][map[0].length/2];
		int miniMap3[][] = new int[map.length/2][map[0].length/2];
		int miniMap4[][] = new int[map.length/2][map[0].length/2];
		
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				if (i<map.length/2 && j<map[0].length/2) { //1사분면 -> 맵1
					miniMap1[i][j] = map[i][j];
				}
				else if (i<map.length/2 && j>=map[0].length/2) { //2사분면 -> 맵2
					miniMap2[i][j-map[0].length/2] = map[i][j];
				}
				else if (i>=map.length/2 && j>=map[0].length/2) { //3사분면 -> 맵3
					miniMap3[i-map.length/2][j-map[0].length/2] = map[i][j];
				}
				else if (i>=map.length/2 && j<map[0].length/2) {
					miniMap4[i-map.length/2][j] = map[i][j];
				}
			}
		}
		
		int[][] newMap = new int[map.length][map[0].length];
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				if (i<map.length/2 && j<map[0].length/2) { //1사분면 -> 맵4
					newMap[i][j] = miniMap4[i][j];
				}
				else if (i<map.length/2 && j>=map[0].length/2) { //2사분면 -> 맵 1
					newMap[i][j] = miniMap1[i][j-map[0].length/2];			
				}
				else if (i>=map.length/2 && j>=map[0].length/2) { //3사분면 -> 맵2
					newMap[i][j] = miniMap2[i-map.length/2][j-map[0].length/2];
				}
				else if (i>=map.length/2 && j<map[0].length/2) { //4사분면 -> 맵3
					newMap[i][j] = miniMap3[i-map.length/2][j];
				}
			}
		}
		map = newMap;
	}
	private static void sixth() {
		int miniMap1[][] = new int[map.length/2][map[0].length/2];
		int miniMap2[][] = new int[map.length/2][map[0].length/2];
		int miniMap3[][] = new int[map.length/2][map[0].length/2];
		int miniMap4[][] = new int[map.length/2][map[0].length/2];
		
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				if (i<map.length/2 && j<map[0].length/2) { //1사분면 -> 맵1
					miniMap1[i][j] = map[i][j];
				}
				else if (i<map.length/2 && j>=map[0].length/2) { //2사분면 -> 맵2
					miniMap2[i][j-map[0].length/2] = map[i][j];
				}
				else if (i>=map.length/2 && j>=map[0].length/2) { //3사분면 -> 맵3
					miniMap3[i-map.length/2][j-map[0].length/2] = map[i][j];
				}
				else if (i>=map.length/2 && j<map[0].length/2) { //4사분면 -> 맵4
					miniMap4[i-map.length/2][j] = map[i][j];
				}
			}
		}
		
		int[][] newMap = new int[map.length][map[0].length];
		for (int i = 0; i < map.length; i++) {
			for (int j = 0; j < map[0].length; j++) {
				if (i<map.length/2 && j<map[0].length/2) { //1사분면 -> 맵2
					newMap[i][j] = miniMap2[i][j];
				}
				else if (i<map.length/2 && j>=map[0].length/2) { //2사분면 -> 맵3
					newMap[i][j] = miniMap3[i][j-map[0].length/2];			
				}
				else if (i>=map.length/2 && j>=map[0].length/2) { //3사분면 -> 맵4
					newMap[i][j] = miniMap4[i-map.length/2][j-map[0].length/2];
				}
				else if (i>=map.length/2 && j<map[0].length/2) { //4사분면 -> 맵1
					newMap[i][j] = miniMap1[i-map.length/2][j];
				}
			}
		}
		map = newMap;
	}
}//end class
