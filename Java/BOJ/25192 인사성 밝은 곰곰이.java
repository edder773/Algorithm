import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int N = Integer.parseInt(br.readLine());
    	int count = 0;
    	HashMap <String, String> people = new HashMap<String, String>();
    	for (int i = 0; i < N; i++) {
    		String check = br.readLine();
    		if (check.equals("ENTER")) {
    			people = new HashMap<String, String>();
    		}
    		else {
    			if (!people.containsKey(check)) {
    				people.put(check, check);
    				count++;    				
    			}
    		}
    	}
    	System.out.println(count);
	}
}