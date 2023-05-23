import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int line = 0;
        int end = 0;
        int top = 0;
        int bottom = 0;
        while (N > end) {
        	line++;
        	end += line;
        }
        int r = end - N;
        if (line % 2 == 0) {
        	top = line - r;
        	bottom = r + 1;
        }
        else {
        	top = r + 1;
        	bottom = line - r;
        }
        System.out.printf("%d/%d", top, bottom);
    }
}