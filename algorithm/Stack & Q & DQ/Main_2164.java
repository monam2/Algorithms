import java.util.ArrayDeque;
import java.util.Scanner;

public class Main_2164_강창우 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		ArrayDeque<Integer> q = new ArrayDeque<>();
		for (int i = 1; i < n+1; i++) {
			q.add(i);
		}
		
		while (q.size()>1) {
			q.pollFirst();
			int tmp = q.pollFirst();
			q.offerLast(tmp);
		}
		System.out.println(q.peek());
	}
}
