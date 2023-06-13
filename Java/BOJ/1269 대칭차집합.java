import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        Set<Integer> A = new HashSet<>();
        st = new StringTokenizer(br.readLine()," ");
        for (int i = 0; i < a; i++) {
        	A.add(Integer.parseInt(st.nextToken()));
        }
        
        Set<Integer> B = new HashSet<>();
        st = new StringTokenizer(br.readLine()," ");
        
        for (int i = 0; i < b; i++) {
        	B.add(Integer.parseInt(st.nextToken()));
        }
        Set<Integer> c = new HashSet<>(A);
        c.removeAll(B);
        Set<Integer> d = new HashSet<>(B);
        d.removeAll(A);
        System.out.println(c.size()+d.size());
	}
}