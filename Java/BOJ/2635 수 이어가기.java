import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        List<Integer> result = new ArrayList<>();
        for (int i = 1 ; i < N+1; i++) {
        	int next = i;
        	int now = N;
        	List<Integer> temp = new ArrayList<>();
        	temp.add(now);
        	temp.add(i);
        	while(now >= next) {
        		int x = now - next;
        		temp.add(x);
        		now = next;
        		next = x;
        		if (temp.size() > result.size()) {
        			result = temp;
        		}
        	}
        }
        System.out.println(result.size());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < result.size(); i++) {
        	sb.append(result.get(i)).append(" ");
        }
        System.out.println(sb);
    }
}