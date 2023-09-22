import java.io.*;
import java.util.*;
import java.math.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] vowel = {"a", "e", "i", "o", "u"};
        while (true) {
            String password = br.readLine();
            boolean check = true;
            int checknum = 0;

            if (password.equals("end")) {
                break;
            }
            
            int flag = 0;
            for (String i : vowel) {
                if (password.contains(i)) {
                    flag = 1;
                	break;
                }
            }
            if(flag == 0) {
                check = false;
            }
            
            int vt = 0, ct = 0;
            for (int i = 0; i < password.length(); i++) {
                char ch = password.charAt(i);
                if ("aeiou".indexOf(ch) != -1) {
                    vt++;
                    ct = 0;
                } else {
                    vt = 0;
                    ct++;
                }

                if (vt == 3 || ct == 3) {
                    check = false;
                    break;
                }
            }

            for (int i = 0; i < password.length() - 1; i++) {
                if (password.charAt(i) == password.charAt(i + 1) && password.charAt(i) != 'e' && password.charAt(i) != 'o') {
                    check = false;
                    break;
                }
            }

            if (check) {
                System.out.println("<" + password + "> is acceptable.");
            } else {
                System.out.println("<" + password + "> is not acceptable.");
            }
        }   
    }
}