public class Mahasiswa {
  String nama;
  String nim;
  String alamat;
  int semester;

  public void setNama(String nama) {
    this.nama = nama;
  }

  public void setNim(String nim) {
    this.nim = nim;
  }

  public void setAlamat(String alamat) {
    this.alamat = alamat;
  }

  public void setSemester(int semester) {
    this.semester = semester;
  }

  void printMahasiswa() {
    System.out.println("nama" + nama);
    System.out.println("nim" + nim);
    System.out.println("alamat" + alamat);
    System.out.println("semester" + semester);
  }
}
