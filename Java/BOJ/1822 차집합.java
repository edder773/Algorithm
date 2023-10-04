import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int nA = Integer.parseInt(st.nextToken());
        int nB = Integer.parseInt(st.nextToken());
        Set<Integer> A = new HashSet<>();
        Set<Integer> B = new HashSet<>();
        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0 ; i < nA; i++) {
        	A.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine(), " ");
        for(int i = 0 ; i < nB; i++) {
        	B.add(Integer.parseInt(st.nextToken()));
        }
        
        Set<Integer> AnB = new HashSet<>(A);
        AnB.removeAll(B);
        
        System.out.println(AnB.size());
        StringBuilder sb = new StringBuilder();
        if(!AnB.isEmpty()) {
        	List<Integer> result = new ArrayList<>(AnB);
        	Collections.sort(result);
        	for(int x : result) {
        		sb.append(x).append(" ");
        	}
        	System.out.println(sb);
        }
    }
}