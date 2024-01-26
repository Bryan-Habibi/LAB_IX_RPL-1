def baca(nama):
    try:
        with open(nama, 'r') as file:
            isi = file.read()
            print(f"Isi file {nama}:\n{isi}")
    except FileNotFoundError:
        print(f"File {nama} tidak ditemukan.")

def tulis(nama, newTeks):
    with open(nama, 'w') as file_tulis:
        file_tulis.write(newTeks)
    print(f"File {nama} berhasil ditulis.")

# Contoh penggunaan
intro = "Satoru gojo dengan limitless nya gagah perkasa"
inti = "ilmu tinggi jurusnya menggila"
penutup = "dengan mata biru penuh misteri"
tambahan = "pesona kiko menyayat hati"
tulisan = "tugas-operasi-file/operasi.txt"
teksBaru = "\n{}\n{}\n{}\n{}".format(intro, inti, penutup, tambahan)

tulis(tulisan, teksBaru)

baca(tulisan)