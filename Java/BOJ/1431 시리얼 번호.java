import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String[] serial = new String[N];

        for (int i = 0; i < N; i++) {
            serial[i] = br.readLine().trim();
        }

        Arrays.sort(serial, new Comparator<String>() {
            public int compare(String s1, String s2) {
                if (s1.length() != s2.length()) {
                    return s1.length() - s2.length();
                } else {
                    int sum1 = sumDigits(s1);
                    int sum2 = sumDigits(s2);
                    if (sum1 != sum2) {
                        return sum1 - sum2;
                    } else {
                        return s1.compareTo(s2);
                    }
                }
            }
        });

        for (String s : serial) {
            System.out.println(s);
        }
    }

    public static int sumDigits(String str) {
        int sum = 0;
        for (char c : str.toCharArray()) {
            if (Character.isDigit(c)) {
                sum += Character.getNumericValue(c);
            }
        }
        return sum;
    }
}