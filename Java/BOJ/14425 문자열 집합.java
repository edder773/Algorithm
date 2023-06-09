import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        HashMap<String, Integer> x = new HashMap<String, Integer>();
        for (int i = 0; i < N; i++) {
        	x.put(br.readLine(), 1);
        }
        int result = 0;
        for (int i = 0; i < M; i++) {
        	String str = br.readLine();
        	if (x.containsKey(str)) {
        		result++;
        	}
        }
        System.out.println(result);
    }
}