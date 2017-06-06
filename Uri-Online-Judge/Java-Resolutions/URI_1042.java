import java.util.Arrays;
import java.util.Scanner;
public class URI_1042 {
	public static void main (String[] args){
		Scanner input = new Scanner(System.in);
		String x = input.nextLine();
		String[] y = x.split(" ");
		int[] z = new int[3]; 
		z[0] = Integer.parseInt(y[0]);
		z[1] = Integer.parseInt(y[1]);
		z[2] = Integer.parseInt(y[2]);
		Arrays.sort(z);
		for (int i = 0;i < 3; ++i){
			System.out.println(z[i]);
		}
		System.out.println("");
		for (int i = 0;i<3;++i){
			System.out.println(y[i]);
		}
	}
}
