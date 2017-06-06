import java.util.Scanner;
public class URI_1172 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		int[] lista = new int[10];
		for(int i = 0;i<10;i++){
			lista[i] = input.nextInt();
			if (lista[i] <= 0){
				lista[i] = 1;
			}
			System.out.printf("X[%d] = %d\n",i,lista[i]);
		}
		
	}
}
