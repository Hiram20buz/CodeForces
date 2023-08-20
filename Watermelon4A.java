import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Watermelon4A {

	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(in.readLine());
	
		 if ((N % 2 != 0) || (N == 2)) {
		    System.out.println("N0");
		} else {
		    System.out.println("YES");
		}
		/*
		String result = (N % 2 != 0) || (N == 2) ? "N0" : "YES";
		System.out.println(result);
		*/
	}

}
