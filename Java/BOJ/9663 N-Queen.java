import java.util.*;
import java.io.*;


public class Main {
	static int N;
	static int cnt;
	static int[] board;
	public static void Queen(int n) {
		for (int i = 0; i < N; i++) {
			if (promise(n,i)) {
				board[n] = i;
				if (n == N-1) {
					cnt++;
					return;
				}
				else {
					Queen(n+1);
				}
			}
		}
	}
	
	public static boolean promise(int a, int b) {
		for (int i = 0; i < a; i++) {
			if (board[i] == b || Math.abs(board[i]-b) == Math.abs(i-a)) {
				return false;
			} 
		}
		return true;
	}
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		N = Integer.parseInt(br.readLine());
		board = new int[N];
		cnt = 0;
		Queen(0);
		System.out.println(cnt);
	}
}