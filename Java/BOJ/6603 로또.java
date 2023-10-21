import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static int[] S;
	static int k;
	static Stack<Integer> lotto = new Stack<>();
	static void find(int n) {
		if (lotto.size() == 6) {
			StringBuilder sb = new StringBuilder();
			for(int i = 0 ; i < 6; i++) {
				sb.append(lotto.get(i)).append(" ");
			}
			System.out.println(sb);
			return;
		}
		for (int i = n ; i < k; i++) {
			if (!lotto.contains(S[i])) {
				lotto.add(S[i]);
				find(i);
				lotto.pop();		
			}
		}
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	k = Integer.parseInt(st.nextToken());
        	if (k == 0) {
        		break;
        	}
        	S = new int[k];
        	for (int i = 0 ; i < k; i++) {
        		S[i] = Integer.parseInt(st.nextToken());
        	}
        	find(0);
        	System.out.println();
        	
        }        
    }
}