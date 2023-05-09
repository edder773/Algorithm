public class 10810 공넣기 {
    
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int [] basket = new int[N];
		for (int m = 0; m < M; m++) {
			st = new StringTokenizer(br.readLine()," ");
			int i = Integer.parseInt(st.nextToken());
			int j = Integer.parseInt(st.nextToken());
			int k = Integer.parseInt(st.nextToken());
			for (int n = i-1; n < j; n++) {
				basket[n] = k;
			}
		}
		for (int i = 0; i < N; i++) {
			System.out.printf("%d ",basket[i]);
		}
		System.out.println();
	}
}