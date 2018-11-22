import java.util.ArrayList;

public class LinhasCruzadas {

	private int n;
	private ArrayList entradaArray;
	//private int qtddCruzamentos;
	
	public int comparaCruzamento() {
		int s = 0;
		for(int i = 0; i<this.entradaArray.size(); i++ ) {
			for(int j = 1; j<this.n+1; i++) {
				int valorIndex = (int) this.entradaArray.get(i);
				if(valorIndex > j) {
					s+=1;
				}
				else if(valorIndex < j) {
					continue;
				}else {break;}
			}
		}
		
		return s;
	}
	
	public static void main(String[] args) {
		
	}

}
