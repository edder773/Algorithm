import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        Deque<Integer> queue = new LinkedList<>();
        for(int i = 0; i< N; i++) {
        	queue.add(i+1);
        }
        while (queue.size() > 1){
        	queue.poll();
        	queue.add(queue.poll());
        }
        System.out.println(queue.peek());        
    }
}