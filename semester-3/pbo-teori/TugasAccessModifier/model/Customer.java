package TugasAccessModifier.model;

public class Customer {
  int idCustomer;
  String name;
  private double saldo;

  public Customer(int customerId, String name, double saldo) {
    this.idCustomer = customerId;
    this.name = name;
    this.saldo = saldo;
  }

  public void buyProduct(Product product, int quantity) {
    if (product.getStock() < quantity) {
      System.out.println("GAGAL: Stok produk tidak mencukupi");
      return;
    }

    double totalPrice = product.getPrice() * quantity;

    if (this.saldo < totalPrice) {
      System.out.println("Transaksi GAGAL: Saldo pembeli tidak mencukupi.");
      return;
    }

    this.saldo -= totalPrice;
    product.reduceStock(quantity);

    System.out.println("Transaksi BERHAkSIL!");
  }
}
