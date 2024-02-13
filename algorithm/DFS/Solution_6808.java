import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_6808 {
	static int gyu[], gyuYeong[], canYeong[], gWin, gDefeat;
	static boolean isUsed[];
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;
	public static void main(String[] args) throws IOException {
		
		int T = Integer.parseInt(br.readLine());
		for (int t = 1; t <= T; t++) {

			gWin = 0; //static 변수 초기화
			gDefeat = 0;

			//카드번호와 인덱스를 맞추기 위함
			//0번째 칸은 -1로 막아두기
			gyu = new int[19];
			gyu[0] = -1;
			isUsed = new boolean[19];
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 9; i++) {
				gyu[Integer.parseInt(st.nextToken())] = 1;
			}
			gyuYeong = new int[9];
			canYeong = new int[9];
			int gIdx = 0;
			int yIdx = 0;
			for (int i = 1; i < gyu.length; i++) {
				if (gyu[i]==1) {
					gyuYeong[gIdx++] = i;
				} else if (gyu[i] == 0) {
					canYeong[yIdx++] = i; //인영이가 가질 수 있는 숫자들
				}
			}
			dfs(0, new int[9]);
			System.out.println("#" + t + " " + gWin + " " + gDefeat);
		}//end TC
	}//end main

	private static void dfs(int cnt, int[] arr) {
		if (cnt==9) {
			//arr(인영이 카드)로 규영이 카드와 비교하기
			compare(arr);
			return;
		}

		for (int i = 0; i < canYeong.length; i++) {
			if (isUsed[canYeong[i]]) continue; //이미 사용한 카드는 패스
			isUsed[canYeong[i]] = true;
			arr[cnt] = canYeong[i];
			dfs(cnt+1, arr);
			isUsed[canYeong[i]] = false;
		}
	}//end dfs

	private static void compare(int[] inYoung) {
		//규영이 카드를 따로 정리
		//arr: 인영이 카드
		int gScore=0;
		int yScore=0;
		
		for (int i = 0; i < inYoung.length; i++) {
			if (gyuYeong[i]>inYoung[i]) { //더 높은 사람이->점수 다가져감
				gScore += gyuYeong[i]+inYoung[i];
			}
			else if (gyuYeong[i]<inYoung[i]) {//규영이 질때
				yScore += gyuYeong[i]+inYoung[i];
			}
		}
		if (gScore > yScore) gWin++;
		else gDefeat++;
	}//end compare
}//end class
