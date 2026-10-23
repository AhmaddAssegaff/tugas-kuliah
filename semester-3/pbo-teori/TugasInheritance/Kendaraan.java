package TugasInheritance;

public class Kendaraan {
  String merk;
  int kecepatanMaks;

  Kendaraan(String merk, int kecepatanMaks) {
    this.merk = merk;
    this.kecepatanMaks = kecepatanMaks;
  }

  void info() {
    System.out.println("Merk: " + merk);
    System.out.println("Kecepatan Maksimal: " + kecepatanMaks + " km/jam");
  }

  void jalan() {
    System.out.println("Kendaraan berjalan.");
  }
}
