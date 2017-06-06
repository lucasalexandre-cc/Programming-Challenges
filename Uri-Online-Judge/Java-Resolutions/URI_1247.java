import java.util.Scanner;
public class URI_1247 {
	public static void main(String[] args){
		boolean success = true;
		Scanner input = new Scanner (System.in);
		while (success == true){
			try{
			String numeros = input.nextLine();
			String array[] = new String[3];
			array = numeros.split(" ");
			int D = Integer.parseInt(array[0]);
			double VF = Double.parseDouble(array[1]);
			double VG = Double.parseDouble(array[2]);
			double hipotenusa = java.lang.Math.sqrt(12*12+D*D);
			double t1 = 12/VF;
			double t2 = hipotenusa/VG;
			if (t2 <= t1){
				System.out.println("S");
			}else{
				System.out.println("N");
			}	
			} catch (Exception EOFError){
				break;
			}
		}
	}
}
