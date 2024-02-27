import java.util.Scanner;

public class Main_1463 { //백준 1463 1로 만들기
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int[] dp = new int[n+1];
		
		//1을 만드는 연산은 0회
		for (int i = 2; i < dp.length; i++) {
			//아무것도 안되는 경우를 먼저 고려 -> 이전 값에 연산 1회+
			dp[i] = dp[i-1] + 1;
			if (i%3==0) {
				//이미 있는거(-1한거)와 3으로 나눈거에 연산1회 한걸 비교
				dp[i] = Math.min(dp[i], dp[i/3]+1);
			}
			if (i%2==0) {
				dp[i] = Math.min(dp[i], dp[i/2]+1);
			}
		}
		System.out.println(dp[n]);
	}//main
}//class
