package TugasAccessModifier.model;

public class Product {
  String name;
  private double price;
  private int stock;

  public Product(String name, double price, int stock) {
    this.name = name;
    this.price = price;
    this.stock = stock;
  }

  public double getPrice() {
    return price;
  }

  public int getStock() {
    return stock;
  }

  protected void reduceStock(int amount) {
    if (amount > 0 && amount <= this.stock) {
      this.stock -= amount;
    }
  }
}
