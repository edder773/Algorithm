import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] x = new int[3];
		int sum = 0;
		for (int i = 0; i < 3; i++) {
			x[i] = Integer.parseInt(br.readLine());
			sum += x[i];
		}
		if (sum == 180) {
			if (x[0] == x[1] && x[1] == x[2] && x[2] == x[0]) {
				System.out.println("Equilateral");
			}
			else if (x[0] == x[1] || x[1] == x[2] || x[2] == x[0]) {
				System.out.println("Isosceles");
			}
			else {
				System.out.println("Scalene");
			}
		}
		else {
			System.out.println("Error");
		}
	}
}