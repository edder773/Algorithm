import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    private static char[] result;

    public static void x(int a, int n) {
        if (n == 1) {
            return;
        }
        for (int i = a + n / 3; i < a + (n / 3) * 2; i++) {
            result[i] = ' ';
        }
        x(a, n / 3);
        x(a + n / 3 * 2, n / 3);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            try {
                String input = br.readLine();
                if (input == null || input.isEmpty()) {
                    break; // Exit the loop when there is no more input
                }

                int T = Integer.parseInt(input);
                result = new char[(int) Math.pow(3, T)];
                for (int i = 0; i < result.length; i++) {
                    result[i] = '-';
                }
                x(0, (int) Math.pow(3, T));
                System.out.println(String.valueOf(result));
            } catch (NumberFormatException e) {
                System.err.println("Invalid input. Please enter a valid integer.");
            }
        }
    }
}