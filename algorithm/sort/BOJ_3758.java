import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class BOJ_3758 { // 백준 3758 KCPC

	static class Team implements Comparable<Team>{
		int id;
		int[] scoreList;
		int submit;
		int lastSubmit;
		int total;
		@Override
		public int compareTo(Team o) {
			if (this.total == o.total) {
				if (this.submit == o.submit) {
					return this.lastSubmit - o.lastSubmit;
				}
				return this.submit - o.submit;
			}
			return o.total - this.total;
		}

	}

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());

		for (int t = 0; t < T; t++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int n = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			int m = Integer.parseInt(st.nextToken());

			Team[] list = new Team[n];
			for (int i = 0; i < m; i++) {
				st = new StringTokenizer(br.readLine());
				int teamID = Integer.parseInt(st.nextToken());
				int problemNum = Integer.parseInt(st.nextToken());
				int score = Integer.parseInt(st.nextToken());

				if (list[teamID - 1] == null) {
					list[teamID - 1] = new Team();
					list[teamID - 1].id = teamID;
					list[teamID - 1].scoreList = new int[k + 1];
				}

				list[teamID - 1].scoreList[problemNum] = Math.max(score, list[teamID - 1].scoreList[problemNum]);
				list[teamID - 1].submit++;
				list[teamID - 1].lastSubmit = i;

			}
			for (int i = 0; i < n; i++) {
				int sum = 0;
				for (int j = 1; j <= k; j++) {
					sum += list[i].scoreList[j];
				}
				list[i].total = sum;
			}

			Arrays.sort(list);

			for (int i = 0; i < n; i++) {
				if (list[i].id == x) {
					System.out.println(String.valueOf(i + 1));
				}
			}
		}
	}

}
