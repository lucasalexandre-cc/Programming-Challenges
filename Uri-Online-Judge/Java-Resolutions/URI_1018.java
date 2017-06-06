import java.util.Scanner;
public class URI_1018 {
	public static void main (String[] args){
		Scanner input = new Scanner(System.in);
		int num = input.nextInt();
		System.out.println(num);
		System.out.println(num/100 + " nota(s) de R$ 100,00");
		num -= (num/100)*100;
		System.out.println(num/50 + " nota(s) de R$ 50,00");
		num -= (num/50)*50;
		System.out.println(num/20 + " nota(s) de R$ 20,00");
		num -= (num/20)*20;
		System.out.println(num/10 + " nota(s) de R$ 10,00");
		num -= (num/10)*10;
		System.out.println(num/5 + " nota(s) de R$ 5,00");
		num -= (num/5)*5;
		System.out.println(num/2 + " nota(s) de R$ 2,00");
		num -= (num/2)*2;
		System.out.println(num + " nota(s) de R$ 1,00");
	}
}
