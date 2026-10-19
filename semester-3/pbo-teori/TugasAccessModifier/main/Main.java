package TugasAccessModifier.main;

import TugasAccessModifier.model.Customer;
import TugasAccessModifier.model.Product;

public class Main {
    public static void main(String[] args) {
        Product laptop = new Product("Laptop", 7500000, 3);

        Customer ahmad = new Customer(1, "Ahmad", 10000000);
        Customer ihsan = new Customer(1, "Ihsan", 2000000);

        ahmad.buyProduct(laptop, 1);
        ihsan.buyProduct(laptop, 1);
        ahmad.buyProduct(laptop, 5);
    }
}
