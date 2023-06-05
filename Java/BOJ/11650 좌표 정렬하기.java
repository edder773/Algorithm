import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] arr = new int[N][2];
        for (int i = 0; i < N; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	arr[i][0] = Integer.parseInt(st.nextToken());
        	arr[i][1] = Integer.parseInt(st.nextToken());
        }
        
        Arrays.sort(arr,(a,b) -> {
        	if(a[0] == b[0]) { // x좌표와 y좌표가 같으면
        		return a[1] - b[1]; // y좌표가 증가하는 순서대로
        	}
        	else {
        		return a[0] - b[0];
        	}
        });
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < N; i++) {
        	sb.append(arr[i][0] + " " + arr[i][1]).append('\n');
        }
        System.out.println(sb);
    }
}