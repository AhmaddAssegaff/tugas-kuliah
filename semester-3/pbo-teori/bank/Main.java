package bank;

public class Main {
  public static void main(String[] args) {
    System.out.println("Nama: Ahmad, NIM: L200250034");

    RekeningTabungan RekTabunganAhmad = new RekeningTabungan(1, "Ahmad", 100000);
    RekeningBisnis RekBisnisAhmad = new RekeningBisnis(2, "Ahmad", 200000);

    RekeningTabungan RekTabunganFahri = new RekeningTabungan(3, "Fahri", 300000);
    RekeningBisnis RekBisnisFahri = new RekeningBisnis(4, "Fahri", 400000);

    RekTabunganAhmad.info();
    RekTabunganAhmad.setJenisRekening("tidak valid");

    RekBisnisAhmad.info();
    RekBisnisAhmad.setNoRekening(0);

    RekTabunganFahri.info();
    RekTabunganFahri.setSaldo(-1);

    RekBisnisFahri.setSaldo(100000);
    RekBisnisFahri.info();
  }
}
