import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader; 

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String S = br.readLine();
		int[] nums = new int[26];
		for (int i = 0; i < 26; i++) {
			nums[i] = -1;
		}
		for (int i = 0; i < S.length(); i++) {
			int num = S.charAt(i)-97;
			if (nums[num] == -1) {
				nums[num] = i;
			}
		}
		StringBuilder sb = new StringBuilder();
		for (int i = 0; i < 26; i++) {
			sb.append(nums[i]).append(" ");
		}
		System.out.println(sb);
	}
}