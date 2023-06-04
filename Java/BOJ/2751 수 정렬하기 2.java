package Main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder(); 
        int N = Integer.parseInt(br.readLine());
        boolean[] nums = new boolean[2000001];
        
        for (int i = 0; i < N; i++) {
        	nums[Integer.parseInt(br.readLine()) + 1000000] = true;
        }
        
        for(int i = 0; i < nums.length; i++) {
        	if(nums[i]) {
        		sb.append(i-1000000).append("\n"); // 여기서 그냥 System.out하면 출력 시간으로 인해 시간 증가
        	}
        }
        System.out.print(sb);
    }
}