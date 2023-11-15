import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());

        String[] cards = new String[n];
        for (int i = 0; i < n; i++) {
            cards[i] = br.readLine().trim();
        }

        Set<String> result = new HashSet<>();

        perm(cards, result, 0, k);

        System.out.println(result.size());
    }

    private static void perm(String[] cards, Set<String> result, int depth, int k) {
        if (depth == k) {
            StringBuilder num = new StringBuilder();
            for (int i = 0; i < k; i++) {
                num.append(cards[i]);
            }
            result.add(num.toString());
            return;
        }

        for (int i = depth; i < cards.length; i++) {
            String temp = cards[i];
            cards[i] = cards[depth];
            cards[depth] = temp;

            perm(cards, result, depth + 1, k);
            temp = cards[i];
            cards[i] = cards[depth];
            cards[depth] = temp;
        }
    }
}