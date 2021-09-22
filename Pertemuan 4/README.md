
Part A :
Pertama mengimport modul dari pygame dan juga sys, sedangak widh dan height untuk mengatur ukuran dari windows dan title untuk memberi  nama pada layae window. Membuat class Player didalamnya terdapat fungsi dari posisi objek dan menentukan posisi pergeseran dari objek, pengaturan kecepatan gerak objek.

Part B :
Def update berfungsi untuk memperbarui layar saat terjadi pergeseran objek, dan untuk menentukan batas obejk bergerak sehingga tidak melebihi batas dari ukuran window. Setiap pergeseran dari objek akan memperbarui posisi dari x dan y.  self.rect untuk menampilkan posisi objek dan ukuran objek. Def draw untuk menampikan window dan objek

Part C :
Untuk memanggil pygame dan memanggil window, set_caption untuk mengubah caption menjadi title yang sudah ditentukan. Font untuk menentukan jenis font yang akan digunakan, font.rendedr untuk merender text .

Part D :
Terdapat perulangan dan even dimana saat menekan tombol quit maka proses akan berhenti dan akan menghilang. Kemudian pada event KEYDOWN adalah saat kira menekan tombol keyboard maka akan ada pengecekan nilai yang akan diubah menjadi True agar objek dapat bergerak. Event KEYUP adalah saat kita melepaskan tombol keyboard, akan dilakukan pengecekan lagi dan nilai akan false.

Part E :
Win.fill untuk mengatur warna background window dan win.blit untuk menampilkan text dan mengatur posisi text. Player.draw untuk menampilkan objek sedangakan player update untuk memperbarui layar saat objek bergerak. Pygame.display.flip untuk menampilkan semua yang ada pada display. Dan clock untuk membatasi pergerakan frame agar tidak lebih dari 120 fps.

