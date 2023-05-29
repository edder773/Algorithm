import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		int maxY = Integer.MIN_VALUE;
		int maxX = Integer.MIN_VALUE;
		int minY = Integer.MAX_VALUE;
		int minX = Integer.MAX_VALUE;
		
		for (int i = 0; i < N; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			int y = Integer.parseInt(st.nextToken());
			int x = Integer.parseInt(st.nextToken());
			if (maxX < x) {
				maxX = x;
			}
			if (maxY < y) {
				maxY = y;
			}
			if (minX > x) {
				minX = x;
			}
			if (minY > y) {
				minY = y;
			}
		}
		System.out.println((maxX-minX)*(maxY-minY));
	}
}