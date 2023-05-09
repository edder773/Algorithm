import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine());
		int maxValue = Integer.MIN_VALUE;
		int minValue = Integer.MAX_VALUE;
		StringBuilder sb = new StringBuilder();
		for (int i=0; i < N; i++) {
			int num = Integer.parseInt(st.nextToken());
			if (num > maxValue) {
				maxValue = num;
			}
			if (num < minValue) {
				minValue = num;
			}
		}
		sb.append(minValue).append(" ");
		sb.append(maxValue);
		System.out.println(sb);
	}
}