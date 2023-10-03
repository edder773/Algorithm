import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        HashMap <Long, Integer> card = new HashMap<>();
        for (int i = 0; i < N; i++) {
        	long x = Long.parseLong(br.readLine());
        	if (card.containsKey(x)) {
        		card.put(x, card.get(x)+1);
        	}
        	else {
        		card.put(x, 1);
        	}
        }
        TreeSet<Long> cards = new TreeSet<>(card.keySet());
        
        int max = 0;
        for (Long i : card.keySet()) {
        	if (max < card.get(i)) {
        		max = card.get(i);
        	}
        }
        
        for (Long i : cards) {
        	if (card.get(i) == max) {
        		System.out.println(i);
        		break;
        	}
        }
    }
}