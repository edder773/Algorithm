import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	static int N;
	static int M;
	static boolean visited[][];
	static int[][] maze;
	static int[] dy = {-1, 1, 0, 0};
	static int[] dx = {0, 0, 1, -1};
	
	public static void find(int a, int b) {
		Queue<int[]> queue = new LinkedList<>();
		queue.add(new int[] {a,b});
		visited[a][b] = true;
		while(!queue.isEmpty()) {
			int now[] = queue.poll();
			int y = now[0];
			int x = now[1];
			for (int i = 0; i<4; i++) {
				int ny = y + dy[i];
				int nx = x + dx[i];
				if (ny >= 0 && ny < N && nx >= 0 && nx < M) {
					if(!visited[ny][nx] && maze[ny][nx] == 1) {
						queue.add(new int[] {ny, nx});
						maze[ny][nx] = maze[y][x] + 1;
						visited[ny][nx] = true;
					}
				}
			}
		}
	}
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        maze = new int[N][M];
        for(int i = 0; i < N; i++) {
        	String S = br.readLine();
        	for (int j = 0; j < M; j++) {
        		maze[i][j] = S.charAt(j) - '0';
        	}
        }
        visited = new boolean[N][M];
        find(0,0);
        System.out.println(maze[N-1][M-1]);
    }
}