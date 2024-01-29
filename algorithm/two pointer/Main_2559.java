import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main_2559 {

	public static void main(String[] args) throws IOException {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());

		int[] arr = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		//		System.out.println(Arrays.toString(arr));

		//로직 시작
		if (m==1) {
			int max=Integer.MIN_VALUE;
			for (int i : arr) {
				max = Math.max(max, i);
			}
			System.out.println(max);
		} else {

			ArrayList<Integer> result = new ArrayList<Integer>();

			int left = 0;
			int right = m-1;
			while (right < arr.length) {
				int sum = 0;
				for (int i = left; i < right+1; i++) {
					sum+=arr[i];
				}
				result.add(sum);

				left++;
				right++;
			}
			int max = Integer.MIN_VALUE;
			for (Integer num : result) {
				max=Math.max(max, num);
			}
			System.out.println(max);
		}
	}
}
