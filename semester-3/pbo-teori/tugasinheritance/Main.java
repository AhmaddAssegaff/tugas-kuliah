package TugasInheritance;

public class Main {
  public static void main(String[] args) {
    Mobil mobil = new Mobil("Toyota", 200, 4);
    Motor motor = new Motor("Honda", 120, "4-tak");

    mobil.info();
    mobil.jalan();

    motor.info();
    motor.jalan();
  }
}
