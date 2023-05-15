import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int C = Integer.parseInt(br.readLine());
		for (int i = 0; i < C; i++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			int sum = 0;
			int N = Integer.parseInt(st.nextToken());
			int[] nums = new int[N];
			for (int j = 0; j < N; j++) {
				int value = Integer.parseInt(st.nextToken());
				nums[j] = value;
				sum += value;
			}
			float avg = sum/N;
			double count = 0;
			for (int k = 0; k < N; k++) {
				if (nums[k] > avg) {
					count++;
				}
			}
			double x = count/N*100;
			System.out.printf("%.3f",x);
			System.out.println("%");
		}
	}
}