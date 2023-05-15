import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int result = N;
		for (int t = 0; t < N; t++) {
			String words = br.readLine();
			for (int i = 0; i < words.length()-1; i++) {
				if (words.charAt(i) ==(words.charAt(i+1))){
					continue;
				}
				else if (words.substring(i+1).contains(Character.toString(words.charAt(i)))) {
						result--;
						break;
				}
			}
		}
		System.out.println(result);
	}
}