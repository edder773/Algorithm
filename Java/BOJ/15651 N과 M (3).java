import java.util.*;
import java.io.*;


public class Main {
	private static StringBuilder sb = new StringBuilder();
	static int N, M;
	static List<Integer> s = new ArrayList<>();
	public static void find() {
		if (s.size() == M) {
			for(int i : s) {
				sb.append(i).append(" ");				
			}
			sb.append("\n");
			return;
		}
		for (int i = 1; i <= N; i++) {
			if (s.contains(i)) {
				s.add(i);
				find();
				s.remove(s.size()-1);
			}
			
			if (!s.contains(i)) {
				s.add(i);
				find();
				s.remove(s.size() -1);
			}
		}
	}
	
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		find();
		System.out.println(sb);
	}
}