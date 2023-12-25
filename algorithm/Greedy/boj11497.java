//백준 11497 통나무 건너뛰기
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Collections;
import java.util.StringTokenizer;

public class boj11497 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		
		int t = Integer.parseInt(br.readLine());
		for (int i=0; i<t;i++) { //테케 반복
			int n = Integer.parseInt(br.readLine());
			st = new StringTokenizer(br.readLine());
			
			Integer[] arr = new Integer[n];
			for (int j=0;j<n;j++) {
				arr[j]= Integer.parseInt(st.nextToken());
			}
			
			Arrays.sort(arr, Collections.reverseOrder());
			
			int gap = 0;
			for (int k=0; k<n-2;k++) {
				gap =  Math.max(gap, Math.abs(arr[k]-arr[k+2]));
			}
			System.out.println(gap);
		}
	}
}
