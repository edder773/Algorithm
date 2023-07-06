import java.util.*;
import java.io.*;


public class Main {
	private static StringBuilder sb = new StringBuilder();
	static int N, M;
	static List<Integer> s = new ArrayList<>();
	public static void find(int m) {
		if (s.size() == M) {
			for(int i : s) {
				sb.append(i).append(" ");				
			}
			sb.append("\n");
			return;
		}
		for (int i = m; i < N+1; i++) {
			s.add(i);
			find(i);
			s.remove(s.size() -1);
		}
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		find(1);
		System.out.println(sb);
	}
}