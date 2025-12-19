# Refactoring Sistem Checkout Menggunakan Prinsip SOLID

## 1. Pendahuluan

Dokumen ini disusun sebagai bagian dari **Latihan Mandiri Refactoring** dengan tujuan menerapkan prinsip **SOLID** pada sebuah studi kasus pemrograman berorientasi objek. Studi kasus yang digunakan adalah **Sistem Checkout dan Pembayaran**, di mana pada kode awal terdapat pelanggaran terhadap prinsip **Single Responsibility Principle (SRP)**, **Open Closed Principle (OCP)**, dan **Dependency Inversion Principle (DIP)**.

Refactoring dilakukan untuk meningkatkan kualitas desain kode, keterbacaan, kemudahan pemeliharaan, serta fleksibilitas dalam pengembangan fitur di masa mendatang.

---

## 2. Deskripsi Kode Awal

Pada implementasi awal, sistem memiliki sebuah class bernama `OrderManager` yang bertanggung jawab untuk:

1. Memproses checkout
2. Menentukan metode pembayaran menggunakan struktur `if/else`
3. Mengirim notifikasi kepada pelanggan

Seluruh logika tersebut diletakkan dalam satu method `process_checkout()`.

---

## 3. Analisis Pelanggaran Prinsip SOLID

### 3.1 Pelanggaran Single Responsibility Principle (SRP)

Single Responsibility Principle menyatakan bahwa sebuah class seharusnya hanya memiliki **satu alasan untuk berubah**. Namun pada kode awal:

* `OrderManager` menangani logika checkout
* Mengatur proses pembayaran
* Mengelola pengiriman notifikasi

Hal ini menyebabkan satu class memiliki lebih dari satu tanggung jawab, sehingga melanggar prinsip SRP.

---

### 3.2 Pelanggaran Open Closed Principle (OCP)

Open Closed Principle menyatakan bahwa sebuah modul harus **terbuka untuk ekstensi tetapi tertutup untuk modifikasi**. Pada kode awal, penambahan metode pembayaran baru (misalnya QRIS) mengharuskan perubahan langsung pada struktur `if/else` di dalam method `process_checkout()`.

Akibatnya, setiap penambahan fitur baru akan meningkatkan risiko bug dan memperbesar ketergantungan antar bagian kode.

---

### 3.3 Pelanggaran Dependency Inversion Principle (DIP)

Dependency Inversion Principle menyatakan bahwa modul tingkat tinggi tidak boleh bergantung pada modul tingkat rendah, melainkan pada abstraksi. Pada kode awal:

* `OrderManager` bergantung langsung pada detail implementasi metode pembayaran
* Tidak terdapat interface atau abstraksi sebagai kontrak

Hal ini menyebabkan kode sulit diuji dan tidak fleksibel terhadap perubahan implementasi.

---

## 4. Implementasi Refactoring

### 4.1 Penerapan Dependency Inversion Principle (DIP)

Untuk menerapkan DIP, dibuat abstraksi berupa interface:

* `IPaymentProcessor` sebagai kontrak untuk semua metode pembayaran
* `INotificationService` sebagai kontrak untuk layanan notifikasi

Class tingkat tinggi (`CheckoutService`) hanya bergantung pada abstraksi tersebut, bukan pada implementasi konkret.

---

### 4.2 Penerapan Open Closed Principle (OCP)

Dengan adanya interface `IPaymentProcessor`, sistem dapat diperluas dengan menambahkan metode pembayaran baru (contoh: QRIS) tanpa mengubah kode pada class `CheckoutService`.

Penambahan fitur dilakukan dengan membuat class baru yang mengimplementasikan interface yang sama.

---

### 4.3 Penerapan Single Responsibility Principle (SRP)

Setelah refactoring, tanggung jawab sistem dipisahkan sebagai berikut:

* `CheckoutService`: Mengkoordinasikan proses checkout
* `PaymentProcessor`: Menangani proses pembayaran
* `NotificationService`: Menangani pengiriman notifikasi

Dengan pemisahan ini, setiap class memiliki satu tanggung jawab yang jelas.

---

## 5. Pembuktian Open Closed Principle (Challenge)

Sebagai pembuktian OCP, ditambahkan metode pembayaran baru yaitu **QRIS** dengan membuat class `QrisProcessor` yang mengimplementasikan `IPaymentProcessor`.

Penambahan ini tidak memerlukan perubahan apa pun pada class `CheckoutService`, sehingga membuktikan bahwa sistem telah memenuhi prinsip OCP.

---

## 6. Kesimpulan

Berdasarkan hasil refactoring yang telah dilakukan, dapat disimpulkan bahwa:

1. Prinsip **SRP** terpenuhi dengan memisahkan tanggung jawab setiap class
2. Prinsip **OCP** terpenuhi karena sistem dapat dikembangkan tanpa memodifikasi kode yang sudah ada
3. Prinsip **DIP** terpenuhi dengan penggunaan abstraksi dan dependency injection

Penerapan prinsip SOLID terbukti mampu meningkatkan kualitas desain sistem serta mempermudah pengembangan dan pemeliharaan kode di masa depan.

---

## 7. Penutup

Dokumen ini diharapkan dapat menjadi referensi akademik dalam memahami penerapan refactoring berbasis prinsip SOLID pada pemrograman berorientasi objek, khususnya dalam bahasa Python.
