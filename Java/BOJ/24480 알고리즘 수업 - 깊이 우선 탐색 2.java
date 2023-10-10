import java.util.*;
import java.io.*;

public class Main {
	static int N, M, R;
	static ArrayList<ArrayList<Integer>> graph = new ArrayList<>();
	static int[] visited;
	static int cnt = 1;
	
	public static void dfs(int n) {
		visited[n] = cnt;
		Collections.sort(graph.get(n), Comparator.reverseOrder());
		for(int i = 0; i < graph.get(n).size(); i++) {
			int x = graph.get(n).get(i);
			if (visited[x] == 0) {
				cnt ++;
				dfs(x);
			}
		}
	}
	
    public static void main(String[] args) throws IOException {
    	BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st = new StringTokenizer(br.readLine());
    	N = Integer.parseInt(st.nextToken());
    	M = Integer.parseInt(st.nextToken());
    	R = Integer.parseInt(st.nextToken());
    	visited = new int[N+1];
    	for(int i = 0; i < N+1; i++) {
        	graph.add(new ArrayList<>());
        }
    	for (int i = 0 ; i < M; i++) {
    		st = new StringTokenizer(br.readLine());
    		int u = Integer.parseInt(st.nextToken());
    		int v = Integer.parseInt(st.nextToken());
    		graph.get(u).add(v);
    		graph.get(v).add(u);
    	}
    	
    	dfs(R);
    	StringBuilder sb = new StringBuilder();
    	for (int i = 1; i < N+1; i++) {
        	sb.append(visited[i]).append("\n");
        }
        System.out.println(sb);
    }
}