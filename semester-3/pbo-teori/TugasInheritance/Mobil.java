package TugasInheritance;

public class Mobil extends Kendaraan {
  int jumlahPintu;

  Mobil(String merk, int kecepatanMaks, int jumlahPintu) {
    super(merk, kecepatanMaks);
    this.jumlahPintu = jumlahPintu;
  }

  @Override
  void info() {
    super.info();
    System.out.println("Jumlah Pintu mobil: " + jumlahPintu);
  }

  @Override
  void jalan() {
    System.out.println("Mobil jalan Override di class Mobil.");
  }
}
