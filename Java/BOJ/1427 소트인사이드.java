import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(); 
        String N = br.readLine();
        int[] nums = new int[10];
        for (int i = 0; i < N.length(); i++) {
        	int digit = N.charAt(i) - '0';
        	nums[digit]++;
        }
        for (int i = 9; i > -1; i--) {
        	while(nums[i] > 0) {
        		sb.append(i);
        		nums[i]--;
        	}
        }
        System.out.println(sb);
    }
}