package bank;

public class Rekening {
  private String nama;
  private int noRekening;
  private double saldo;

  public Rekening(int noRekening, String nama, double saldo) {
    this.nama = nama;
    this.setNoRekening(noRekening);
    this.setSaldo(saldo);
  }

  public double getSaldo() {
    return this.saldo;
  }

  public void setSaldo(double saldo) {
    if (saldo >= 0) {
      this.saldo = saldo;
      return;
    }

    System.out.println("saldo tidak boleh di bawah nol");
  }

  public double getNoRekening() {
    return this.noRekening;
  }

  public void setNoRekening(int noRekening) {
    if (noRekening > 0) {
      this.noRekening = noRekening;
      return;
    }

    System.out.println("nomer rekening harus di atas nol");
  }

  protected void info() {
    System.out.println("nomer rekening: " + this.noRekening);
    System.out.println("nama : " + this.nama);
    System.out.println("saldo : " + this.saldo);
  }
}
