package bank;

public class RekeningBisnis extends Rekening {
  private String jenisRekening = "Bisnis";

  RekeningBisnis(int noRekening, String nama, double saldo) {
    super(noRekening, nama, saldo);
  }

  @Override
  protected void info() {
    super.info();
    System.out.println("jenis rekening : " + this.jenisRekening);
  }

  public String getJenisRekening() {
    return this.jenisRekening;
  }

  public void setJenisRekening(String jenisRekening) {
    if (jenisRekening == "Tabungan" || jenisRekening == "Bisnis") {
      this.jenisRekening = jenisRekening;
      return;
    }

    System.out.println("jenisRekening harus 'Tabungan' atau 'Bisnis'");
  }
}
