import java.util.Scanner;
public class URI_1069 { 
	public static void main(String[] args){
		Scanner input = new Scanner (System.in);
		int cont = input.nextInt();
		for(int i = 0;i<cont;++i){
			int cont2 = 0;
			int qnt = 0;
			String diamante = input.next();
			for (int j = 0;j<diamante.length();++j){
				char letra = diamante.charAt(j);
				if (letra == '<'){
					cont2 += 1;
				}else if(letra == '>'){
					cont2 -= 1;
					if(cont2 >= 0){
						qnt += 1;
					}else{
						cont2 = 0;
					}
				}
			}
			System.out.println(qnt);
		}
	}
}
