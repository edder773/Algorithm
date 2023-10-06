import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int K = Integer.parseInt(br.readLine());
        for (int T = 1 ; T < K+1; T++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	int N = Integer.parseInt(st.nextToken());
        	int[] students = new int[N];
        	for(int i = 0 ; i < N; i++) {
        		students[i] = Integer.parseInt(st.nextToken());
        	}
        	Arrays.sort(students);
        	int result = 0; 
        	for(int i = 0; i < N-1; i++) {
        		result = Math.max(result, students[i+1] - students[i]);
        	}
        	System.out.println("Class " + T);
        	System.out.println("Max " + students[N-1] + ", " + "Min " + students[0] + ", " + "Largest gap " + result);
        }
    }
}