
Nama : Zhafira Richas

NPM : 2506540941

Kelas : PBP C

## TUGAS 1
1. Pada Tutorial dan Tugas 1, Anda diberi kebebasan untuk menentukan tampilan dari website portofolio Anda. Saat Anda merancang struktur HTML yang digunakan, apakah Anda menggunakan elemen semantik HTML5 seperti <section>, <article>, atau <aside>? Jika iya, bagaimana elemen tersebut membantu Anda dalam membuat static web? Jika tidak, mengapa tanpa elemen tersebut sudah memenuhi kebutuhan desain Anda?
Saya menggunakan <section> pada tiap bagian profile,skills, experiences, dan education. Kerna memudahkan dalam membagi bagian masing-masing dan terlihat rapi.

2. Ketika Anda mengatur CSS Anda agar tetap responsive, tantangan tata letak apa yang Anda temukan? Bagaimana Anda mengevaluasi elemen mana yang harus diubah posisinya atau diprioritaskan ukurannya saat berpindah dari tampilan desktop ke mobile?
Sejauh ini belum ada tantangan yang berarti karena saya hanya melanjutkan desing yg udah ada dengan sedikit perubahan layout pada section baru yang saya buat sendiri.

3. Website yang Anda buat saat ini adalah static web murni. Batasan apa yang Anda rasakan saat mencoba menyajikan informasi pada portofolio Anda secara optimal? Berdasarkan batasan tersebut, fungsionalitas dinamis apa yang paling ingin Anda persiapkan dan tambahkan pada iterasi proyek selanjutnya?
Sejauh ini batasan dalam web static, tidak menghambat pembuatan web portofolio ini. Mungkin juga dari saya yang belum mengerti betul materi. Untuk fungsionalis dinamis yang ingin saya persiapkan pastinya saya ingin menambahkan pada section project agar lebih interkatif. 

Untuk penggunaan Gen Ai, saya menggunakan Gemini untuk keperluan memahami css pada template yg sudah ada pada tutorial 1 dan dengan manual saya mengimplementasikannya pada section-section yang baru dengan sepemahaman saya.

### Tugas 2

1. Jelaskan alur yang terjadi ketika pengguna membuka halaman portofolio baru, mulai dari permintaan yang diterima proyek hingga data ditampilkan pada browser. Dalam jawabanmu, jelaskan peran urls.py proyek, urls.py aplikasi, view, model, dan template.

Ketika pengguna membuka halaman portofolio baru, siklus permintaan  pada Django melewati beberapa tahapan hingga data ditampilkan di browser:
Pengguna mengirimkan Request dan Pengguna memasukkan URL.
Project urls.py, Django memeriksa URL yang masuk melalui berkas urls.py di tingkat proyek. Berkas ini berfungsi sebagai peta besar yang mengarahkan bagian awal URL ke aplikasi Django yang bersangkutan.
App urls.py , Setelah diarahkan ke aplikasi tertentu, Django mencocokkan sisa pola URL dengan aturan di dalam urls.py milik aplikasi tersebut untuk menentukan fungsi atau kelas view mana yang harus dipanggil.
View, View menerima request tersebut dan bertindak sebagai jembatan. View memanggil model untuk mengambil data yang diperlukan dari database, lalu memproses logika bisnis sebelum mengirimkannya ke template.
Model, Berdasarkan instruksi view, model berinteraksi dengan database melalui Django ORM (Object-Relational Mapping) untuk mengambil data portofolio baru yang diminta.
Template, View menggabungkan data yang diperoleh dari model ke dalam template (berkas HTML yang dipadukan dengan Django Template Language). Template merender data tersebut menjadi struktur visual halaman web.
Response ke Browser, Django mengirimkan hasil akhir rendering template kembali ke browser pengguna dalam bentuk HTTP Response, dan halaman portofolio baru pun tampil.

2. Mengapa data untuk bagian portofolio baru sebaiknya disimpan pada model dan tidak ditulis langsung di dalam template? Jelaskan dampaknya terhadap kemudahan pemeliharaan dan pengembangan aplikasi.

Menulis data secara langsung (hardcode) di dalam template HTML melanggar prinsip Separation of Concerns (pemisahan antara logika/data dan tampilan). Penyimpanan data pada model memberikan dampak signifikan terhadap aspek pemeliharaan dan pengembangan.
Kemudahan Pemeliharaan, jika  setiap kali ada penambahan, perubahan deskripsi, atau pembaruan gambar, maka harus membuka dan mengubah kode file HTML secara manual. Kalo menggunakan model, data dikelola secara terpusat di database. Pembaruan data bahkan dapat dilakukan melalui antarmuka Django Admin. Model memungkinkan data dikelola secara dinamis. Anda bisa dengan mudah melakukan filtering, sorting, pencarian pada data portofolio. Selain itu, data yang sama di dalam model dapat digunakan kembali (reusable) di berbagai halaman berbeda.

3. Apa perbedaan fungsi makemigrations dan migrate pada Django? Berikan contoh perubahan model yang mengharuskanmu menjalankan kedua perintah tersebut.
makemigrations, berfungsi untuk mendeteksi perubahan yang Anda lakukan pada berkas models.py dan menerjemahkannya ke dalam bentuk berkas skrip migrasi baru. Perintah ini belum mengubah struktur tabel di dalam database fisik, melainkan baru membuat rancangan atau blueprint-nya saja.
migrate, berfungsi untuk membaca berkas-berkas skrip migrasi yang belum diterapkan dan mengeksekusi perintah SQL yang sesuai ke dalam database aktual. Perintah inilah yang secara nyata membuat, mengubah, atau memperbarui tabel-tabel di dalam database agar sinkron dengan model Python Anda.

Untuk penggunaan AI pada tugas kali ini sangat sedikit, saya meminta ai untuk menjelaskan tentang pertanyaan refleksi yang menurut saya kurang saya pahami sehingga bisa saya pahami lebih dalam. Untuk penambahan model dan test pada tugas ini saya hanya memodifikasi pada model experience dan tutorial 2 tanpa menggunakan AI.
