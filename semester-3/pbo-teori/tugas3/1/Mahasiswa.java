public class Mahasiswa {
  String nama;
  static String universitas = "UMS";

  public void tampilkanMahasiswa() {
    System.out.println("nama : " + nama);
    System.out.println("universitas : " + universitas);
  }

  public static void main(String[] args) {
    Mahasiswa mhs1 = new Mahasiswa();
    mhs1.nama = "Ahmad";

    Mahasiswa mhs2 = new Mahasiswa();
    mhs2.nama = "Ihsan";

    Mahasiswa mhs3 = new Mahasiswa();
    mhs3.nama = "Fathir";
    mhs3.universitas = "UMY";

    mhs1.tampilkanMahasiswa();
    mhs2.tampilkanMahasiswa();
    mhs3.tampilkanMahasiswa();
  }
}
