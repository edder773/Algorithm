import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int A = Integer.parseInt(st.nextToken());
		int B = Integer.parseInt(st.nextToken());
		int C = Integer.parseInt(br.readLine());
		A += C / 60;
		B += C % 60;
		if (A > 24){
			A = A % 24;
		}
		if (B >= 60) {
			B = B - 60;
			A += 1;
		}
		if (A == 24) {
			A = 0;
		}
		System.out.printf("%d %d",A,B);
		
	}
}