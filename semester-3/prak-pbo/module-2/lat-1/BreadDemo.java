public class BreadDemo {
  public static void main(String[] args) {
    Bread bread1 = new Bread();

    bread1.setColor("white");
    bread1.setTaste("enak");
    bread1.setWight(150);
    bread1.setPrice(100000);

    bread1.printBread();

    Bread bread2 = new Bread();

    bread2.setColor("black");
    bread2.setTaste("enak 2");
    bread2.setWight(10);
    bread2.setPrice(1000);

    bread2.printBread();

    Bread bread3 = new Bread();

    bread3.setColor("red");
    bread3.setTaste("enak 3");
    bread3.setWight(1);
    bread3.setPrice(100000);

    bread3.printBread();

    Bread bread4 = new Bread();

    bread4.setColor("red");
    bread4.setTaste("enak 3");
    bread4.setWight(1);
    bread4.setPrice(100000);

    bread4.printBread();
  }
}
