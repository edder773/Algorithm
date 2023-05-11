import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		String A = st.nextToken();
		String B = st.nextToken();
		String rev_A = "";
		String rev_B = "";
		for (int i = A.length()-1; i >= 0; i--) {
			rev_A += A.charAt(i);
		}
		for (int i = B.length()-1; i >= 0; i--) {
			rev_B += B.charAt(i);
		}
		int An = Integer.parseInt(rev_A);
		int Bn = Integer.parseInt(rev_B);
		System.out.println(Math.max(An, Bn));
	}
}