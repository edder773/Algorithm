import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 
import java.util.HashMap;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		HashMap <String, Integer> dict = new HashMap <String, Integer>();
		dict.put("ABC", 3);
		dict.put("DEF", 4);
		dict.put("GHI", 5);
		dict.put("JKL", 6);
		dict.put("MNO", 7);
		dict.put("PQRS", 8);
		dict.put("TUV", 9);
		dict.put("WXYZ", 10);
		String S = br.readLine();
		int result = 0;
		for (int i =0; i < S.length(); i++) {
			char s = S.charAt(i);
			for (String j : dict.keySet()){
				for (int k = 0; k < j.length(); k++) {
					if (j.charAt(k) == s) {
						result += dict.get(j);
					}
				}
			}
		}
		System.out.println(result);
	}
}