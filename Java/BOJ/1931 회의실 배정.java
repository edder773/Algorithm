import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] meeting = new int[N][2];
        
        for(int i = 0; i < N; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	meeting[i][0] = Integer.parseInt(st.nextToken());
        	meeting[i][1] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(meeting, (a,b) -> a[1] == b[1] ? a[0] - b[0] : a[1] - b[1]);
        
        int cnt = 1;
        int temp = meeting[0][1];
        for(int i = 1; i< N; i++) {
        	if(meeting[i][0] >= temp) {
        		temp = meeting[i][1];
        		cnt++;
        	}
        }
        System.out.println(cnt);
    }
}