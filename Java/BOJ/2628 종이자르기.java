import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int T = Integer.parseInt(br.readLine());
        
        ArrayList<Integer> w = new ArrayList<>();
        ArrayList<Integer> h = new ArrayList<>();

        w.add(0);
        w.add(n);
        
        h.add(0);
        h.add(m);

        int result= 0;
        for (int i=0; i<T; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int line = Integer.parseInt(st.nextToken());

            if (x == 0) {
                h.add(line);
            } else {
                w.add(line);
            }
            
            Collections.sort(w);
            Collections.sort(h);

       }
        for (int j=0; j<w.size()-1; j++) {
        	for (int k=0; k<h.size()-1; k++) {
        		
        		int x_diff=w.get(j+1)-w.get(j);
        		int y_diff=h.get(k+1)-h.get(k);
        		
        		result=Math.max(result, x_diff*y_diff);  
        	}
        }
        System.out.println(result); 
    }
}