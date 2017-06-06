import java.util.ArrayList;
import java.util.Scanner;
public class URI_1179 {
	public static void main(String[] args){
		Scanner input = new Scanner(System.in);
		ArrayList<Integer> par = new ArrayList<> ();
		ArrayList<Integer> impar = new ArrayList<> ();
		int num;
		for(int i = 0; i<15;i++){
			num = input.nextInt();
			if(num%2 == 0){
				par.add(num);
			}else{
				impar.add(num);
			}
			if (par.size() == 5){
				for(int j = 0;j<5;j++){
					System.out.printf("par[%d] = %d\n",j,par.get(j));
				}
				par.clear();
			}else if(impar.size() == 5){
				for(int j = 0;j<5;j++){
					System.out.printf("impar[%d] = %d\n",j,impar.get(j));
				}
				impar.clear();
			}
		}
		if(impar.size() > 0){
			for(int j = 0;j<impar.size();j++){
				System.out.printf("impar[%d] = %d\n",j,impar.get(j));
			}
		}
		if(par.size() > 0){
			for(int j = 0;j<par.size();j++){
				System.out.printf("par[%d] = %d\n",j,par.get(j));
			}
		}
	}
}
