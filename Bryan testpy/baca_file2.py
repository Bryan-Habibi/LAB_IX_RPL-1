# buka file

file_pantun = open("file_io/pantun.txt", "r")



# baca isi file

pantun = file_pantun.read()

print (pantun)



# tutup file

file_pantun.close()