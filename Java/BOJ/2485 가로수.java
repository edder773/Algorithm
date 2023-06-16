import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static int GCD(int a, int b) {
		if (a % b == 0) {
			return b;
		}
		return GCD(b, a%b);
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] tree = new int[N];
        for (int i = 0 ; i < N; i++) {
        	tree[i] = Integer.parseInt(br.readLine());
        }
        int[] tree_distance = new int[N-1];
        for (int i = 0; i < N-1; i++) {
        	tree_distance[i] = tree[i+1] - tree[i];
        }
        int num = tree_distance[0];
        for (int i = 1; i < N-1; i++) {
        	num = GCD(num, tree_distance[i]);
        }
        int result = 0;
        for (int i = 0; i< N-1; i++) {
        	result += (tree_distance[i]/num)-1;
        }
        System.out.println(result);
	}
}