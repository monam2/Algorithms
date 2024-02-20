import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class sdaf {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;
	
	static int n, left, right, value, values[], arr[];
	public static void main(String[] args) throws NumberFormatException, IOException {
		/*
		 * 특성값(합이)이 0에 가까운 용액
		 * 용액은 정렬된 순서로 주어짐
		 * 입력이 10만 -> n^2은 안됨
		 * 이분탐색 : logN / 투포인터 : N
		 * 
		 * 포인터 이동 조건
		 * left + right가
		 * 1. 0보다 크다 -> right--
		 * 2. 0보다 작다 -> left++
		 * 3. 0과 같다 -> 갱신하고 right --
		 * 
		 * 특성값 갱신 조건
		 * - 특성값 변수와 특성값을 이루는 두 값을 담을 정수 배열
		 */
		
		n = Integer.parseInt(br.readLine());
		arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		//투 포인터 선언
		left = 0;
		right = n-1;
		
		value = Integer.MAX_VALUE;
		values = new int[2];
		
		while (left<right) {
			int sum = arr[left] + arr[right];
			
			//갱신 먼저
			
			//현재 베스트 특성값보다 더 작은 값이라면 갱신
			if (value >= Math.abs(sum)) {
				value = Math.abs(sum);
				values[0] = arr[left];
				values[1] = arr[right];
			}
			
			//포인터 이동
			if (sum >= 0) {
				right--;
			} else if (sum < 0 ) {
				left++;
			}
		}
		
		System.out.println(values[0] + " " + values[1]);
	}
}
