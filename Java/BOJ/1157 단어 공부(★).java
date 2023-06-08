import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().toUpperCase();
        char[] S = input.toCharArray();
        HashSet<Character> Sr = new HashSet<>();
        for (char c : S) {
            Sr.add(c);
        }
        ArrayList<Integer> cnt = new ArrayList<>();
        for (char i : Sr) {
            int count = 0;
            for (char j : S) {
                if (i == j) {
                    count++;
                }
            }
            cnt.add(count);
        }
        int max = Integer.MIN_VALUE;
        int maxIndex = -1;
        for (int i = 0; i < cnt.size(); i++) {
            if (cnt.get(i) > max) {
                max = cnt.get(i);
                maxIndex = i;
            }
        }
        int maxCount = 0;
        for (int i = 0; i < cnt.size(); i++) {
            if (cnt.get(i) == max) {
                maxCount++;
            }
        }
        if (maxCount > 1) {
            System.out.println("?");
        } else {
            System.out.println(Sr.toArray()[maxIndex]);
        }
    }
}
