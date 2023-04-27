import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int a = Integer.parseInt(br.readLine());
		String b = br.readLine();
		int i = Character.getNumericValue(b.charAt(0));
		int j = Character.getNumericValue(b.charAt(1));
		int k = Character.getNumericValue(b.charAt(2));
		System.out.println(a*k);
		System.out.println(a*j);
		System.out.println(a*i);
		System.out.println(a*(Integer.parseInt(b)));
		
	}
}