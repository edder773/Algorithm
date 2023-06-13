import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String x = br.readLine();
        Set<String> k= new HashSet<String>();
        for(int i = 0; i < x.length(); i++) {
        	for (int j = i+1; j <= x.length(); j++) {
        		k.add(x.substring(i,j));
        	}
        }
        System.out.println(k.size());
	}
}