import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_17281 { //백준 17281 야구

	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;

	static int n, players[][], result, order[];
	static boolean isUsed[];


	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());

		players = new int[n+1][10];
		for (int i = 1; i < n+1; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j = 1; j < 10; j++) {
				players[i][j] = Integer.parseInt(st.nextToken());
			}
		}

		//순열로 타자 순서를 뽑아서 저장할 타자 순서 배열 필요

		isUsed = new boolean[10]; //순열 선택 배열
		isUsed[4] = true; //4번타자는 무조건 1번
		order = new int[10]; //타자 순서
		order[4] = 1;

		result = 0;

		//1명은 정해져 있으므로 2번부터 뽑아야 함
		per(2);

		System.out.println(result);
	}//end main

	private static void per(int cnt) {
		if (cnt == 10) {
			//함수 실행
			game();
			return;
		}
		for (int i = 1; i <= 9; i++) {
			if (isUsed[i]) continue;
			
			isUsed[i] = true;
			order[i] = cnt; //뽑은 순서대로 타자 순서 배정
			per(cnt+1);
			isUsed[i] = false;
		}
	}

	private static void game() {
		int score = 0;
		int startPlayer = 1; //이닝 시작 타자
		boolean[] base; //베이스 배열

		for (int i = 1; i < n+1; i++) { //이닝 반복문
			int out = 0;
			base = new boolean[4]; //홈, 1루, 2루, 3루
			outer : while (true) {

				for (int j = startPlayer; j <= 9; j++) {
					int batter = players[i][order[j]]; //타자가 치는 공
					
					if (batter == 0) { //아웃
						out++;
					}
					else if (batter == 1) { //1루타
						//3루에 있는 선수는 홈으로 들어오고, 나머지는 1루씩 전진
						for (int k = 3; k >= 1; k--) {
							if (base[k]) { //k번째 베이스에 선수가 있으면
								if (k==3) { //3루에 선수 있으면 홈으로
									score++;
									base[k] = false;
									continue;
								}
								//1,2루에 선수가 있으면 하나씩 전진
								base[k] = false;
								base[k+1] = true;
							}
						}			
						base[1] = true; //타자는 1루로 전진
					} //end 1루타
					else if (batter == 2) { //2루타
						for (int k = 3; k >= 1; k--) {
							if (base[k]) {
								if (k==3 || k==2) {
									score++;
									base[k] = false;
									continue;
								}
								base[k] = false;
								base[k+2] = true;
							}
						}
						base[2] = true; //타자는 2루로 전진
						continue;
					}//end 2루타
					if (batter == 3) { //3루타
						for (int k = 3; k >= 1; k--) {
							if (base[k]) { //3루타면 1루에 있어도 홈으로 들어올 수 있음
								score++;
								base[k] = false;
							}
						}
						base[3] = true; //타자는 3루로 전진
					}//end 3루타
					else if (batter == 4) { //홈런
						for (int k = 3; k >= 1; k--) { //모든 주자가 다 들어옴
							if (base[k]) {
								base[k] = false;
								score++;
							}
						}

						score++; //타자도 바로 돌아서 들어옴
					}

					if (out==3) { //3아웃이면 다음 이닝부터 다음 타자로 넘기기
						startPlayer = j+1;
						if (startPlayer==10) {
							startPlayer = 1;
						}
						break outer;
					}
				}//선수 로테이션 중

				//아웃이 아닐 경우엔 직접 타자 순서를 1로 바꿔줘야 함
				startPlayer = 1;

			}//while문
		}//이닝

		//게임이 끝나면(모든 이닝 끝) 갱신
		result = Math.max(result, score);
	}//end game

	
}//end class
