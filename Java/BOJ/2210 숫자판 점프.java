import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static String[][] nums = new String[5][5];
	static int[][] move = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
	static HashSet<String> result = new HashSet<>();
	public static void find(int a,int b,int n,String num) {
		if (n == 6) {
			result.add(num);
			return;
		}
		for (int[] p : move) {
			int ny = a + p[0];
			int nx = b + p[1];
			if (ny >= 0 && ny < 5 && nx >= 0 && nx < 5) {
				find(ny, nx, n+1, num+nums[ny][nx]);
			}
		}
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        for (int i = 0; i < 5; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	for (int j = 0 ; j < 5; j++) {
        		nums[i][j] = st.nextToken();
        	}
        }
        for (int i = 0; i < 5; i++) {
        	for (int j = 0; j < 5; j++) {
        		find(i, j, 0, "");
        	}
        }
        System.out.println(result.size());
    }
}