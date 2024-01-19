# buka file

file_pantun = open("file_io/pantun.txt", "r")



# baca isi file

pantun = file_pantun.readlines()



# cetak baris pertama

print(pantun[0])



# cetak baris kedua

print (pantun[1])



# tutup file

file_pantun.close()