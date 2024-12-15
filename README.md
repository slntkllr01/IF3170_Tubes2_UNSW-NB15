# IF3170_Tubes2_UNSW-NB15

| Names                  | NIM      | Pembagian Tugas      | 
| ---------------------- |:--------:|:--------:|
| Thea Josephine Halim   | 13522012 | All      |
| Debrina Veisha R. W.   | 13522025 | All      |
| Melati Anggraini       | 13522035 | All      |
| Raffael Boymian S      | 13522046 | All      |

## The Problem 
Dataset UNSW-NB15 merupakan dataset berisi raw network packets yang dibuat menggunakan IXIA PerfectStorm oleh Cyber Range Lab UNSW Canberra. Dataset ini terdiri dari 10 jenis aktivitas (9 jenis attack dan 1 aktivitas normal). Sembilan jenis attack yang termasuk ke dalam dataset ini adalah Fuzzers, Analysis, Backdoors, DoS, Exploits, Generic, Reconnaissance, Shellcode dan Worms. 

Supervised Learning adalah salah satu jenis pembelajaran mesin (machine learning) di mana model dilatih menggunakan dataset yang sudah memiliki label atau output yang diketahui. Model supervised learning belajar dari data yang berpasangan antara input (fitur) dan output (target) untuk membuat prediksi pada data baru. Data input merupakan kumpulan variabel yang digunakan untuk memprediksi output. Sedangkan data output merupakan nilai target yang ingin diprediksi.

## The Algorithm
#### Algoritma KNN
KNN (K-Nearest Neighbor) adalah salah algoritma supervised learning yang hanya menyimpan seluruh data training dan tidak menghasilkan hipotesis. Algoritma KNN merupakan lazy learner karena sifatnya yang tidak melakukan proses learning atau pembuatan model eksplisit selama tahap pelatihan. Caranya memprediksi data adalah dengan mengkategorikan kelas berdasarkan kemiripannya dalam data yang disimpan. 

#### Algoritma Naive Bayes
Algoritma Naive Bayes adalah salah satu algoritma supervised learning yang berbasis pada Teorema Bayes dengan asumsi "naïve" bahwa semua fitur dalam dataset saling independen, setiap kelas tidak saling mempengaruhi satu sama lain. Pada algoritma Naive Bayes akan dilakukan perhitungan probabilitas suatu data X masuk dalam kelas y.


#### ID3/ Decision Tree
ID3 menggunakan algoritma top-greedy untuk ID3 (Iterative Dichotomiser 3) membangun pohon keputusan berdasarkan entropi dan information gain untuk memisahkan data. Decision tree ini terdiri dari beberapa node berupa persegi panjang, panah (edges) mewakili value yang mungkin dari suatu atribut, dan daun (node terakhir tanpa cabang lagi).

## Setting Up
- Clone this repository with `https://github.com/slntkllr01/IF3170_Tubes2_UNSW-NB15.git`
- Open the .ipynb file then click on the Run All button on top left