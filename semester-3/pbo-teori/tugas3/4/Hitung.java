public class Hitung {
  int tambah(int a, int b) {
    int hasil = a + b;
    System.out.println("hasil tambah dgn tipe data int : " + hasil);

    return hasil;
  }

  double tambah(double a, double b) {
    double hasil = a + b;
    System.out.println("hasil tambah dgn tipe data double : " + hasil);

    return hasil;
  }

  public static void main(String[] args) {
    Hitung hitung = new Hitung();

    hitung.tambah(5, 3);
    hitung.tambah(5.5, 5.3);
  }
}
