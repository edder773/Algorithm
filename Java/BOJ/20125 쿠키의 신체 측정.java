import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int heart_x = 0;
        int heart_y = 0;
        int back = 0;
        int arm_left = 0 ;
        int arm_right = 0 ;
        int leg_left = 0;
        int leg_right = 0;
        
        for (int i = 0 ; i < N; i++) {
        	String S = br.readLine();
        	for (int j = 0 ; j < N; j++) {
        		if (S.charAt(j) == '*') {
        			if (heart_x == 0 && heart_y == 0) {
        				heart_x = i+1;
        				heart_y = j;
        			}
        			else if (heart_x == i && heart_y > j) {
        				arm_left++;
        			}
        			else if (heart_x == i && heart_y < j) {
        				arm_right++;
        			}
        			else if (heart_x < i && heart_y == j) {
        				back++;
        			}
        			else if (heart_x + back < i && heart_y > j) {
        				leg_left++;
        			}
        			else if (heart_x + back < i && heart_y < j) {
        				leg_right++;
        			}
        		}
        	}
        }
        StringBuilder sb = new StringBuilder();
        sb.append(heart_x+1).append(" ");
        sb.append(heart_y+1).append("\n");
        sb.append(arm_left).append(" ");
        sb.append(arm_right).append(" ");
        sb.append(back).append(" ");
        sb.append(leg_left).append(" ");
        sb.append(leg_right).append(" ");
        System.out.println(sb);
    }
}