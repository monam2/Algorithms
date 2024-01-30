package bruteforce;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Solution_1208 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		for (int i = 0; i < 10; i++) {
			st = new StringTokenizer(br.readLine());
			int dump = Integer.parseInt(st.nextToken());
			int[] nums = new int[100];
			st = new StringTokenizer(br.readLine());
			for (int j = 0; j < nums.length; j++) {
				nums[j] = Integer.parseInt(st.nextToken());
			}
			//로직 시작
			/*
			 * while문을 통해서 -> 조건 : dump가 0보다 클때
			 * 최댓값과 최솟값을 각각 구함.
			 * 최댓값은 -1, 최솟값은 +1을 해줌
			 */
			
			while (dump > 0) {
				int max=0;
				int maxIdx = 0;
				int min=101;
				int minIdx = 0;
				
				for (int j = 0; j < nums.length; j++) {
					if (nums[j]>max) {
						max = nums[j];
						maxIdx = j;
					}
					if (nums[j]<min) {
						min = nums[j];
						minIdx = j;
					}
				}
				
				nums[maxIdx]--;
				nums[minIdx]++;
				dump--;
			}
			
			int maxRes = 0;
			int minRes = 101;
			for (int j : nums) {
				maxRes = Math.max(maxRes, j);
				minRes = Math.min(minRes, j);
			}
			System.out.println("#"+(i+1) + " " + (maxRes-minRes));

		}
	}
}
