import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] paper = new int[100][100];
        int N = Integer.parseInt(br.readLine());
        for (int t = 0; t < N; t ++) {
        	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        	int a = Integer.parseInt(st.nextToken());
        	int b = Integer.parseInt(st.nextToken());
        	for (int i = 0; i < 10; i++) {
        		for (int j = 0; j < 10; j++) {
        			paper[a+i][b+j] = 1;
        		}
        	}
        }
        int result = 0;
        for(int i = 0; i < 100; i++) {
        	for(int j = 0; j< 100; j++) {
        		if(paper[i][j] == 1) {
        			result += 1;
        		}
        	}
        }
        System.out.println(result);
    }
}