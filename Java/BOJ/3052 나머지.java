import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] nums = new int[42];
		for (int i = 0; i < 10; i++) {
			int num = Integer.parseInt(br.readLine());
			nums[num%42] = 1;
		}
		int result = 0;
		for (int i = 0; i<42; i++) {
			if (nums[i] > 0) {
				result +=1;
			}
		}
		System.out.println(result);
	}
}