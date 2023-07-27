import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[] A = new int[N+1];
        st = new StringTokenizer(br.readLine()," ");
        int x = 0;
        for (int i = 1; i < N+1; i++) {
        	int n = Integer.parseInt(st.nextToken());
        	x += n;
        	A[i] = x;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < M; i ++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	int a = Integer.parseInt(st.nextToken())-1;
        	int b = Integer.parseInt(st.nextToken());
        	sb.append(A[b]-A[a]).append("\n");
        }
        System.out.println(sb);
	}
}