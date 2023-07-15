import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	private static Map<Integer, Integer> dp = new HashMap<>();
	private static int find(int n) {
		if (dp.containsKey(n)) {
			return dp.get(n);
		}
		
		int minValue;
		if (n% 3 == 0 && n % 2 == 0) {
			minValue = Math.min(find(n/3) + 1, find(n/2) + 1);
		}
		else if (n % 3 == 0) {
			minValue = Math.min(find(n/3) + 1, find(n-1) + 1);
		}
		else if (n % 2 == 0) {
			minValue = Math.min(find(n/2) + 1, find(n-1) + 1);
		}
		else {
			minValue = find(n-1) + 1;
		}
		
		dp.put(n, minValue);
		return minValue;
	}
	
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int X = Integer.parseInt(br.readLine());
        dp.put(1, 0);
        System.out.println(find(X));
    }
}