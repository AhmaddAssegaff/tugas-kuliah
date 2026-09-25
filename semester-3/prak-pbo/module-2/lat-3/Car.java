public class Car {
  int cadence;
  int speed;
  int gear;

  void setCadence(int carCadence) {
    cadence = carCadence;
  }

  void setSpeed(int carSpeed) {
    speed = carSpeed;
  }

  void setGear(int carGear) {
    gear = carGear;
  }

  void printCar() {
    System.out.println("carCadence: " + cadence);
    System.out.println("carSpeed: " + speed);
    System.out.println("carGear: " + gear);
  }
}
