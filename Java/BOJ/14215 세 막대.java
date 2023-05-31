import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Arrays;

public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int[] x = new int[3];
		for (int i = 0; i < 3; i++) {
			x[i] = Integer.parseInt(st.nextToken());
		}
		Arrays.sort(x);
		while (x[0] + x[1] <= x[2]) {
			x[2]--;
		}
		System.out.println(x[0]+x[1]+x[2]);
	}
}