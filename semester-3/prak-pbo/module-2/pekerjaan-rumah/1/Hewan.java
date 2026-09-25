public class Hewan {
  String name;
  int jumlahKaki;
  String makanan;
  String hewanType;

  void setName(String nameHewan) {
    name = nameHewan;
  }

  void setJumlahKaki(int Kaki) {
    jumlahKaki = Kaki;
  }

  void setMakanan(String makananHewan) {
    makanan = makananHewan;
  }

  void setHewanType(String hewanT) {
    hewanType = hewanT;
  }

  void printHewan() {
    System.out.println("hewan name: " + name);
    System.out.println("hewan kaki: " + jumlahKaki);
    System.out.println("makanan: " + makanan);
    System.out.println("hewan type: " + hewanType);
  }
};
