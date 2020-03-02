import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;

public class Main {

	public static void main(String[] args) {
		// inverterValoresSemVariavelAuxiliar(5, 2);
		inverterVariavelComVariavelAux(5, 2);
	}

	/// 103 - Inverter String
	public static void inverterString(String texto) {

		char[] outroTexto = new char[texto.length()];
		int j = 0;

		for (int i = texto.length() - 1; i >= 0; i--) {
			outroTexto[j] = texto.charAt(i);
			j++;
		}

		texto = "";

		for (int i = 0; i < outroTexto.length; i++) {
			texto += outroTexto[i];
		}

		System.out.println("String invertida: " + texto);
	}

	// 104
	public static void inverterValoresSemVariavelAuxiliar(int x, int y) {

		System.out.println("Valores Iniciais");
		System.out.println("X:" + x);
		System.out.println("Y:" + y);

		x = x + y;
		y = x - y;
		x = x - y;

		System.out.println("Realizando a troca");
		System.out.println("X:" + x);
		System.out.println("Y:" + y);
	}

	// 104
	public static void inverterVariavelComVariavelAux(int x, int y) {

		System.out.println("Valores Iniciais");
		System.out.println("X:" + x);
		System.out.println("Y:" + y);

		int aux = x;
		x = y;
		y = aux;

		System.out.println("Realizando a troca");
		System.out.println("X:" + x);
		System.out.println("Y:" + y);
	}

	public static void desafio105() {
		List<BigDecimal> lista = new ArrayList<>();
		BigInteger n = new BigInteger("99999999999999999999999999");

		preencherList(BigInteger.valueOf(10), lista);
	}
    // 105
	public static void preencherList(BigInteger n, List<BigDecimal> lista) {
		int i = 1;

		while (true) {

			lista.add(new BigDecimal(i));
			i++;
			if (BigInteger.valueOf(i) == n) {
				break;
			}
		}
		System.out.println(lista);
		verificaMultiplo(lista);
	}
   // 105
	public static void verificaMultiplo(List<BigDecimal> lista) {

		BigDecimal multiplo = new BigDecimal("5");

		for (BigDecimal n : lista) {
			BigDecimal auxDivisao = n.divide(multiplo);
			BigDecimal auxMultiply = auxDivisao.multiply(multiplo);
			if (auxMultiply.equals(n)) {
				System.out.println(n + " É MULTIPLO DE:" + multiplo);
			}
		}
	}
}
