import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Iterator;
import java.util.StringTokenizer;

public class Main_1244 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());

		int[] arr = new int[n+1];
		st = new StringTokenizer(br.readLine());
		for (int i = 1; i < arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}

		st = new StringTokenizer(br.readLine());
		int mansN = Integer.parseInt(st.nextToken());
		int[] gender = new int[mansN];
		int[] number = new int[mansN];
		for (int i = 0; i < mansN; i++) {
			st = new StringTokenizer(br.readLine());
			gender[i] = Integer.parseInt(st.nextToken());
			number[i] = Integer.parseInt(st.nextToken());
		}
		//로직 시작

		for (int i = 0; i < mansN; i++) {
			if (gender[i]==1) { //남학생이면
				ArrayList<Integer> muls = new ArrayList<Integer>();
				for (int j = 1; j < n+1; j++) {
					if (j%number[i]==0) {
						muls.add(j);
					}
				}
				for (Integer num : muls) {
					if (arr[num]==0) arr[num]=1;
					else arr[num] = 0;
				}
			} else { //여학생이면
				int mid = number[i];
				int left = mid-1;
				int right = mid+1;
				HashSet<Integer> toChg = new HashSet<Integer>();
				toChg.add(number[i]);
				while (left>0 && right<arr.length) {
					if (arr[left]!=arr[right]) {
						break;
					}
					
					for (int j = left; j < right+1; j++) {
						toChg.add(j);
					}
					left--;
					right++;
				}
				for (int j : toChg) {
					if (arr[j]==0) arr[j]=1;
					else arr[j] = 0;
				}
			}
		}
		int cnt = 1;
		for (int i = 1; i < arr.length; i++) {
			System.out.print(arr[i] + " ");
			if (cnt%20==0) System.out.println();
			cnt++;
		}
	}
}
