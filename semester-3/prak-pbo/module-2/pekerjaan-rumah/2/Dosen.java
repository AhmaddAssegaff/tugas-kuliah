import java.util.Date;

public class Dosen {
  String nama;
  int nik;
  String pendidik;
  Date tglLahir;

  public void setNama(String nama) {
    this.nama = nama;
  }

  public void setNik(int nik) {
    this.nik = nik;
  }

  public void setPendidik(String pendidik) {
    this.pendidik = pendidik;
  }

  public void setTglLahir(Date tglLahir) {
    this.tglLahir = tglLahir;
  }

  void printDosen() {
    System.out.println("nama :" + nama);
    System.out.println("nik" + nik);
    System.out.println("pendidik" + pendidik);
    System.out.println("tglLahir" + tglLahir);
  }
}
