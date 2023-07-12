import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] house = new int[N][3];
        for(int i = 0; i < N; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	for(int j = 0; j < 3; j++) {
        		house[i][j] = Integer.parseInt(st.nextToken());
        	}
        }
        for(int i = 1; i < N; i++) {
        	house[i][0] = Math.min(house[i-1][1], house[i-1][2]) + house[i][0];
        	house[i][1] = Math.min(house[i-1][0], house[i-1][2]) + house[i][1];
        	house[i][2] = Math.min(house[i-1][0], house[i-1][1]) + house[i][2];
        }
        int result = Integer.MAX_VALUE;
        for (int j = 0; j < 3; j++) {
        	if (result > house[N-1][j]) {
        		result = house[N-1][j];
        	}
        }
        System.out.println(result);
    }
}