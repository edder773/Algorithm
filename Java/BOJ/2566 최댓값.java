import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] board = new int[9][9];
        for (int i = 0; i < 9; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	for (int j = 0; j < 9; j++) {
        		board[i][j] = Integer.parseInt(st.nextToken());        		
        	}
        }
        StringBuilder sb = new StringBuilder();
        int y = 0;
        int x = 0;
        int maxValue = Integer.MIN_VALUE;
        for (int i = 0; i < 9; i++) {
        	for (int j = 0; j < 9; j++) {
        		if (board[i][j] > maxValue) {
        			maxValue = board[i][j];
        			y = i;
        			x = j;
        		}
        	}
        }
        sb.append(y+1).append(" ").append(x+1);
        System.out.println(maxValue);
        System.out.println(sb);
    }
}