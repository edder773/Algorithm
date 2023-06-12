import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        HashMap<String,String> people = new HashMap<String,String>();
        String person = "";
        String check = "";
        for (int i = 0; i < N; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	person = st.nextToken();
        	check = st.nextToken();
        	if (check.equals("enter")) {
        		people.put(person, check);
        	}
        	else {
        		people.remove(person);
        	}
        }
        ArrayList<String> list = new ArrayList<String>(people.keySet());
        Collections.sort(list, Collections.reverseOrder());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < list.size(); i++) {
        	sb.append(list.get(i)).append("\n");
        }
        System.out.println(sb);
    }
}