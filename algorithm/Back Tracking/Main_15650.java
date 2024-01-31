import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main_15650 {
	static ArrayList<Integer> result = new ArrayList<>();
	static int n, m;
	static boolean[] visited;
	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		n = sc.nextInt();
		m = sc.nextInt();
		visited = new boolean[n+1];
		rec(0,1);
	}
	
	static void rec(int cnt, int start) {
		if (result.size()==m) {
			for (Integer integer : result) {
				System.out.print(integer+ " ");
			}
			System.out.println();
			return;
		}
		
		for (int i = start; i <= n; i++) {
			if (visited[i]) continue;
			result.add(i);
			visited[i]=true;
			rec(cnt+1, i+1);
			result.remove(result.size()-1);
			visited[i]=false;
		}
	}
}
