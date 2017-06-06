import java.util.Scanner;
public class URI_1049 {
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		String[] vertebrados = {"ave","carnivoro","aguia","ave","onivoro","pomba","mamifero","onivoro","homem",
				"mamifero","herbivoro","vaca"};
		String[] invertebrados = {"inseto","hematofago","pulga","inseto","herbivoro","lagarta"
				,"anelideo","hematofago","sanguessuga","anelideo","onivoro","minhoca"};
		String P1 = input.next();
		String P2 = input.next();
		String P3 = input.next();
		if(P1.equals("vertebrado")){
			for(int i = 0;i<12;i+= 3){
				if(P2.equals(vertebrados[i])){
					for(int j = i+1;j<12;j+=3){
						if(P3.equals(vertebrados[j])){
							System.out.println(vertebrados[j+1]);
							break;
							}
						}
					break;
					}
			}
		}else{
			for(int i = 0;i<12;i+= 3){
				if(P2.equals(invertebrados[i])){
					for(int j = i+1;j<12;j+=3){
						if(P3.equals(invertebrados[j])){
							System.out.println(invertebrados[j+1]);
							break;
							}
						}
					break;
					}
			}
		}
	}
}
