import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int X = Integer.parseInt(st.nextToken());
        int[] blog = new int[N];
        st = new StringTokenizer(br.readLine());
        int maxValue = Integer.MIN_VALUE;
        for(int i = 0; i < N; i++) {
        	int num = Integer.parseInt(st.nextToken());
        	blog[i] = num;
        	if (num > maxValue) {
        		maxValue = num;
        	}
        }
        if (maxValue == 0) {
            System.out.println("SAD");
        } else {
            int x = 0;
            int value = 0;
            int result = 1;

            for (int i = 0; i < X; i++) {
                x += blog[i];
            }
            value = x;

            for (int i = X; i < N; i++) {
                value -= blog[i - X];
                value += blog[i];
                if (value > x) {
                    x = value;
                    result = 1;
                } else if (value == x) {
                    result++;
                }
            }

            System.out.println(x);
            System.out.println(result);
        }
    }
}