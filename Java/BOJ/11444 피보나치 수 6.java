import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static long MOD = 1000000007;
	static long[][] multiply(long[][] a, long[][] b) {
        long[][] c = new long[2][2];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 2; j++) {
                for (int k = 0; k < 2; k++) {
                    c[i][j] = (c[i][j] + (a[i][k] * b[k][j]) % MOD) % MOD;
                }
            }
        }
        return c;
    }

    static long[][] power(long[][] matrix, long n) {
        if (n == 1) {
            return matrix;
        } else {
            long[][] halfMatrix = power(matrix, n / 2);
            long[][] result = multiply(halfMatrix, halfMatrix);
            if (n % 2 == 0) {
                return result;
            } else {
                return multiply(result, matrix);
            }
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        long N = Long.parseLong(br.readLine());

        long[][] x = {{1, 1}, {1, 0}};
        long[][] result = power(x, N);

        System.out.println(result[0][1]);

    }
}