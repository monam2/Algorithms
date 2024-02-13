import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main_16435 {
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st = null;
	static int n, l, fruits[];
	
	public static void main(String[] args) throws IOException {
		st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		l = Integer.parseInt(st.nextToken());
		
		
		st = new StringTokenizer(br.readLine());
		fruits = new int[n];
		for (int i = 0; i < n; i++) {
			fruits[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(fruits);
		
		for (int i = 0; i < fruits.length; i++) {
			if (l >= fruits[i]) {
				l++;
			} else {
				break;
			}
		}
		System.out.println(l);
	}
}
