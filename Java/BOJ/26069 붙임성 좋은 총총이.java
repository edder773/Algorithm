import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	ArrayList<String> people = new ArrayList<String>();
    	people.add("ChongChong");
    	for(int i = 0; i < N; i++) {
    		StringTokenizer st = new StringTokenizer(br.readLine()," ");
    		String A = st.nextToken();
    		String B = st.nextToken();
    		if (people.contains(A)) {
    			if (!people.contains(B)) {
    				people.add(B);
    			}
    		}	
    		else if(people.contains(B)) {
    			if(!people.contains(A)) {
    				people.add(A);
    			}
    		}
    	}
    	System.out.println(people.size());
	}
}