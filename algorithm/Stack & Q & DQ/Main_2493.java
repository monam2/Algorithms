import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main_2493 {
//	앞에서부터 입력을 받음
//
//	스택이 비어있으면? 현재 탑에서 닿을 수 있는 탑이 없음
//	-> 스택에 현재 탑 추가. (인덱스+1) 반환
//
//	스택이 비어있지 않을때
//	-> 스택의 마지막 요소가 현재 탑보다 크면
//	--> 거기에 레이저가 닿음 : 그거 출력하고 끝
//
//	-> 스택의 마지막 요소가 현재 탑보다 작으면
//	--> 그 탑은 스택에서 빼야함
//
//	어쨋거나 지난 탑은 스택에 넣어야함.
//	스택에서 뺄지 말지 결정하는건 다음 탑과 비교시.
	
	static int n;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;
		
		n = Integer.parseInt(br.readLine());
		Stack<int[]> stack = new Stack<int[]>(); //idx, val
		st = new StringTokenizer(br.readLine());
		for (int i = 0; i < n; i++) {
			int now = Integer.parseInt(st.nextToken());
			while (!stack.isEmpty()) {
				if (stack.peek()[1]<now) { //스택 마지막 요소가 현재 탑보다 작으면
					stack.pop();
				} else { //스택 마지막 요소가 현재 탑보다 크면 -> 그 탑에 닿음
					System.out.print(stack.peek()[0]+1 + " ");
					break;
				}
			}
			if (stack.isEmpty()) {
				System.out.print(0 + " ");
			}
			stack.push(new int[] {i, now});
		}
	}
}
