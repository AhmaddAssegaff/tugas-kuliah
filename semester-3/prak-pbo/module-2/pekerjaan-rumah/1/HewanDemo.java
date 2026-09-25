public class HewanDemo {
  public static void main(String[] args) {
    Hewan hewan1 = new Hewan();
    Hewan hewan2 = new Hewan();

    hewan1.setName("Harimau");
    hewan1.setJumlahKaki(4);
    hewan1.setMakanan("daging");
    hewan1.setHewanType("karnivora");

    hewan2.setName("kerbau");
    hewan2.setJumlahKaki(4);
    hewan2.setMakanan("rumput");
    hewan2.setHewanType("karnivora");

    hewan1.printHewan();
    hewan2.printHewan();
  }
}
