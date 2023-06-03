import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
	static public void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		String[][] chess = new String[N][M];
		for (int i = 0; i < N; i++) {
			String x = br.readLine();
			for (int j = 0; j < M; j++) {
				chess[i][j] = String.valueOf(x.charAt(j));
			}
		}

		int result = Integer.MAX_VALUE;
		for (int i = 0; i < N-7; i++) {
			for (int j = 0; j < M-7; j++) {
				int x = 0;
				int y = 0;
				for (int a = i; a < i+8; a++) {
					for (int b = j; b < j+8; b++) {
						if ((a+b) % 2 == 0) {
							if (chess[a][b].equals("W")) {
								x++;
							}
							if (chess[a][b].equals("B")) {
								y++;
							}
						}
						else {
							if (chess[a][b].equals("B")) {
								x++;
							}
							if (chess[a][b].equals("W")) {
								y++;
							}
						}
					}
				}
				if (x < result) {
					result = x;
				}
				if (y < result) {
					result = y;
				}
			}
		}
		System.out.println(result);
	}
}