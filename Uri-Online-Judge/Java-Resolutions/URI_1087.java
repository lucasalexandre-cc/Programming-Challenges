import java.util.Scanner;
public class URI_1087 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		String num = input.nextLine();
		String array[] = new String[4];
		array = num.split(" ");
		int X1 = Integer.parseInt(array[0]);
		int Y1 = Integer.parseInt(array[1]);
		int X2 = Integer.parseInt(array[2]);
		int Y2 = Integer.parseInt(array[3]);
		while (X1!= 0 || X2 != 0 || Y1 != 0 || Y2 != 0){
		
		if(X1 == X2 && Y1 == Y2){
			System.out.println(0);
		}else if (X1-Y1 == X2-Y2 || X1 == X2 || Y1 == Y2){
			System.out.println(1);
		}else{
			int a1 = X2;
			int a2 = Y2;
			int b1 = a1;
			int b2 = a2;
			while (true){
				a1 --;
				a2 ++;
				b1++;
				b2--;
				if ((a1 == X1 && a2 == Y1)||(b1 == X1 && b2 == Y1)){
					System.out.println(1);
					break;
				}
				if ((a1 < 0 || a2 > 8)&&(b1 > 8 || b2 < 0)){
					System.out.println(2);
					break;
				}
			}
		}
		num = input.nextLine();
		array = num.split(" ");
		X1 = Integer.parseInt(array[0]);
		Y1 = Integer.parseInt(array[1]);
		X2 = Integer.parseInt(array[2]);
		Y2 = Integer.parseInt(array[3]);
		}
	}
}
