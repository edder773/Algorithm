import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {

	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String S = br.readLine();
		String check = "";
		for (int i = (S.length())-1; i>= 0; i--) {
			check += S.charAt(i);
		}
		if (S.equals(check)) {
			System.out.println(1);
		}
		else {
			System.out.println(0);
		}
	}
}