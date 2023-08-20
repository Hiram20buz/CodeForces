import java.util.Scanner;

public class DominoPiling50A {

    public static void main(String[] args) {
        Scanner ip = new Scanner(System.in);
        String inputLine = ip.nextLine(); 
        String[] digitStrings = inputLine.split(" "); 
        int digits = 1;
        for (int i = 0; i < digitStrings.length; i++) {
            digits = digits * Integer.parseInt(digitStrings[i]);
        }

        System.out.println(digits / 2);
    }
}
