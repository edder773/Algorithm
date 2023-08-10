import java.io.*;
import java.util.*;

public class Main {
	static int N;
	static Character[][] image;
	static String result = "";
	public static void find (int y, int x, int n ) {
		char color = image[y][x];
		for (int i = y; i < y + n; i++) {
			for (int j = x; j < x + n; j++) {
				if (color != image[i][j]) {
					int m = n/2;
					result += "(";
					find(y, x, m);
					find(y, x+m,m);
					find(y+m, x, m);
					find(y+m, x+m, m);
					result += ")";
					return;
				}
			}
		}
		if (color == '1') {
			result += "1";
		}
		else {
			result += "0";
		}
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        image = new Character[N][N];
        for(int i = 0 ; i < N; i++) {
        	String S = br.readLine();
        	for (int j = 0 ; j < N; j++) {
        		image[i][j] = S.charAt(j);
        	}
        }
        find(0,0,N);
        System.out.println(result);
    }
}