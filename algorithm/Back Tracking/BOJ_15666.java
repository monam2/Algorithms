import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ_15666 { //백준 15666 N과 M 12
	static int n, m, nums[], arr[];
	static Set<int[]> set;

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());

		nums = new int[n];
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			nums[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(nums);
		arr = new int[m];
		set = new HashSet<>();
		dfs(0, 0);
	}//main

	private static void dfs(int idx, int start) {
		if (idx == m) {
			for (int i : arr) {
				System.out.print(i + " ");
			}
			System.out.println();
			return;
		}

		int before = -1;
		for (int i = start; i < n; i++) {
			if (before == nums[i]) continue;
			before = nums[i];
			arr[idx] = nums[i];
			dfs(idx+1, i);
		}
	}//dfs
}//class
