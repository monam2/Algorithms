import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main_30892 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		//정렬 후 내가 먹을 수 있는 애들은 스택에 담아놓고, 끝에서부터 확인한다.
		st = new StringTokenizer(br.readLine());
		
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		st = new StringTokenizer(br.readLine());
		int[] arr = new int[n];
		for (int i = 0; i < arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		long result;
	
		Arrays.sort(arr);
		//오름차순 정렬
		//1 5 10 15 24
		
		//스택 두개
		//1. 모든 상어를 담을 스택
		//2. 아기상어가 먹을 상어 스택
		Stack<Integer> sharks = new Stack<>();
		Stack<Integer> toEat = new Stack<>();
		
		//큰 상어부터 스택에 넣음
		for (int i = n-1; i >=0; i--) {
			sharks.push(arr[i]);
		}
		result = m;
		for (int i = 0; i < k; i++) { //먹을 수 있는 마릿수동안 반복
			while(!sharks.isEmpty() && sharks.peek() < result) {
				//상어 스택이 비어있지 않고, 제일 위의 상어가 result보다 작으면
				toEat.push(sharks.pop()); //제일 위의 상어를 뽑아서 먹을 스택에 넣음
			}
			if (!toEat.isEmpty()) { //먹을 스택이 비어있지 않으면 잡아먹기
				result += toEat.pop();
			}
		}
		System.out.println(result);
	}//end main
}//end class
