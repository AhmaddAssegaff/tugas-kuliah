package TugasInheritance;

public class Motor extends Kendaraan {
  String jenisMesin;

  Motor(String merk, int kecepatanMaks, String jenisMesin) {
    super(merk, kecepatanMaks);
    this.jenisMesin = jenisMesin;
  }

  @Override
  void jalan() {
    System.out.println("Motor jalan Override di class Motor.");
  }
}
