import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] name = new String[N];
        for (int i = 0 ; i < N; i++) {
        	name[i] = br.readLine();
        }
        String[] asname = Arrays.copyOf(name, N);
        String[] dename = Arrays.copyOf(name, N);
        Arrays.sort(asname);
        Arrays.sort(dename, (a, b) -> b.compareTo(a));
        
        if (Arrays.equals(name, dename)) {
            System.out.println("DECREASING");
        } else if (Arrays.equals(name, asname)) {
            System.out.println("INCREASING");
        } else {
            System.out.println("NEITHER");
        }
    }
}