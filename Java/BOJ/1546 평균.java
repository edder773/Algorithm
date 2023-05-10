import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 
import java.util.StringTokenizer;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		int[] nums = new int[N];
		int maxValue = 0;
		for (int i = 0; i < N; i++) {
			int num = Integer.parseInt(st.nextToken());
			nums[i] = num;
			if (maxValue < num) {
				maxValue = num;
			}
		}
		
		double avg = 0;
		for (int j = 0; j < N; j++) {
			double n = (double)(nums[j]*100)/maxValue;
			avg += n;
		}
		double result = avg/N;
		System.out.println(result);
	}
}