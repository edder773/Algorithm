import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int x[] = new int[3];
		int y[] = new int[3];
		
		for (int i = 0; i < 3; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine());
			x[i] = Integer.parseInt(st.nextToken());
			y[i] = Integer.parseInt(st.nextToken());
		}
		
		int a = 0;
		int b = 0;
		
		if(x[0] == x[1]) {
			a = x[2];
		}
		else if (x[0] == x[2]) {
			a = x[1];
		}
		else if (x[1] == x[2]){
			a = x[0];
		}
		
		if(y[0] == y[1]) {
			b = y[2];
		}
		else if (y[0] == y[2]) {
			b = y[1];
		}
		else if (y[1] == y[2]) {
			b = y[0];
		}
		System.out.println(a+" "+b);
	}
}