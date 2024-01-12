import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int[] arr = new int[n];
		
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		Arrays.sort(arr, Collections.reverseOrder());
		
		int[] result = new int[n];
		for (int j=0; j<n; j++) {
			result[j] = arr[j] * (j+1);
		}
		
		int mx = 0;
		for (int k=0; k<result.length; k++) {
			mx = Math.max(mx, result[k]);
		}
		System.out.println(mx);
	}
}
