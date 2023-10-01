import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<int[]> num = new ArrayList<>();

        for (int i = 1; i <= 8; i++) {
            int score = Integer.parseInt(br.readLine());
            num.add(new int[]{score, i});
        }

        Collections.sort(num, (a, b) -> Integer.compare(b[0], a[0]));

        int result = 0;
        List<Integer> rank = new ArrayList<>();

        for (int i = 0; i < 5; i++) {
            result += num.get(i)[0];
            rank.add(num.get(i)[1]);
        }

        System.out.println(result);

        Collections.sort(rank);
        for (int r : rank) {
            System.out.print(r + " ");
        }
    }
}