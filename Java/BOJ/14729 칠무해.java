import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        double[] scores = new double[N];
        for(int i = 0; i < N; i++) {
        	scores[i] = Double.parseDouble(br.readLine());
        }
        Arrays.sort(scores);
        
        for (int i = 0; i < 7 ; i++) {
        	System.out.printf("%.3f\n", scores[i]);
        }
    }
}