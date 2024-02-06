import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class Solution_1233 {
    /*
     * 1. 각 노드 자신은 연산자여야 하고, 노드의 자식들은 숫자여야 함(자손에서 올라온 연산 결과여도 무방)
     * 2. 리프 노드는 반드시 숫자여야 함. 리프 노드를 제외한 노드는 반드시 연산자.
     * 3. 루트 노드는 반드시 연산자여야 함.
     * 
     * 리프노드는 트리 높이가 h라면 2^h이상 2^(h+1)미만 의 번호임
     */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = null;
 
        for(int t=1;t<=10;t++) {
            int n = Integer.parseInt(br.readLine());
//          int h = (int)Math.sqrt(n);
            int result = 1;
            for (int i = 0; i < n; i++) {
                st = new StringTokenizer(br.readLine());
                if (st.countTokens()==4) {
                    st.nextToken();
                    String what = st.nextToken();
                    st.nextToken();
                    st.nextToken();
                     
                    //두번째 요소가 연산자가 아니라면 종료
                    if (what.equals("+") || what.equals("-") ||what.equals("*")||what.equals("/")) continue;
                    result = 0;
                     
                } else {
                    st.nextToken();
                    String what = st.nextToken();
                     
                    if (what.equals("+") || what.equals("-") ||what.equals("*")||what.equals("/")) {
                        result=0;
                    }
                }
//              if (nodeNum<(int)Math.pow(2, h)) { //루트노드이거나 리프노드가 아닐때
//                  if (!(what.equals("+") || what.equals("-") ||what.equals("*")||what.equals("/"))){
//                      sb.append(0);
//                      break; //루트노드, 일반 노드가 연산자가 아니라면 종료
//                  }
//                  int left = Integer.parseInt(st.nextToken());
//                  int right = Integer.parseInt(st.nextToken());
//              } else { //리프노드면 반드시 nodeNum은 숫자여야 함
//              }
            }
            System.out.println("#"+t+" "+result);
        }//end test for
    }//end main
}//end class
