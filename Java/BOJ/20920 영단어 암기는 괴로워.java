import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine()," ");
    	int N = Integer.parseInt(st.nextToken());
    	int M = Integer.parseInt(st.nextToken());
    	HashMap <String, Integer> x = new HashMap <>();
    	for (int i = 0; i < N; i++) {
    		String S = br.readLine();
    		if (S.length() >= M) {
    			x.put(S, x.getOrDefault(S, 0) + 1);
    		}
    	}
    	
    	List<String> result = new ArrayList<>(x.keySet());
    	Collections.sort(result);
    	result.sort((a, b) -> Integer.compare(b.length(), a.length()));
    	result.sort((a, b) -> Integer.compare(x.get(b), x.get(a)));
    	StringBuilder sb = new StringBuilder();
    	for (String word : result) {
    		sb.append(word).append('\n');
    	}
    	System.out.println(sb);
	}
}