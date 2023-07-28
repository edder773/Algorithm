import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap<Character, int[]> temp = new HashMap<>();
        char[] S = br.readLine().toCharArray();
        int q = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        
        for(int i = 0; i < q; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        	char a = st.nextToken().charAt(0);
        	int l = Integer.parseInt(st.nextToken());
        	int r = Integer.parseInt(st.nextToken());
        	int cnt = 0;
        	if (!temp.containsKey(a)) {
                int[] temp1 = new int[S.length];
                for (int j = 0; j < S.length; j++) {
                    if (a == S[j]) {
                        cnt++;
                    }
                    temp1[j] = cnt;
                }
                temp.put(a, temp1);
            }

            int[] acc_sum = temp.get(a);
            if (l > 0) {
                sb.append(acc_sum[r] - acc_sum[l - 1]).append('\n');
            } else {
            	 sb.append(acc_sum[r]).append('\n');
            }
        }
        System.out.println(sb);
	}
}