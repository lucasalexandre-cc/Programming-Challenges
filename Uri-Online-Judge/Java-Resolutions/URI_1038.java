import java.util.Locale;
import java.util.Scanner;
public class URI_1038 {
	public static void main(String[] args){
		Locale.setDefault(Locale.US);
		Scanner input = new Scanner(System.in);
		String x = input.nextLine();
		String[] y = x.split(" ");
		int P = Integer.parseInt(y[0]);
		int Q = Integer.parseInt(y[1]);
		if (P == 1){
			System.out.println(String.format("Total: R$ %.2f",Q*4.00));
		}else if(P == 2){
			System.out.println(String.format("Total: R$ %.2f",Q*4.50));
		}else if(P == 3){
			System.out.println(String.format("Total: R$ %.2f",Q*5.00));
		}else if (P==4){
			System.out.println(String.format("Total: R$ %.2f",Q*2.00));
		}else if (P == 5){
			System.out.println(String.format("Total: R$ %.2f",Q*1.50));
		}
		
	}
}
