import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for (int t = 0; t < T; t++) {
        	Deque<Integer> queue = new LinkedList<>();
        	StringTokenizer st = new StringTokenizer(br.readLine()," ");
        	int N = Integer.parseInt(st.nextToken());
        	int M = Integer.parseInt(st.nextToken());
        	st = new StringTokenizer(br.readLine()," ");
        	for (int i = 0; i < N; i++) {
        		queue.add(Integer.parseInt(st.nextToken()));
        	}
        	int result = 0;
        	while (!queue.isEmpty()) { // 큐가 빌때까지
        		int out = 0; // 우선 순위가 가장 높은게 나감
        		for (Integer x : queue) { 
        			if (x > out) {
        				out = x;
        			}
        		}
        		int front = queue.poll(); // 맨 앞에 껄 꺼내
        		M --; // 찾고자 하는 위치 -1
        		if (out == front) { // 우선순위 가장 높은게 맨 앞에 있으면
        			result += 1; // 출력 + 1
        			if (M < 0){ // M < 0 이면 가장 앞에 있는것이니
        				System.out.println(result);
        				break;
        			}
        		}
        		else {
        			queue.add(front); // 다시 뒤로 붙이고
        			if (M < 0) { // 이때 찾는게 맨 앞에 있으면
        				M = queue.size()-1; // 맨 뒤의 위치 지정
        			}
        		}
        	}
        }
    }
}