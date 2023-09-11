import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
	static int n, m;
	static int[][] visited, land;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        visited = new int[n][m];
        land = new int[n][m];
        int ay = 0;
        int ax = 0;
        int[] dy = {0, 0, 1, -1};
        int[] dx = {1, -1, 0, 0};
        for (int i = 0 ; i < n; i++) {
        	st = new StringTokenizer(br.readLine());
        	for(int j = 0 ; j < m ; j++) {
        		int num = Integer.parseInt(st.nextToken());
        		visited[i][j] = -1;
        		if (num == 2) {
        			ay = i;
        			ax = j;
        		}
        		else if (num == 0) {
        			visited[i][j] = 0;
        		}
        		land[i][j] = num;
        	}
        }
        Deque <int[]> deque = new LinkedList<>();
        int[] arr = {ay, ax};
        deque.add(arr);
        visited[ay][ax] = 0;
        while (!deque.isEmpty()) {
        	int[] temp = deque.pollFirst();
        	int y = temp[0];
        	int x = temp[1];
        	for (int i = 0 ; i < 4; i++) {
        		int ny = y + dy[i];
        		int nx = x + dx[i];
        		if (ny >= 0 && ny < n && nx >= 0 && nx < m && visited[ny][nx] == -1 && land[ny][nx] == 1) {
        			visited[ny][nx] = visited[y][x] + 1;
        			int[] arr2 = {ny, nx};
        			deque.addLast(arr2);
        		}
        	}	
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < n; i++) {
        	for (int j =0; j <m; j++) {
        		sb.append(visited[i][j]).append(" ");
        	}
        	sb.append('\n');
        }
        System.out.println(sb);
    }
}