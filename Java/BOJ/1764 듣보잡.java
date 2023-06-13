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
        HashMap<String,String> x = new HashMap<String, String>();
        for(int i = 0; i < N; i++) {
        	String person = br.readLine();
        	if(!x.containsKey(person)) {
        		x.put(person, person);        		
        	}
        }
        StringBuilder sb = new StringBuilder();
        ArrayList<String> y = new ArrayList<>();
        for(int i = 0; i < M; i++) {
        	String check = br.readLine();
        	if (x.containsKey(check)) {
        		y.add(check);
        	}
        }
        Collections.sort(y);
        for(int i = 0; i < y.size(); i++) {
        	sb.append(y.get(i)).append("\n");
        }
        System.out.println(y.size());
        System.out.println(sb);
    }
}