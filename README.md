# Laporan Proyek Machine Learning - Feivel Jethro Ezhekiel
![Gambar Buku](Assets/Gambar_buku/vecteezy_whimsical-book-stack-with-hot-air-balloons_51064729.jpg)
## Project Overview

Proyek ini merupakan Kecerdasan Buatan berbentuk Sistem Rekomendasi berdasarkan penulis/author menggunakan data yang mencakup informasi tentan judul buku, penulis, tahun terbit, ISBN, dan rating pengguna. Pembaca/user diberikan 10 rekomendasi menggunakan 2 teknik pendekatan, `Content Based Filtering` dan `Collaborative Filtering`. Adapula `Content Based Filtering` merupakan rekomendasi berdasarkan kesamaan konten atau produk yang ada dengan kesamaan item dengan preferensi pengguna, sedangkan `Collaborative Filtering` menggunakan pola perilaku user lain yang memiliki kesamaan perilaku berdasarkan konten/produk yang mereka sukai.

**Rubrik Tambahan**:
- Berdasarkan riset dari Yale School of Publich Health menemukan bahwa mereka yang meluangkan waktunya untuk membaca buku 30 menit setiap harinya dalam setahun memiliki umur lebih panjang 2 tahun dibandingkan mereka yang tidak pernah membaca. Kemudian menurut Specktor (2018) membaca membuat orang sang pembaca menjadi seseorang yang lebih baik karena menjadikannya seorang yang berempati dan memiliki kecerdasan emosional yang baik. Bahkan menurut Erasmus (2018) membaca dapat menurunkan stress dan mencerdasan dalam jangka watu yang panjang karena menstimulasi otak dan meningkatkan fungsi memori otak. 
- Penelitian yang dilakukan oleh Tulgan (2018) menjelaskan bahwa Gen-Z memiliki *critical thinking* yang buruk dikarenakan ketergantungan mereka terhadap gadget mereka sebagai sumber informasi dan kecepatannya mengakibatkan generasi ini tidak dapat *berpikir diatas kaki sendiri* karena jawaban yang disuguhkan secara cepat oleh internet, bukannya pengalaman mereka sendiri dalam mencari jawaban dengan **kedalaman berpikir** untuk menyelesaikan sebuah masalah.
- PISA(Programme for International Student Assessment) adalah studi internasional yang mengukur kemampuan pelajar di seluruh dunia pada umur 15 tahun yang melambangkan Sumber Daya Manusia(SDM) dari negara tersebut. Penyelenggara tes ini adalah Organisation for Economic Co-operation and Development (OECD) yang terdiri dari negara-negara maju dan berkembang yang memiliki tujuan meningkatkan kesejahteraan ekonomi dan sosial. Tes PISA ini dilakukan setiap 3 tahun sekali. Tes ini mencakup tiga kategori utama:
  - Matematika : Menguji kemampuan siswa dalam menerapkan konsep matematika untuk memecahkan masalah sehari-hari.
  - Membaca : Menilai kemampuan siswa untuk memahami dan menggunakan informasi dari teks tertulis dalam berbagai konteks.
  - Sains : Mengukur pemahaman siswa tentang konsep ilmiah dan kemampuan mereka menerapkan ilmu pengetahuan dalam situasi nyata.
