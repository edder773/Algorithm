import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0 ; t < T; t++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int J = Integer.parseInt(st.nextToken());
        	int N = Integer.parseInt(st.nextToken());
        	List<Integer> box = new ArrayList<>();
        	for (int i = 0; i< N; i++) {
        		st = new StringTokenizer(br.readLine());
        		int R = Integer.parseInt(st.nextToken());
        		int C = Integer.parseInt(st.nextToken());
        		box.add(R*C);
        	}
        	Collections.sort(box, Collections.reverseOrder());
        	int result = 0;
        	 for (int i = 0; i < N; i++) {
                 if (box.get(i) <= J) {
                     J -= box.get(i);
                     result++;
                 } else {
                     if (J > 0) {
                         result++;
                     }
                     break;
                 }
             }
        	System.out.println(result);
        }
    }
}