import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
	//요세푸스 문제
	static int n, k;
	static ArrayDeque<Integer> q = new ArrayDeque<>();
	static StringBuilder sb = new StringBuilder();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		k = sc.nextInt();
		
		getNums();
		start();
	}//end main
	
	private static void getNums() {
		for (int i = 1; i <= n; i++) {
			q.offer(i);
		}
	}//getNums
	
	private static void start() {
		sb.append("<");
		while (q.size()>1) {
			int cnt = 0;
			while (cnt<k) {
				int tmp = q.pollFirst();
				q.offer(tmp);
				cnt++;
			}
			
			int tmp2 = q.pollLast();
			sb.append(tmp2).append(", ");
		}
		sb.append(q.pollLast()).append(">");
		System.out.println(sb.toString());
	}//Start
}//end class
