import java.util.*;
import java.io.*;

public class Main {
    static int[][] board;
    static List<List<Integer>> blank = new ArrayList<>();
    static StringBuilder sb = new StringBuilder();

    public static boolean row(int a, int n) {
        for (int i = 0; i < 9; i++) {
            if (board[a][i] == n) {
                return false;
            }
        }
        return true;
    }

    public static boolean column(int a, int n) {
        for (int i = 0; i < 9; i++) {
            if (board[i][a] == n) {
                return false;
            }
        }
        return true;
    }

    public static boolean square(int y, int x, int n) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (board[(y / 3) * 3 + i][(x / 3) * 3 + j] == n) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void sudoku(int n) {
        if (blank.size() == n) {
            for (int i = 0; i < 9; i++) {
                for (int j = 0; j < 9; j++) {
                    sb.append(board[i][j]).append(" ");
                }
                sb.append("\n");
            }
            System.out.println(sb);
            System.exit(0);
        }
        for (int i = 1; i < 10; i++) {
            int y = blank.get(n).get(0);
            int x = blank.get(n).get(1);
            if (column(x, i) && row(y, i) && square(y, x, i)) {
                board[y][x] = i;
                sudoku(n + 1);
                board[y][x] = 0;
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        board = new int[9][9];
        for (int i = 0; i < 9; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            for (int j = 0; j < 9; j++) {
                int n = Integer.parseInt(st.nextToken());
                board[i][j] = n;
                if (n == 0) {
                    List<Integer> x = new ArrayList<>();
                    x.add(i);
                    x.add(j);
                    blank.add(x);
                }
            }
        }
        sudoku(0);
    }
}