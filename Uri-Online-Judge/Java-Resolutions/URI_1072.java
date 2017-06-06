import java.util.Scanner;
public class URI_1072 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int x = input.nextInt();
		int in = 0;
		int out = 0;
		int num;
		for(int i = 0;i<x;i++){
			num = input.nextInt();
			if (num>= 10 && num<=20){
				in++;
			}else{
				out++;
			}
		}
		System.out.printf("%d in\n",in);
		System.out.printf("%d out\n",out);
	}
}
