import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Solution_1225 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		for (int t = 1; t <= 10; t++) {
			st = new StringTokenizer(br.readLine());
			int tc = Integer.parseInt(st.nextToken());
			ArrayDeque<Integer> q = new ArrayDeque<>();
			st = new StringTokenizer(br.readLine());
			for (int i = 0; i < 8; i++) {
				q.add(Integer.parseInt(st.nextToken()));
			}
			boolean flag = true;
			while (flag) {
				for (int i = 0; i < 5; i++) {
					int tmp = q.pollFirst();
					tmp-=i+1;
					if (tmp<=0) {
						tmp=0;
						flag = false;
					}
					q.add(tmp);
					if (!flag) break;
				}
			}
			System.out.print("#"+tc+" ");
			for (Integer integer : q) {
				System.out.print(integer + " ");
			}
			System.out.println();

		}// end for - t
	}//end main
}//end class
