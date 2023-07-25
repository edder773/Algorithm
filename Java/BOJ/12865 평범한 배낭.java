import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());
        List<int[]> items = new ArrayList<>();
        for(int i = 0 ; i < N; i++) {
        	st = new StringTokenizer(br.readLine()," ");
        	int weight = Integer.parseInt(st.nextToken());
        	int value =  Integer.parseInt(st.nextToken());
        	items.add(new int[] {weight, value});
        }
        Collections.sort(items, (a,b) -> Integer.compare(b[1], a[1]));
        Map<Integer, Integer> bag = new HashMap<>();
        bag.put(0, 0);
        for(int[] item : items) {
        	int weight = item[0];
        	int value = item[1];
        	Map<Integer, Integer> temp = new HashMap<>(bag);
        	
        	for(Map.Entry<Integer, Integer> entry : bag.entrySet()) {
        		int i = entry.getKey();
        		int j = entry.getValue();
        		
        		int newValue = value + i;
        		int newWeight = weight + j;
        		
        		if(bag.getOrDefault(newValue, K+1) > newWeight){
        			temp.put(newValue, newWeight);
        		}
        	}
        	bag.putAll(temp);
        }
        int max = Collections.max(bag.keySet());
        System.out.println(max);
    }
}
