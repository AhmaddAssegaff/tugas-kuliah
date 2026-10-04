public class Lingkaran {
  int jariJari;

  double hitungLuas() {
    return 3.14 * this.jariJari * this.jariJari;
  }

  public static void main(String[] args) {
    Lingkaran lingkaran1 = new Lingkaran();
    lingkaran1.jariJari = 10;

    Lingkaran lingkaran2 = new Lingkaran();
    lingkaran2.jariJari = 5;

    System.out.println(lingkaran1.hitungLuas());
    System.out.println(lingkaran2.hitungLuas());
  }
}
