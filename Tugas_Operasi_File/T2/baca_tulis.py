class operasiFile():
    def __init__(self):
        pass

    def bacaFile(self, file):
        try:
            with open(file, "r") as baca:
                return baca.read()
        except FileNotFoundError as lost:
            return "File Tidak Ditemukan: {}".format(lost)

    def tulisFile(self, file, isi, metode):
        if metode == 'w':
            try:
                with open(file, "w") as tulis:
                    tulis.write(isi)
                    print('file berhasil ditulis ')
            except Exception as e:
                return "Maaf Terjadi kesalahan saat menulis file ini {}: {}".format(file, e)
        else:
            try:
                with open(file, 'a') as tambah:
                    tambah.write(isi)
                    print('file berhasil ditulis ')
            except Exception as e:
                return "Maaf Terjadi kesalahan saat menulis file ini {}: {}".format(file, e)

# Contoh penggunaan
objek = operasiFile()
objek.tulisFile("baca_tulis/baca_tulis.txt", "\nNama file ini adalah txt", 'a')
print(objek.bacaFile("baca_tulis/baca_tulis.txt"))
 