import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int[] weight = new int[N];
        for (int i = 0; i < N; i++) {
        	weight[i] = Integer.parseInt(st.nextToken());
        }
        int M = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine()," ");
        int[] bead = new int[M];
        for (int i = 0 ; i < M; i++) {
        	bead[i] = Integer.parseInt(st.nextToken());
        }
        
        HashSet<Integer> dp = new HashSet<>();
        dp.add(0);
        
        for (int i : weight) {
        	HashSet<Integer> temp = new HashSet<>();
        	for(int j : dp) {
        		temp.add(i+j);
        		temp.add(Math.abs(i-j));
        	}
        	dp.addAll(temp);
        }
        List<String> result = new ArrayList<>();
        for(int i : bead) {
        	if (dp.contains(i)) {
        		result.add("Y");
        	}
        	else {
        		result.add("N");
        	}
        }
        System.out.println(String.join(" ", result));
    }
}
