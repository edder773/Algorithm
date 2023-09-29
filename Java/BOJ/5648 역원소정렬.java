import java.io.*;
import java.util.*;
import java.math.*;

public class Main{
	public static void main(String[] args) throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()," ");
        int n = Integer.parseInt(st.nextToken());
        List<Long> num = new ArrayList<>();
        while(st.hasMoreTokens()) {
        	String reversedStr1 = new StringBuilder(st.nextToken()).reverse().toString();
        	num.add(Long.parseLong(reversedStr1));
        }
        while (num.size() < n) {
            st = new StringTokenizer(br.readLine(), " ");
            while (st.hasMoreTokens()) {
                String reversedStr2 = new StringBuilder(st.nextToken()).reverse().toString();
                num.add(Long.parseLong(reversedStr2));
            }
        }

        Collections.sort(num);

        for (Long i : num) {
            System.out.println(i);
        }
	}
}