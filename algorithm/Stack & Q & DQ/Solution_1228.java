import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.Stack;
import java.util.StringTokenizer;
 
public class Solution_1228 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
        for (int t = 1; t <= 10; t++) {
             
             
            ArrayDeque<Integer> q = new ArrayDeque<>();
            int n = Integer.parseInt(br.readLine());
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < n; i++) {
                q.offerLast(Integer.parseInt(st.nextToken()));
            }
            int commandNum = Integer.parseInt(br.readLine());
             
            Stack<Integer> stack1 = new Stack<>(); //원본 암호문 잠깐 보관
            Stack<Integer> stack2 = new Stack<>(); //새로 넣을 암호문 순서 정리
             
            st = new StringTokenizer(br.readLine());
            for (int i = 0; i < commandNum; i++) {
                 
                String I = st.nextToken();
                int x = Integer.parseInt(st.nextToken());
                int y = Integer.parseInt(st.nextToken());
                 
                for (int j = 0; j < x; j++) { //x번 빼서 스택에 넣어놓기
                    int tmp = q.pollFirst();
                    stack1.push(tmp);
                }
                 
                for (int j = 0; j < y; j++) { //입력 새 암호를 스택에 넣어서 순서 바꾸고
                    int code = Integer.parseInt(st.nextToken());
                    stack2.add(code);
                }
                for (int j = 0; j < y; j++) { //암호 큐에 넣음
                    q.offerFirst(stack2.pop());
                }
                 
                for (int j = 0; j < x; j++) { //stack1에 보관했던 원래 암호 다시 추가
                    q.offerFirst(stack1.pop());
                }
            }
             
            System.out.print("#"+t+" ");
            for (int i = 0; i < 10; i++) {
                System.out.print(q.pollFirst() + " ");
            }
             
             
             
        }//end for
    }//end main
}//end class
