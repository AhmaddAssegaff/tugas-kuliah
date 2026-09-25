public class Bread {
  String color;
  String taste;
  int wight;
  double price;

  void setColor(String breadColor) {
    color = breadColor;
  }

  void setTaste(String breadTaste) {
    taste = breadTaste;
  }

  void setWight(int breadWight) {
    wight = breadWight;
  }

  void setPrice(double breadPrice) {
    price = breadPrice;
  }

  void printBread() {
    System.out.println("color: " + color);
    System.out.println("taste: " + taste);
    System.out.println("wight: " + wight);
    System.out.println("price: " + price);
  }
}
