import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        List<Integer> lecture = new ArrayList<>();
        
        for(int k = 0; k < N; k++) {
        	st = new StringTokenizer(br.readLine());
        	int P = Integer.parseInt(st.nextToken());
        	int L = Integer.parseInt(st.nextToken());
        	List<Integer> m = new ArrayList<>();
        	st = new StringTokenizer(br.readLine());
        	for (int i = 0 ; i < P; i++) {
        		m.add(Integer.parseInt(st.nextToken()));
        	}
        	
        	Collections.sort(m, Collections.reverseOrder());
        	if ( P < L) {
        		lecture.add(1);
        	}
        	else {
        		lecture.add(m.get(L-1));
        	}
        }
        Collections.sort(lecture);
        int result =0;
        for (int i : lecture) {
        	if(M >= i) {
        		result += 1;
        		M -= i;
        	}
        }
        System.out.println(result);
    }
}