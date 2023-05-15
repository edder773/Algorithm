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
		int[] basket = new int[N];
		for (int i=0; i<N; i++) {
			basket[i] = i+1;
		}
		int[] rotate = new int[N];
		for (int t = 0; t < M; t++ ) {
			st = new StringTokenizer(br.readLine());
			int i = Integer.parseInt(st.nextToken())-1;
			int j = Integer.parseInt(st.nextToken())-1;
			int k = Integer.parseInt(st.nextToken())-1;
			int tmp = i;
			for (int x = 0; x < j-i+1; x++) {
				if(k+x <= j) {
					rotate[x+i] = basket[k+x];
				}
				else {
					rotate[x+i] = basket[tmp];
					tmp++;
				}
			}
			for (int y = 0; y < N; y++) {
				if (rotate[y] != 0) {
					basket[y] = rotate[y];
				}
			}
		}
		StringBuilder result = new StringBuilder();
		for (int z = 0; z < N; z ++) {
			result.append(basket[z]).append(" ");
		}
		System.out.println(result);
	}
}