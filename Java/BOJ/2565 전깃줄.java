import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        ArrayList<int[]> line = new ArrayList<>();
        int[] dp = new int[N];
        
        for (int i = 0 ; i< N; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            line.add(new int[]{a, b});
            dp[i] = 1;
        }
        Collections.sort(line, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[0], o2[0]);
            }
        });
        for (int i = 0 ; i < N; i++) {
            for (int j = 0 ; j < i; j++) {
                if (line.get(i)[1] > line.get(j)[1]) {
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
        }
        int maxValue = 0;
        for (int i = 0 ; i < N; i++) {
            if (maxValue < dp[i]) {
                maxValue = dp[i];
            }
        }
        System.out.println(N-maxValue);
	}
}