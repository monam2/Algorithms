import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.Stack;

public class Solution_1218 {
	public static void main(String[] args) throws IOException {
		/*
		 * 괄호의 짝을 찾기
		 * char배열에 모든 괄호를 넣고 반복문을 돌린다.
		 * 
		 * 스택이 비어있고 (, {, <, [ 이면 스택에 넣는다.
		 * i가 닫는 괄호이고( }, ), >,  ) i와 스택의 마지막 요소(peek)가 같다면, 스택에서 pop한다.
		 * 이걸 반복
		 * 
		 * 반복이 끝났을 때 스택에 남아 있는 요소가 있으면 0 else 1
		 */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		for (int t = 1; t <= 10; t++) {

			int n = Integer.parseInt(br.readLine());
			char[] arr = br.readLine().toCharArray();

			Stack<Character> stk = new Stack<>();

			for (int i = 0; i < arr.length; i++) {
				//스택이 비어있는데 닫는 괄호가 들어온다? -> 바로 종료
				//스택이 비어있는데 여는 괄호 -> 스택에 추가
				if (stk.size()==0) {
					if (arr[i]=='}' || arr[i]==']' || arr[i]=='>' || arr[i]==')') {
						stk.push(arr[i]);
						break; //스택 비었는데 닫는괄호 추가 시 종료
					}
					if (arr[i]=='{' || arr[i]=='[' || arr[i]=='<' || arr[i]=='(') {
						stk.push(arr[i]);
						continue;
					}
				}


				//스택이 비어있지 않을 때
				// 닫는 괄호이면 아래 조건문
				// 여는 괄호는 무조건 스택에 추가
				if (arr[i]=='}' || arr[i]==']' || arr[i]=='>' || arr[i]==')') {
					if (!stk.empty() && stk.peek()=='{' && arr[i]=='}') stk.pop();
					else if (!stk.empty() && stk.peek()=='[' && arr[i]==']') stk.pop();
					else if (!stk.empty() && stk.peek()=='(' && arr[i]==')') stk.pop();
					else if (!stk.empty() && stk.peek()=='<' && arr[i]=='>') stk.pop();	
					else break;
				} else stk.push(arr[i]);

			}
			if (stk.empty()) System.out.println("#"+t + " " + 1);
			else System.out.println("#"+t + " " + 0);
		}//end for
	}//end main
}//end class
