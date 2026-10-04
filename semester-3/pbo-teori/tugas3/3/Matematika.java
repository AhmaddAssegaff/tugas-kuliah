public class Matematika {
  public void kali(int a, int b) {
    int hasil = a * b;
    System.out.println("hasil perkalian: " + hasil);
  }

  public static void tambah(int a, int b) {
    int hasil = a + b;
    System.out.println("Hasil pertambahan : " + hasil);
  }

  public static void main(String[] args) {
    tambah(1, 2);

    Matematika mtk = new Matematika();
    mtk.kali(1, 2);
  }
}
