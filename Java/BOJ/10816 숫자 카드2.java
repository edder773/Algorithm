import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        HashMap<Integer, Integer> cards = new HashMap<Integer, Integer>();
        for (int i = 0; i < N; i++) {
        	int card = Integer.parseInt(st.nextToken());
        	if (!cards.containsKey(card)){
        		cards.put(card, 1);
        	}
        	else {
        		cards.put(card, cards.get(card)+1);
        	}
        }
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i++) {
        	int m = Integer.parseInt(st.nextToken());
        	if (cards.containsKey(m)) {
        		sb.append(cards.get(m)).append(" ");        		
        	}
        	else {
        		sb.append(0).append(" ");
        	}
        }
        System.out.println(sb);
    }
}