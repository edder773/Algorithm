import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int j = Integer.parseInt(br.readLine());
        int start = 0;
        int end = M;
        int move = 0;
        for (int t = 0; t < j; t++) {
        	int x = Integer.parseInt(br.readLine());
        	if (x < start) {
        		move += start - x;
        		start = x;
        		end = x + M - 1;
        	}
        	else if(x > end){
        		move += x - end;
        		end = x;
        		start = end - M + 1;
        	}
        }
        System.out.println(move);
    }
}