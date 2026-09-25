import java.util.Date;

public class Karyawan {
  String nama;
  String alamat;
  String jabatan;
  double gaji;

  public void setNama(String nama) {
    this.nama = nama;
  }

  public String getAlamat() {
    return alamat;
  }

  public String getJabatan() {
    return jabatan;
  }

  public double getGaji() {
    return gaji;
  }

  void printKaryawan() {
    System.out.println("nama :" + nama);
    System.out.println("alamat :" + alamat);
    System.out.println("jabatan :" + jabatan);
    System.out.println("gaji :" + gaji);
  }
}
