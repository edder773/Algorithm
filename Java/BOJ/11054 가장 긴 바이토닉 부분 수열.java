import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int[] x = new int[N];
        int[] y = new int[N];
        for(int i = 0 ; i < N; i++) {
        	x[i] = Integer.parseInt(st.nextToken());
        	y[i] = 1;
        }
        for (int i = 1; i < N; i++) {
        	for(int j = 0; j <i; j++) {
        		if(x[j] < x[i]) {
        			y[i] = Math.max(y[i], y[j]+1);
        		}
        	}
        }
        for (int i = 1; i < N; i++) {
        	for(int j = 0; j <i; j++) {
        		if(x[j] > x[i]) {
        			y[i] = Math.max(y[i], y[j]+1);
        		}
        	}
        }
        int maxValue = 0;
        for(int i = 0; i < N; i ++) {
        	if (maxValue < y[i]) {
        		maxValue = y[i];
        	}
        }
        System.out.println(maxValue);
	}
}