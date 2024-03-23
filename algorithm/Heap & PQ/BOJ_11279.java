import java.util.PriorityQueue;
import java.util.*;

public class Main { // 백준 11279 최대힙

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
        StringBuilder sb = new StringBuilder();
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>(Collections.reverseOrder());
		for (int i = 0; i < n; i++) {
			int num = sc.nextInt();
			if (num==0) {
				if (pq.size()==0) {
					sb.append("0").append("\n");
					continue;
				}
				int a = pq.poll();
				sb.append(a).append("\n");
				continue;
			}
			pq.add(num);
		}
        System.out.println(sb.toString());
	}
}
