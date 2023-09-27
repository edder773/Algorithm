import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[][] graph = new int[101][101];
        for(int t = 0; t < 4; t++) {
        	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	int x = Integer.parseInt(st.nextToken());
        	int y = Integer.parseInt(st.nextToken());
        	int nx = Integer.parseInt(st.nextToken());
        	int ny = Integer.parseInt(st.nextToken());
        	for(int i = x; i < nx; i++) {
        		for(int j = y; j < ny; j++) {
        			graph[i][j] = 1;
        		}
        	}
        }
        int result = 0;
        for (int i = 0 ; i < 101; i++) {
        	for (int j = 0; j < 101; j++) {
        		if(graph[i][j] == 1) {
        			result++;
        		}
        	}
        }
        System.out.println(result);
    }
}