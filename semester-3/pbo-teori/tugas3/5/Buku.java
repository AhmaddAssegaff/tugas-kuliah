public class Buku {
  String judul;
  String penulis;
  static int jumlahBuku;

  Buku(String judul, String penulis) {
    this.judul = judul;
    this.penulis = penulis;
    jumlahBuku++;
  }

  static int getJumlahBuku() {
    return jumlahBuku;
  }

  public static void main(String[] args) {
    Buku buku1 = new Buku("buku1", "Ahmad");
    Buku buku2 = new Buku("buku2", "Ihsan");
    Buku buku3 = new Buku("buku3", "Abel");

    System.out.println("Jumlah buku: " + Buku.getJumlahBuku());
  }
}
