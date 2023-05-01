import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;


public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int H = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		M = M -45;
		if (M < 0) {
			M = M + 60;
			H --;
			if ((H < 0)) {
				H = 23;
			}
		}
		System.out.print(H);
		System.out.print(" ");
		System.out.println(M);
	}
}