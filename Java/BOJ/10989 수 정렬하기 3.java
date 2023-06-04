import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(); 
        int N = Integer.parseInt(br.readLine());
        int[] nums = new int[10000001];
        
        for (int i = 0; i < N; i++) {
        	nums[Integer.parseInt(br.readLine())]++;
        }
        
        for(int i = 0; i < nums.length; i++) {
        	while(nums[i] > 0) {
        		sb.append(i).append("\n");
        		nums[i]--;
        	}
        }
        System.out.print(sb);
    }
}