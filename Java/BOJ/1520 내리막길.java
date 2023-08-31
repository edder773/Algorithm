import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static int N, M;
	static int[][] board;
	static int[][] visited;
	static int[] dy = {1,-1,0,0};
	static int[] dx = {0, 0, 1, -1};
	
	static int find(int y, int x) {
		if (y == N-1 && x == M - 1) {
			return 1;
		}
		if (visited[y][x] != -1) {
			return visited[y][x];
		}
		visited[y][x] = 0;
		
		for (int i = 0; i < 4; i++) {
			int ny = y + dy[i];
			int nx = x + dx[i];
			if (0 <= ny && ny < N && 0 <= nx && nx < M && board[y][x] > board[ny][nx]) {
				visited[y][x] += find(ny, nx);
			}
		}
		return visited[y][x];
	}
	
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        board = new int[N][M];
        visited = new int[N][M];
        for (int i = 0; i < N; i++) {
        	st = new StringTokenizer(br.readLine(), " ");
        	for (int j = 0; j < M; j++) {
        		board[i][j] = Integer.parseInt(st.nextToken());
        		visited[i][j] = -1;
        	}
        }
        System.out.println(find(0,0));
    }
}
