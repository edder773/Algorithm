import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		while(true) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			int c = Integer.parseInt(st.nextToken());
			if (a == 0 && b == 0 && c == 0) {
				break;
			}
			int maxValue = Math.max(Math.max(a, b), c);
			int line = 0;
			if (maxValue == a) {
				line = b + c;
			}
			else if (maxValue == b) {
				line = a + c;
			}
			else {
				line = a + b;
			}
			if (line > maxValue) {
				if (a == b && b == c && c == a) {
					System.out.println("Equilateral");
				}
				else if (a == b || b == c || c == a) {
					System.out.println("Isosceles");
				}
				else {
					System.out.println("Scalene");
				}
			}
			else {
				System.out.println("Invalid");
			}
		}
	}
}