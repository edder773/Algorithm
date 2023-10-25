import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String S = br.readLine();
        String[] letter = new String[S.length()];
        for(int i = 0 ; i < S.length(); i++) {
        	letter[i] = S.substring(i);
        }
        Arrays.sort(letter);
        StringBuilder sb = new StringBuilder();
        for (int i = 0 ; i < S.length(); i++) {
        	sb.append(letter[i]).append("\n");
        }
        System.out.println(sb);
    }
}