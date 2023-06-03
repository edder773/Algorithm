import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Main{
	static public int num(String n) {
		int result = 0;
		for(int i = 0; i < n.length(); i++) {
			result += Character.getNumericValue(n.charAt(i));
		}
		return Integer.parseInt(n) + result;
	}
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		ArrayList<Integer> x = new ArrayList<>();
		String N = br.readLine();
		int m = Integer.parseInt(N);
		for(int i = 0; i < m; i++) {
			x.add(num(Integer.toString(i)));
		}
		if (x.contains(m)) {
			System.out.println(x.indexOf(m));
		}
		else {
			System.out.println(0);
		}
	}
}