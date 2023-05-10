import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int T = Integer.parseInt(br.readLine());
		for (int i = 0; i< T; i++) {
			String S = (String)br.readLine();
			System.out.print(S.charAt(0));
			System.out.println(S.charAt(S.length()-1));
		}
	}
}