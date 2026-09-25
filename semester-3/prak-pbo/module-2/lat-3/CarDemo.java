public class CarDemo {
  public static void main(String[] args) {
    Car car1 = new Car();
    Car car2 = new Car();

    car1.setCadence(50);
    car1.setSpeed(200);
    car1.setGear(5);

    car2.setCadence(20);
    car2.setSpeed(20);
    car2.setGear(2);

    car1.printCar();
    car2.printCar();
  }
}
