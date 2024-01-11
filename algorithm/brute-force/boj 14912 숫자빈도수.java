//백준 14912 숫자빈도수
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int d = Integer.parseInt(st.nextToken());
		
		int answer = 0;
		
		for (int i=1; i<=n; i++) {
			String numS = Integer.toString(i);
			for (int j=0; j<numS.length(); j++) {

				if (numS.charAt(j) == Integer.toString(d).charAt(0)) {
					answer += 1;
				}
			}
		}
		
		System.out.println(answer);
		
	}
	
	
	
}
