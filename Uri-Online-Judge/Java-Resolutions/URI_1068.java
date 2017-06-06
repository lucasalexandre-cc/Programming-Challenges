import java.util.Scanner;
public class URI_1068 {
	public static void main (String[] args){
		Scanner input = new Scanner (System.in);
		while (true){
			try{
				String texto = input.nextLine();
				int cond = 0;
				boolean cond2 = true;
				for (int i = 0;i<texto.length();++i){
					char letra = texto.charAt(i);
					if (letra == '('){
						cond += 1;
					}else if (letra == ')'){
						cond -= 1;
					}
					
					if (cond < 0){
						cond2 = false;
						break;
					}
				}
				if (cond2 == true && cond == 0){
					System.out.println("correct");
				}else{
					System.out.println("incorrect");
				}
			}catch(Exception EOFErrir){
				break;
			}
		}
		
		}
}
