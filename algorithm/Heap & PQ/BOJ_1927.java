import java.util.PriorityQueue;
import java.util.Scanner;

public class BOJ_1927 { //백준 1927 최소 힙

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		PriorityQueue<Integer> pq = new PriorityQueue<Integer>();
		for (int i = 0; i < n; i++) {
			int num = sc.nextInt();
			if (num==0) {
				if (pq.size()==0) {
					System.out.println(0);
					continue;
				}
				int a = pq.poll();
				System.out.println(a);
				continue;
			}
			pq.add(num);
		}
	}
}
