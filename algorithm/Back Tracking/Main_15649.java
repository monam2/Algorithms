import java.util.ArrayList;
import java.util.Scanner;

public class Main_15649 {
	static ArrayList<Integer> result = new ArrayList<>();
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		int m = sc.nextInt();
		boolean[] nums = new boolean[n+1];
		for (int i = 1; i < n+1; i++) {
			nums[i] = false;
		}
		
		rec(n,m,nums);
	}
	
	static void rec(int n, int m, boolean[] nums) {
		if (result.size() == m) {
			for (Integer integer : result) {
				System.out.print(integer + " ");
			}
			System.out.println();
			return;
		}
		for (int i = 1; i <= n; i++) {
			if (nums[i]) continue;
			nums[i]=true;
			result.add(i);
			rec(n, m, nums);
			nums[i]=false;
			result.remove(result.size()-1);
		}
	}
}
