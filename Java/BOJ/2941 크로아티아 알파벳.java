import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String S = br.readLine();
		S=S.replace("c=", "x");
		S=S.replace("c-", "x");
		S=S.replace("dz=", "x");
		S=S.replace("d-", "x");
		S=S.replace("lj","x");
		S=S.replace("nj", "x");
		S=S.replace("s=", "x");
		S=S.replace("z=", "x");
		System.out.println(S.length());
	}
}