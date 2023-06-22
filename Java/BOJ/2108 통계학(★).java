import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringBuilder sb = new StringBuilder();
    	int N = Integer.parseInt(br.readLine());
    	int[] nums = new int[N];
    	int[] common = new int[8001];
    	double sum = 0;
    	int maxValue = Integer.MIN_VALUE;
    	int minValue = Integer.MAX_VALUE;
    	int maxCount = 0;
    	for (int i = 0; i < N; i++) {
    		int num = Integer.parseInt(br.readLine());
    		nums[i] = num;
    		common[num+4000]++;
    		sum += num; // 평균을 위한 합
    		maxValue = Math.max(maxValue, num); // 범위를 위한 최대값
    		minValue = Math.min(minValue, num); // 범위를 위한 최소값
    		maxCount = Math.max(maxCount, common[num + 4000]); // 최빈수를 위한 최대 등장수
    	}

    	int index = 0;
    	int flag = 0;
    	for (int i = 0; i < common.length; i++) {
    		if (common[i] == maxCount) {
    			if(index != 0 && flag == 0) {
    				index = i - 4000; // 최빈수가 1개일 수도 있으니 index에 할당
    				flag = 1; // 체크
    			}
    			else if(flag == 0) {
    				index = i - 4000;
    			}
    		}
    	}
    	Arrays.sort(nums);
    	sb.append(Math.round(sum/N)).append("\n");
    	sb.append(nums[N/2]).append("\n");
    	sb.append(index).append("\n");
    	sb.append(maxValue-minValue).append("\n");
    	System.out.println(sb);
	}
}