- Skor PISA Indonesia ada dimana? Menurut artikel Detik.com, skor PISA Indonesia sejak tahun 2000(pertama kali dilakukan studi ini) termasuk ke kategori rendah. Skor Indonesia pada tahun 2022 adalah 359, skor matematika 366, dan skor sains 396. Hasil ini menjadikan negara Indonesia berada diperingkat ke-69 dari 80 negara yang berpartisipasi.
![Gambar Skor PISA tahun 2022](https://cdn.gnfi.net/goodstats/uploads/images/15189/September/s__Pisa.png)

  
  
Referensi: 
- [EXPLORING READING ISSUES AMONG MILLENNIALS AND GENZ](https://www.researchgate.net/publication/329814876_EXPLORING_READING_ISSUES_AMONG_MILLENNIALS_AND_GENZ) 
- [Skor PISA Indonesia Ditarget Setara Negara OECD, Diaspora RI Usul Belajar Ini](https://www.detik.com/edu/sekolah/d-7695294/skor-pisa-indonesia-ditarget-setara-negara-oecd-diaspora-ri-usul-belajar-ini)
- [Skor PISA: Acuan Kualitas SDM Negara](https://s1pbing.fbs.unesa.ac.id/post/skor-pisa-acuan-kualitas-sdm-negara)
- [Posisi Indonesia di PISA 2022, Siapkah untuk 2025?](https://goodstats.id/article/posisi-indonesia-di-pisa-2022-siapkah-untuk-2025-6RLyK)
- [Narasi Skor PISA Indonesia Jangan Seolah-olah Prestasi](https://www.kompas.id/baca/humaniora/2023/12/06/narasi-skor-pisa-indonesia-jangan-seolah-olah-prestasi)

## Business Understanding

Kemampuan membaca generasi muda Indonesia berada dibawah rata-rata dunia. Hal ini tergambarkan dari skor PISA kita yang masih rendah pada kriteria soal matematika, membaca, dan sains. Memangnya skor PISA dapat mencerminkan apa? Berdasarkan artikel yang dikeluarkan oleh Universitas Negeri Surabaya, skor PISA dijadikan acuan oleh negara-negara sebagai indikator kualitas SDM Negara. Skor PISA yang sering dijadikan acuan karena beberapa alasan berikut :
  1. Indikator Esensial
  2. Komparatif Antarnegara
  3. Prediktor Masa Depan SDM
  4. Dasar Pengambilan Kebijakan Pendidikan

Oleh karena itu, Rendahnya minat baca generasi muda di Indonesia
Hal ini berkontribusi terhadap rendahnya skor PISA Indonesia dibandingkan negara Asia Tenggara lainnya.

### Problem Statements
Teknologi yang terus berkembang dan *gadget* yang menjadi benda yang selalu digenggam oleh generasi muda Indonesia atau disebut Handphone Pintar, ternyata tidak cukup pintar untuk meningkatkan minat baca mereka. Beberapa penyebab dari kurangnya minat baca generasi muda di Indonesia adalah :
- Buku tidak sesuai minat/kebutuhan pembaca 
- Kurangnya sistem personalisasi dalam penyajian konten literasi

### Goals

![Teen Reading a Book](https://newsone.com/wp-content/uploads/sites/22/2022/08/16600434609052.jpg?strip=all&quality=80)

Permasalahan diatas dapat diatasi dengan salah satu teknologi AI dimana tujuannya adalah :
- **Meningkatkan minat baca dan keterlibatan generasi muda Indonesia**
Hal ini dapat dicapai dengan menciptakan sebuah sistem yang dapat mengenali dan melakukan personalisasi minat setiap anak melalui perangkat pintar mereka masing-masing yang disebut Recommendation System.
- **Mengembangkan Recommendation System Buku**
Sistem rekomendasi ini dibangun untuk meningkatkan personalisasi dan rekomendasi buku berdasarkan interaksi anak muda dengan buku-buku yang pernah dibaca maupun dengan pengguna lainnya.

**Rubrik Tambahan**:

![Ilustrasi Metode Sistem Rekomendasi](https://lh4.googleusercontent.com/0NoiKF9NDEM0_daE0Wwfmyq9Z5sRCMIoNM0Fst-JJr9Hi0dG7PSSZeUM_Xok3lW762UbDYit8bCz_p8vZ7rJO9XuSKbRyUPFk_gTIgA2G2i_PmknJUc8l91nB-Stx77z1tMxtFsxIOpjXh0bAenftLfk6KqMXJoA9SOhcd8lKQf1ZWev7gL2gOaaZf7wsw)

Untuk mencapai goals tersebut kita perlu menemukan pendekatan solusi kecerdasan buatan dengan metode tertentu yang diantaranya adalah :
  ### Content Based Filtering
  Metode ini merupakan salah satu metode rekomendasi dimana sistem akan menggunakan karakteristik atau sifat dari item/produk yang nantinnya akan dijadikan landasan atau basis dalam rekomendasi kepada user. Secara umum Content-Based Filtering menggunakan 2 teknik umum dalam membuat rekomendasi, *heuristic-based* dan *model-based*. Untuk detailnya adalah sebagai berikut :
  #### *Heuristic-based*
  - Cosine Similarity
  - Boolean Query
  - TF-IDF
  - Clustering
  #### *Model-based*
  - Bayesian Classifier & Clustering
  - Decision Tree
  - Artificial Neural Network
  ### Collaborative Filtering
  Metode ini paling populer digunakan saat ini. Banyak penelitian yang membahas tentang teknik ini karena beberapa keunggulannya seperti: menghasilkan serendipity(tak terduga) item, sesuai trend market, mudah diimplementasikan dan memumgkinkan diterapkan pada beberapa domain (book, movies, music, dll). Cara kerja metode ini adalah mencari kesamaan data antar pengguna dengan memanfaatkan data komunitas dimana pengguna yang memiliki preferensi yang sama di masa lalu cenderung memiliki preferensi yang sama dimasa depan.


## Data Understanding
-  Sumber Data : [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset/data)

Dataset diambil dari Kaggle merupakan dataset yang bertujuan menciptakan sistem rekomendasi berbasis data User, data Buku seperti ISBN, judul, penulis, dan penerbit, serta data rating yang berisi jumlah rating user terhadap item buku.

- Jumlah baris dan kolom
Dataset tersebut memiliki 3 file yang bernama `Books.csv`,`Ratings.csv`, dan `Users.csv`. 
  - Books.csv memiliki 271360 baris dan 8 kolom
  - Ratings.csv memiliki 1149780 baris dan 3 kolom
  - Users.csv memiliki 278858 baris dan 3 kolom

- Kondisi Data
  - Pertama, pada `Books.csv` 3 kolom/fitur yang tidak berpengaruh pada sistem rekomendasi, terdapat 4 data yang mengalami **missing values** yang berada pada fitur *Book-Author* dan *Publisher*. Judul fitur juga tidak rapih, sehingga pada fitur Book-Author, Year-Of-Publication, dan Book-Title diganti menjadi book_author, YoP, dan book_title.
  - Kedua, `Ratings.csv` tidak terdapat **missing values**, tidak terdapat **duplicated data**, dan semua fitur penting untuk sistem rekomendasi sehingga datanya cukup bersih.
  - Ketiga, `Users.csv` memiliki 110.762 data yang mengalami `missing values` pada kolom **Age** dan daftar lokasi yang tidak rapih. Selebihnya data tersebut cukup bersih dan dapat ditindaklanjuti.

  - Jumlah data yang didapatkan dari data pada dataset diatas adalah :
    - 271.360 baris dengan 8 kolom pada `Books.csv`
    - 1.149.780 dengan 3 kolom pada `Ratings.csv`
    - dan 278.858 dengan 3 kolom pada `Users.csv`

- Uraian Seluruh Fitur Pada Data

  Variabel-variabel pada `Books.csv`:
  | **Variabel**         | **Deskripsi**                                                                                              |
  |----------------------|------------------------------------------------------------------------------------------------------------|
  | **Users ID**          | ID user yang telah dimapping dan dianomalisasi menjadi data integer.                                        |
  | **Location**          | Lokasi user dari negara, negara bagian, dan nama desa.                                                     |
  | **Age**               | Umur dari user.                                                                                             |
  | **Book_Title**        | Judul buku yang telah dibaca.                                                                                |
  | **Book_Author**       | Penulis dari buku tersebut.                                                                                  |
  | **ISBN**              | Nomor identifikasi buku. Setiap buku dengan judul yang sama, tetapi memiliki penerbit atau tahun rilis yang berbeda memiliki ISBN yang berbeda. |
  | **Year of Publication** | Tahun terbit dari buku tersebut.                                                                            |
  | **Publisher**         | Penerbit dari buku tersebut.                                                                                 |
  | **Image-URL-S**       | Gambar cover buku tersebut dengan ukuran Small.                                                              |
  | **Image-URL-M**       | Gambar cover buku tersebut dengan ukuran Medium.                                                             |
  | **Image-URL-L**       | Gambar cover buku tersebut dengan ukuran Large.                                                              |
  | **Book-Rating**       | Hasil ulasan buku dari user dengan rentang 0 hingga 10.                                                      |

  Uraian pada `Ratings.csv`

  | **Variabel**    | **Deskripsi**                                                                                                                    |
  | --------------- | -------------------------------------------------------------------------------------------------------------------------------- |
  | **User-ID**     | ID unik dari setiap pengguna yang memberikan rating.                                                                             |
  | **ISBN**        | Nomor identifikasi buku. Setiap buku dengan judul yang sama namun penerbit atau tahun terbit berbeda akan memiliki ISBN berbeda. |
  | **Book-Rating** | Nilai rating yang diberikan oleh user untuk buku tertentu, biasanya dalam rentang 1 hingga 5.                                    |

  Uraian pada `Users.csv`

  | **Variabel** | **Deskripsi**                                                                                   |
  | ------------ | ----------------------------------------------------------------------------------------------- |
  | **User-ID**  | ID unik untuk setiap pengguna yang telah dianonimkan menjadi data integer.                      |
  | **Location** | Lokasi pengguna yang terdiri dari negara, negara bagian, dan kota/desa, dipisahkan oleh koma.   |
  | **Age**      | Umur pengguna. |

- Apabila divisualisasikan terhadap data penulis buku, terdapat 10 nama penulis yang memiliki jumlah buku paling banyak atau dengan kata lain produktif.
![top 10 penulis](Assets/Prolific%20Authors.png)

  Pada data tersebut terlihat bahwa Agatha Christie merupakan Penulis paling produktif diantara semua penulis di dataset tersebut disusul oleh William Shakespeare dan Stephen King.
- Kemudian melihat persebaran data dari rating buku dapat dilihat pada visualisasi berikut.
![Rating buku](/Assets/book_rating.png)
  Dapat dilihat bahwa lebih banyak data user yang tidak memberikan rating alias bintang 0(dari 10).
- Lalu distribusi tahun terbit dari dataset ditampilkan seperti berikut
![Year Publication Distribution](/Assets/distribution_year.png)
Terlihat bahwa terdapat data yang bukunya tidak diketahui tahun terbitnya.

**Rubrik Tambahan**:
Untuk memahami data, perlu dilakukan **`Exploratory Data Analysis(EDA)`**. Tahapan ini cukup penting untuk memahami konteks dari data yang ada seperti bentuk data, jumlah data, dan juga isi dari data itu sendiri. Adapula detail dari EDA yang dilakukan pada project ini akan dijelaskan pada bagian [Perisapan Data](#data-preparation)

## Data Preparation
![Data Clean Illustration](https://sp-ao.shortpixel.ai/client/to_auto,q_lossy,ret_img,w_1595/https://mammoth.io/wp-content/uploads/2024/02/data-preparation-with-mammoth.jpg)

Pada tahap ini kita melakukan EDA dengan detail sebagai berikut:
Pada ketiga dataset, diawal kita melakukan `drop_duplicates()` untuk menghilangkan data duplikat.
### Data Preperation pada `df_books.csv`
- Menghapus duplicated data
Terdapat duplicated data pada ketika dataset dan silakukan diawal proses EDA.
- Penghapusan fitur
Pada dataset books.csv terdapat fitur yang tidak diperlukan untuk proses training sistem rekomendasi, sehingga dapat dihapus, seperti gambar novel yang berukuran M, S, dan L. Apabila diperlukan untuk visualisasi tidak apa-apa, tetapi dalam projeck ini tidak diperlukan dalam proses training model sehingga kita dapat melakukan `drop` kolom tersebut.
- Mengatasi Missing Values
Terdapat 2 missing values pada kolom publisher dan Book-Author. Dengan jumlah yang sedikit maka dapat diterapkan dropna.
- Mengganti nama fitur
Pada books.csv dilakukan rename fitur hal ini dikarenakan format penulisan yang sulit diproses ketika diproses ke tahap selanjutnya membuat penggantian nama perlu dilakukan dengan fungsi `.rename()`
- Features Selection
Fitur yang paling penting dipilih dan digunakan untuk proses training selanjutnya adalah ISBN, judul buku, nama penulis, dan tahun terbit buku.
### Data Preperation pada `df_ratings.csv`
- Mengganti nama fitur
Pada dataset df_ratings.csv terdapat karakter pada nama fitur yang perlu diganti agar pemrosesan data lebih cepat tanpa kendala maka perlu dilakukan operasi 'rename'.
Setelah dilakukan pengecekan, ternyata dataset df_ratings.csv cukup bersih tanpa ada missing values, duplicated data, dan featuresnya memiliki bobot untuk pembangunan sistem rekomendasi.

### Data preperation pada `df_users.csv`
dataset ini memiliki 3 kolom, **User-ID**, **Location**, dan **Age**
- Menghapus missin values
pada kolom **Age** terdapat 110762 data user yang belum memiliki data. Dengan jumlah sebanyak itu, akan disayangkan apabila kita menghapusnya semua dengan metode dropna. Maka kita dapat mengisinya dengan betode Group-by Location dimana kecenderungan di wilayah *A* memiliki rata-rata umur *X* tahun, maka data yang kosong apabila berada di wilayah *A* maka akan diisi dengan umur *X* tahun.
- Pembenahan isi data Location
Ketika dilihat lebih dalam, ternyata data lokasi user memiliki inputan yang tidak seragam dan cenderung redundan, seperti USA, US, America, United States, dll. Maka dari itu user melakukan manipulasi data dengan Regex dimana hanya mengambil negaranya saja.
- Pemilihan Features

### TF-IDF
Terakhir adalah dengan menerapkan TF-IDF, metode statistik untuk mengukur kepentingan suatu kata dalam dokumen terhadap dokumen lainnya. Pada Content-based filtering kita menggunakan ini agar dapat mengukur seberapa penting sebuah judul atau penulis dari sebuah dataset relatif terhadap kumpulin data lainnya pada dataset tersebut. Cara menghitungnya dengan menghitung frekuensi kemunculan suatu kata dalam dokumen tersebut. Kedua dengan menghitung Inverse Document Frequency, yaitu rasio antara jumlah dokumen dan jumlah dokumen yang mengandung kata tersebut.

Tahapan ini juga dilakukan untuk mempermudah proses pembuatan model sistem rekomendasi. Pada tahapan pertama dilakukan sampling, mengambil sebagian data dari keseluruhan dataset, sebanyak 10.000 data pertama. Hal ini dikarenakan dataset yang dimiliki terlampau banyak dan dapat mengakibatkan kepenuhan memory dan menghentikan proses modeling. Kedua, ketiga data dilakukan merge Books.csv dan Ratings.csv dengan menggabungkan data ISBN dan metode `left`. Kemudian dataframe tersebut diubah menjadi `.to_list()`.

**Rubrik Tambahan**: 
- `Sampling` : Mengambil sebagian data(10.000 baris pertama) dari keseluruhan dataset.
- `Merge` : menggunakan metode left join, menggabungkan dataframe berdasarkan kolom kunci(key) dan mempertahankan sisi kiri meskipun tidak ada pasangan yang cocok di dataframe sebelah kanan. Ini penting agar setiap interaksi user (misal: rating) punya konteks lengkap (misalnya judul buku, genre). Bisa menghasilkan fitur gabungan (misalnya rating buku berdasarkan genre, usia user, dsb). Model punya representasi lengkap terhadap relasi user–item.
- `Series to List` : Proses mengubah object series menjadi list menggunakan metode .to_list() yang sudah disediakan oleh library pandas. Tujuannya adalah untuk mempersiapkan data sebelum masuk ke proses modeling yang melatih data berbasis list seperti sklearn dan operasi matrix yang akan kita lakukan dalam membangun sistem rekomendasi.

## Model & Results
Pada tahap ini, dilakukan proses pembangunan dan evaluasi model sistem rekomendasi buku untuk mendorong peningkatan minat baca generasi muda Indonesia. Sistem rekomendasi ini dibangun menggunakan dua pendekatan utama: **Content-Based Filtering** dan **Collaborative Filtering**, kemudian disajikan dalam bentuk Top-10 Recommendation sebagai output yang dipersonalisasi untuk setiap pengguna.

### **Content-Based Filtering**
Content-Based Filtering merekomendasikan buku berdasarkan kemiripan konten dengan buku yang sebelumnya disukai atau dibaca oleh pengguna. Fitur-fitur konten yang digunakan antara lain:
- Penulis

Model ini memanfaatkan teknik seperti:
- TF-IDF Vectorization pada nama Penulis
- Cosine Similarity untuk mengukur kemiripan antar penulis

1. Menggunakan metode `cosine similarity`, yaitu teknik untuk mengukur kesamaan antara dua vektor berdasarkan sudut di antara mereka. Pada proyek ini, library **sklearn.metrics.pairwise** digunakan untuk menghitung `cosine similarity`.
2. Fungsi `author_recommendations()` digunakan untuk memberikan rekomendasi berdasarkan kesamaan penulis **(Book-Author)**. Fungsi ini kemungkinan mengambil nama penulis sebagai input dan mengembalikan buku-buku lain dari penulis yang sama atau penulis dengan profil serupa.

Hasil dari pembuatan model untuk Content-Based Filtering ditunjukkan dengan top N rekomendasi berikut:

**Rekomendasi dengan buku yang pernah dibaca adalah "The Diaries of Adam and Eve"**
| No | Book Title                                         | Book Author |
|-------|----------------------------------------------------|-------------|
| 1     | The Adventures of Tom Sawyer                       | Mark Twain  |
| 2     | The Adventures of Tom Sawyer                       | Mark Twain  |
| 3     | A Connecticut Yankee in King Arthur's Court (D...  | Mark Twain  |
| 4     | A Connecticut Yankee in King Arthur's Court        | Mark Twain  |
| 5     | A Connecticut Yankee in King Arthur's Court        | Mark Twain  |
| 6     | A Connecticut Yankee in King Arthur's Court        | Mark Twain  |
| 7     | A Connecticut Yankee in King Arthur's Court        | Mark Twain  |
| 8     | Treasury of Illustrated Classics: Adventures o...  | Mark Twain  |
| 9     | The Adventures of Tom Sawyer                       | Mark Twain  |
| 10     | The Adventures of Tom Sawyer                       | Mark Twain  |


### **Collaborative Filtering**
Collaborative Filtering merekomendasikan buku berdasarkan perilaku pengguna lain yang memiliki kesamaan preferensi. Model ini tidak melihat konten buku, tetapi menggunakan data seperti:
- Histori pembacaan
- Interaksi pengguna terhadap buku seperti pemberian rating

Model dibangun dengan pendekatan:
- User-based Collaborative Filtering → Kemiripan antar pengguna
- Item-based Collaborative Filtering → Kemiripan antar buku berdasarkan pengguna yang menyukai/penulis yang sama

1. Library `Surprise`, `Tensorflow`, dan `Keras` digunakan untuk membangun model rekomendasi berbasis collaborative filtering. Dataset yang digunakan terdiri dari df_ratings yang berisi informasi rating dari pengguna terhadap buku. Ini merupakan data interaksi user-item. 
2. Model dibangun dengan kelas `RecommenderNet` untuk melatih Neural Network. **Embedding** adalah cara untuk mengubah ID pengguna dan ID restoran menjadi vektor numerik yang lebih kecil dan lebih mudah dikelola. Vektor ini menangkap informasi penting tentang pengguna dan restoran.
Setiap pengguna dan restoran diwakili oleh vektor yang memiliki ukuran tetap (ditentukan oleh embedding_size). Selain embedding, model juga mempertimbangkan bias untuk setiap pengguna dan restoran. Bias ini membantu model untuk menyesuaikan prediksi berdasarkan kecenderungan umum pengguna atau restoran. Ketika model menerima input (pasangan ID pengguna dan ID restoran), langkah-langkah berikut dilakukan:
    - Ambil Vektor: Model mengambil vektor embedding untuk pengguna dan restoran yang sesuai.
    - Hitung Interaksi: Model menghitung interaksi antara pengguna dan restoran dengan melakukan produk titik (dot product) antara vektor pengguna dan vektor restoran. Ini memberikan nilai yang menunjukkan seberapa baik pengguna dan restoran "cocok" satu sama lain.
    - Tambahkan Bias: Model menambahkan bias pengguna dan restoran ke nilai interaksi untuk mendapatkan prediksi akhir.
    - Aktivasi Sigmoid: Model menerapkan fungsi aktivasi sigmoid pada hasil akhir, yang mengubah nilai menjadi rentang antara 0 dan 1. Nilai ini dapat diartikan sebagai probabilitas atau rating yang menunjukkan seberapa besar kemungkinan pengguna menyukai restoran tersebut.

Secara sederhana, algoritma ini menggunakan teknik embedding untuk merepresentasikan pengguna dan penulis, menghitung interaksi antara keduanya, dan menyesuaikan prediksi dengan bias. Dengan cara ini, model dapat memberikan rekomendasi yang lebih akurat berdasarkan data yang ada.

Hasil N Top Rekomendasi pada Collaborative Filtering ditunjukkan sebagai berikut:

**Top 10 Book Recommendations for User 278450**

| Rank | Author                          | Book Title                                                            |
|------|---------------------------------|----------------------------------------------------------------------|
| 1    | Harper Lee                      | To Kill a Mockingbird                                                 |
| 2    | Robert T. Kiyosaki              | Rich Dad, Poor Dad: What the Rich Teach Their Kids About Money--That the Poor and Middle Class Do Not! |
| 3    | Carl Sagan                      | The Demon-Haunted World: Science As a Candle in the Dark              |
| 4    | Chitra Banerjee Divakaruni      | Arranged Marriage: Stories                                            |
| 5    | Chitra Banerjee Divakaruni      | The Unknown Errors of Our Lives: Stories                              |
| 6    | George Orwell                   | 1984                                                                 |
| 7    | Jacqueline Carey               | Kushiel's Chosen (Kushiel's Legacy)                                   |
| 8    | JOHN GRISHAM                    | The Runaway Jury                                                      |
| 9    | Anne Bishop                     | Daughter of the Blood (Black Jewels Trilogy)                          |
| 10   | Anne Rice                       | Memnoch the Devil (Vampire Chronicles, No 5)                          |


### Komparasi Model
#### Content-Based Filtering
> Pros
1. Personalized Sepenuhnya
Rekomendasi berdasarkan preferensi unit tiap pengguna, bukan berdasarkan orang lain.
2. Tidak butuh banyak data pengguna lain
Cocok untuk sistem dengan sedikit data pengguna
3. Aman dari popularitas palus
Tidak bias terhadap item populer saja, fokus pada kemiripan konten.
4. Transparan dan dapat dijelaskan
Mudah dijelaskan mengapa sistem merekomendasikan item tertentu
> Cons
1. Kurang variatif
Cenderung merekomendasikan buku yang mirip-mirip selalu, tidak ada rekomendasi baru yang mungkin disukai oleh pengguna.
2. Butuh representasi fitur yang baik
Hasil tergantung dari seberapa baik fitur konten (genre, deskripsi) direpresentasikan
3. Tidak bisa menangkap tren kolektif
Tidak memanfaatkan informasi dari pengguna lain(trend)

#### Collaborative Filtering
> Pros
1. Menangkap selera kolektif
Menggunakan preferensi banyak pengguna, memungkinkan penemuan item yang tidak terduga
2. Tidak perlu informasi konten
sistem tetap bisa merekomendasikan meski tidak tahu isi buku(berbasis rating)
3. Bagus untuk meningkatkan engagement
Karena memanfaatkan pola sosial dan tren pengguna
> Cons
1. Cold-Start Problem
Sulit bekerja jika pengguna baru (tidak ada histori) atau item baru (belum ada ulasan)
2. Skalabilitas
Jika jumlah pengguna besar, perhitungan kemiripan bisa sangat berat secara komputasi
3. Data Sparsity
Sistem bisa kurang akurat jika data rating terlalu sedikit atau jarang diisi

### Hasil Evaluasi
Pada bagian ini memvisualisasikan hasil evaluasi matrix antara model berbasis Content-Based dan Collaborative Filtering.

#### Content-Based Filtering
Pada pendekatan Content-based filtering, model memberikan hasil :
- Precision: 100.00%
- Recall: 55.56%
- F1-score: 71.43%
Kemudian ketika diminta rekomendasi dengan penulis yang telah dibaca oleh user, sistem dapat memberikan beberapa rekomendasi buku seperti berikut:
<div>
  
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>book_title</th>
      <th>book_author</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>The Adventures of Tom Sawyer</td>
      <td>Mark Twain</td>
    </tr>
    <tr>
      <th>1</th>
      <td>The Adventures of Tom Sawyer</td>
      <td>Mark Twain</td>
    </tr>
    <tr>
      <th>2</th>
      <td>A Connecticut Yankee in King Arthur's Court (D...</td>
      <td>Mark Twain</td>
    </tr>
    <tr>
      <th>3</th>
      <td>A Connecticut Yankee in King Arthur's Court</td>
      <td>Mark Twain</td>
    </tr>
    <tr>
      <th>4</th>
      <td>A Connecticut Yankee in King Arthur's Court</td>
      <td>Mark Twain</td>
    </tr>
    <tr>
      <th>5</th>
      <td>A Connecticut Yankee in King Arthur's Court</td>
      <td>Mark Twain</td>
    </tr>
    <tr>
      <th>6</th>
      <td>A Connecticut Yankee in King Arthur's Court</td>
      <td>Mark Twain</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Treasury of Illustrated Classics: Adventures o...</td>
      <td>Mark Twain</td>
    </tr>
    <tr>
      <th>8</th>
      <td>The Adventures of Tom Sawyer</td>
      <td>Mark Twain</td>
    </tr>
    <tr>
      <th>9</th>
      <td>The Adventures of Tom Sawyer</td>
      <td>Mark Twain</td>
    </tr>
  </tbody>
</table>
</div>

#### Collaborative Filtering
Pada metode ini menggunakan matrix evaluase RMSE dan MAE dengan hasil :
- RMSE : 21.8%
- MAE : 17.2%
Kemudian ketika sistem diminta untuk memberikan 10 buku rekomendasi dengan model `RecommanderNet` maka dengan grafik pelatihan sebagai berikut
![alt text](image.png)

Menunjukkan hasil rekomendasi seperti berikut
Showing recommendations for users: 278450

--------------------------------

Top 10 Book Recommendation for user: 278450
`
--------------------------------
| **No.** | **Author**                    | **Book Title**                                                                                       |
|---------|-------------------------------|-----------------------------------------------------------------------------------------------------|
| 1       | Harper Lee                    | To Kill a Mockingbird                                                                                |
| 2       | Robert T. Kiyosaki            | Rich Dad, Poor Dad: What the Rich Teach Their Kids About Money--That the Poor and Middle Class Do Not! |
| 3       | Carl Sagan                     | The Demon-Haunted World: Science As a Candle in the Dark                                              |
| 4       | Chitra Banerjee Divakaruni     | Arranged Marriage: Stories                                                                            |
| 5       | Chitra Banerjee Divakaruni     | The Unknown Errors of Our Lives: Stories                                                             |
| 6       | George Orwell                  | 1984                                                                                                 |
| 7       | Jacqueline Carey               | Kushiel's Chosen (Kushiel's Legacy)                                                                  |
| 8       | JOHN GRISHAM                   | The Runaway Jury                                                                                   |
| 9       | Anne Bishop                    | Daughter of the Blood (Black Jewels Trilogy)                                                        |
| 10      | Anne Rice                      | Memnoch the Devil (Vampire Chronicles, No 5)                                                         |


sehingga apabila divisualisasikan dalam bentuk tabel, maka hasil pendekatan kedua sistem rekomendasi diatas dapat dilihat pada tabel dibawah berikut.

| Filtering Method          | Precision        | Recall           | F1-Score        | RMSE            | MAE             |
|--------------------------|------------------|------------------|-----------------|-----------------|-----------------|
| Content-Based Filtering   | 100%  | 55.56%     | 71,43%  |   -             | -               |
| Collaborative Filtering   | -                | -                | -               | 21.8%      | 17.2%       |

Hasil dari evaluasi matrix memberikan insight bahwa model memberikan hasil yang cukup baik untuk sistem rekomendasi dan memberikan generalisasi konten yang baik untuk rekomendasi buku berbasis judul dan penulis buku sehingga harapannya minat baca generasi muda Indonesia dapat meningkat, lalu menaikkan peringkat PISA Indonesia, dan dapat meningkatkan SDM Indonesia di kancah international.

Dalam proyek ini, metrik evaluasi yang digunakan pada Content-Based Filtering adalah `Precision`, `Recall`, dan `F1-score` karena sistem rekomendasi yang dibangun bertujuan untuk memberikan daftar penulis yang paling mirip berdasarkan kesamaan dengan penulis yang sudah dibaca oleh pengguna. 
- **Precision** mengukur seberapa banyak rekomendasi yang benar-benar ditulis oleh penulis yang sama dari seluruh hasil rekomendasi.
- **Recall** mengukur sejauh mana sistem berhasil merekomendasikan seluruh buku dari penulis yang sama yang ada dalam dataset.
- **F1-score** adalah rata-rata harmonis dari Precision dan Recall yang berguna untuk menyeimbangkan keduanya.

**Rumus Evaluasi :**

$$
  Precision = \frac{True Positive}{Total Rekomendasi}
$$

$$
  Recall = \frac{True Positive}{Total buku oleh Penulis}
$$

$$
  F1-Score = 2.\frac{Precision . Recall}{Precision + Recall}
$$

Metrik Evaluasi pada Collaborative Filtering menggunakan Mean Absolut Error(MAE) dan RMSE (Root Mean Squared Error). Dimana RMSE menunjukkan seberapa besar error prediksi model dari ground truth (semakin kecil, semakin baik).

**MAE**: MAE memberikan rata-rata kesalahan absolut. Nilai yang lebih rendah menunjukkan model yang lebih baik. Sebagai aturan umum, MAE yang lebih kecil dari 10% dari rentang nilai target sering dianggap baik.

$$\text{RMSE}(y, \hat{y}) = \sqrt{\frac{\sum_{i=0}^{N - 1} (y_i - \hat{y}_i)^2}{N}}$$

**RMSE**: RMSE memberikan penalti yang lebih besar untuk kesalahan yang lebih besar karena kesalahan dikuadratkan. Ini membuat RMSE lebih sensitif terhadap outlier. Nilai RMSE yang lebih rendah menunjukkan model yang lebih baik.

$$\text{MAE}(y, \hat{y}) = \frac{\sum_{i=0}^{N - 1} |y_i - \hat{y}_i|}{N}$$


## Evaluation
Dengan sistem rekomendasi berbasis AI ini  dapat meningkatkan minat baca buku digenerasi muda sehingga bacaan mereka sesuai dengan minat/kebutuhannya. Kemudian sistem personalisasi dalam penyajian konten literasi juga ditingkatkan agar setiap anak juga memiliki personalisasinya masing-masing yang tersimpan pada agen sistem rekomendasi yang telah kita bangun. Dengan hasil ini `Goals` kita :
1. Meningkatkan minat baca dan keterlibatan generasi muda Indonesia ✅
hal ini tercapai karena sistem rekomendasi buku dapat melakuka personalisasi pembaca dengan buku yang ada sehingga Problem Statements kita yang pertama, **"Buku tidak sesuai minat/kebutuhan pembaca"** dapat terselesaikan
2. Sistem Rekomendasi Buku kita telah dikembangkan. ✅
Kita telah berhasil membuat AI untuk melakukan rekomendasi buku melalui 2 pendekatan, Content-based filtering dan Collaborative Filtering sehingga dapat memberikan akurasi yang general pada user berdasarkan 2 pendekatan masing-masing sehingga menyelesaikan Problem Statements yang kedua, **Kurangnya sistem personalisasi dalam penyajian konten literasi**
