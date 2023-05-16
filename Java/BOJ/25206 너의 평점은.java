import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        HashMap <String,Double> dict= new HashMap <String,Double>();
        dict.put("A+",4.5);
        dict.put("A0",4.0);
        dict.put("B+",3.5);
        dict.put("B0",3.0);
        dict.put("C+",2.5);
        dict.put("C0",2.0);
        dict.put("D+",1.5);
        dict.put("D0",1.0);
        dict.put("F",0.0);
        double sum = 0;
        double n = 0;
        for (int i = 0; i < 20; i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	String subject = st.nextToken();
        	double score = Double.parseDouble(st.nextToken());
        	String grade = st.nextToken();
        	if (grade.equals("P")) {
        		continue;
        	}
        	else {
        		sum += score * dict.get(grade);
        		n += score;
        	}
        }
        double result = sum / n;
        System.out.println(result);
    }
}