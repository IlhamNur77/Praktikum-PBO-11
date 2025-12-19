# Praktikum-PBO-11
ANALISIS README
Kode Awal Sebelum Refactoring

class OrderManager:
    def process_checkout(self, order, payment_method):
        if payment_method == "credit_card":
            ...
        elif payment_method == "bank_transfer":
            ...
        else:
            return False

        print("Mengirim notifikasi")
        order.status = "paid"

Pelanggaran SOLID
SRP (Single Responsibility Principle)
Satu class OrderManager memiliki banyak tanggung jawab:
- Mengelola checkout
- Memproses pembayaran
- Mengirim notifikasi
Seharusnya 1 class = 1 tanggung jawab

OCP (Open Closed Principle)
Jika ingin menambah metode pembayaran (misalnya QRIS), maka:
elif payment_method == "qris":
Kode lama harus diubah. Seharusnya cukup menambah class baru

DIP (Depedency Inversion Principle)
Order Manager bergantung pada:
- detail pembayaran
- detail notifikasi
Tidak bergantung pada abstrak(interface)

IMPLEMENTASI DIP & OCP
Maka solusi untuk menyelesaikannya dengan cara:
- Gunakan Interface (Abstract Base Class)
- Gunakan Dependency Injection
- Checkout tidak tahu detail metode pembayaran
