import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	StringTokenizer st = new StringTokenizer(br.readLine()," ");
    	int minValue = Integer.MAX_VALUE;
    	int maxValue = Integer.MIN_VALUE;
    	for (int i = 0; i < N; i++) {
    		int m = Integer.parseInt(st.nextToken());
    		minValue = Math.min(minValue, m);
    		maxValue = Math.max(maxValue, m);
    	}
    	System.out.println(minValue*maxValue);
	}
}