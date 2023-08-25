import java.util.*;
import java.io.*;

public class Main {
	static int N;
	static int C;
	static int[] x;
	
	static int search() {
		int start = 1 ;
		int end = x[N-1] - x[0];
		int result = 0;
		while (start <= end) {
			int mid = (start+end)/2;
			int num = x[0];
			int count = 1;
			
			for (int i = 0 ; i < N; i ++) {
				if (x[i] >=  num + mid) {
					count++;
					num = x[i];
				}
			}
			if (count >= C) {
				start = mid + 1;
				result = mid;
			}
			else {
				end = mid- 1;
			}
		}
		return result;
	}
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        N = Integer.parseInt(st.nextToken());
        C = Integer.parseInt(st.nextToken());
        x = new int[N];
        for(int i = 0; i < N; i ++) {
        	x[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(x);
        System.out.println(search());
    }
}
