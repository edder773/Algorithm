import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] nums = new int[30];
		for(int i = 0; i < 28; i++) {
			int num = Integer.parseInt(br.readLine());
			nums[num-1] = 1;
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i <30; i++) {
			if (nums[i] == 0 ) {
				sb.append(i+1).append('\n');
			}
		}
		System.out.println(sb);
	}
}