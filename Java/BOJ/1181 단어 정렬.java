import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] x = new String[N];
        for (int i = 0 ; i < N; i++) {
        	x[i] = br.readLine();
        }
        Set<String> uniqueStrings = new LinkedHashSet<>(Arrays.asList(x));
        String[] y = uniqueStrings.toArray(new String[0]);
        
        Arrays.sort(y, Comparator.comparingInt(String::length).thenComparing(Comparator.naturalOrder()));
        for (String str : y) {
        	System.out.println(str);
        }
    }
}