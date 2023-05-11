import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		StringBuilder result = new StringBuilder();
		int[] chess = new int[6];
		chess[0] = 1;
		chess[1] = 1;
		chess[2] = 2;
		chess[3] = 2;
		chess[4] = 2;
		chess[5] = 8;
		for (int i = 0; i < 6; i++) {
			int num = Integer.parseInt(st.nextToken());
			result.append(chess[i]-num).append(" ");
		}
		System.out.println(result);
	}
}