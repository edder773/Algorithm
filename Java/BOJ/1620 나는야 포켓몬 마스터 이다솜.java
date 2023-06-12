import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        HashMap<String, Integer> pocket = new HashMap<String, Integer>();
        HashMap<Integer, String> pocket2 = new HashMap<Integer, String>();
        for (int i = 1; i <= N; i++) {
        	String m = br.readLine();
        	pocket.put(m, i);
        	pocket2.put(i, m);
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= M; i++) {
        	String check = br.readLine();
        	if(check.matches("\\d+")){
        		int index = Integer.parseInt(check);
        		sb.append(pocket2.get(index)).append("\n");
        	}
        	else {
        		sb.append(pocket.get(check)).append("\n");
        	}
        }
        System.out.println(sb);
    }
}