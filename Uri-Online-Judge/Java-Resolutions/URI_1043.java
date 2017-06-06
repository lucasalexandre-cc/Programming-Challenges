import java.util.Locale;
import java.util.Scanner;
public class URI_1043 {//Main on URI
	public static void main(String[] args){
		Locale.setDefault(Locale.US);
		Scanner input = new Scanner(System.in);
		String num = input.nextLine();
		String[] lista = num.split(" ");
		double A = Double.parseDouble(lista[0]);
		double B = Double.parseDouble(lista[1]);
		double C = Double.parseDouble(lista[2]);
		if((Math.abs(B-C) < A && A < B+C)|| (Math.abs(A-B) < C && C < A+B) || (Math.abs(A-C) < B && B < A+C)){
			System.out.println(String.format("Perimetro = %.1f", A+B+C));
		}else{
			System.out.println(String.format("Area = %.1f", ((A+B)/2)*C));
		}	
	}
}
