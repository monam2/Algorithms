import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main_17592 { //백준 17592 과제는 끝나지 않아!
	
	static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	static StringTokenizer st;
	
	static int n, score;
	static Stack<int[]> stack;
	
	public static void main(String[] args) throws IOException {
		n = Integer.parseInt(br.readLine());
		score = 0;
		stack = new Stack<int[]>();
		
		for (int i = n; i > 0; i--) {
			st = new StringTokenizer(br.readLine());
			int work = Integer.parseInt(st.nextToken());
			//work가 1일 경우
			if (work==1) {
				int A = Integer.parseInt(st.nextToken());
				int T = Integer.parseInt(st.nextToken());
				
				T--;
				
				//일을 받자마자 했을 때, 바로 못 끝내면 스택에 넣어야 함
				if (T > 0) stack.add(new int[] {A, T});
				else score += A;
			}
			//work가 0일 경우
			else {
				if (!stack.isEmpty()) { //앞에서 못끝낸 일이 남아 있으면
					int[] todo = stack.pop();
					todo[1]--;
					
					if (todo[1]>0) {//일이 다 안끝났으면 다시 스택에 넣어야 함
						stack.add(todo);
					} else score += todo[0];
				}
			}

		}//end i
		System.out.println(score);
	}//end main
}//end class
