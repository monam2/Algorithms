import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.StringTokenizer;

public class BOJ_3961 { //백준 3961 터치 키보드
	private static class Node {
		int x;
		int y;

		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = null;

		
		char[][] keyboard = {
				{'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
				{'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
				{'z', 'x', 'c', 'v', 'b', 'n', 'm'}
		};
		Map<Character, Node> map = new HashMap<>();

		for (int i = 0; i < keyboard.length; i++) {
			for (int j = 0; j < keyboard[i].length; j++) {
				map.put(keyboard[i][j], new Node(i, j));
			}
		}


		int T = Integer.parseInt(br.readLine());
		for (int t = 0; t < T; t++) {
			List<String[]> results = new ArrayList<>();
			
			st = new StringTokenizer(br.readLine());
			String StdWord = st.nextToken();
			int n = Integer.parseInt(st.nextToken());
			String[] words = new String[n];

			for (int i = 0; i < n; i++) {
				words[i] = br.readLine();
			}

			for (String word : words) {
				int distance = 0;
				for (int i = 0; i < StdWord.length(); i++) {
					Node char1 = map.get(StdWord.charAt(i));
                    Node char2 = map.get(word.charAt(i));
                    distance += getDist(char1, char2);
				}
				results.add(new String[] {word, String.valueOf(distance)});
			}
			
			results.sort((a, b) -> {
                int distCompare = Integer.compare(Integer.parseInt(a[1]), Integer.parseInt(b[1]));
                if (distCompare == 0) {
                    return a[0].compareTo(b[0]);
                }
                return distCompare;
            });

            for (String[] result : results) {
                System.out.println(result[0] + " " + result[1]);
            }

		}//for T
	}// main
	
	public static int getDist(Node a, Node b) {
		return Math.abs(a.x - b.x) + Math.abs(a.y - b.y);
	}
}// class
