import json

class jsonku:
    def baca(self, file):
        with open(file, 'r') as file:
            data = json.load(file)
            print(data)
            return data

    def tulis(self, file, obj):
        try:
            with open(file, 'w') as tulis:
                json.dump(obj, tulis, indent=8)
            print("Objek berhasil ditulis.")
            return tulis 
        except Exception as e:
            print(f"Gagal menulis objek: {str(e)}")

    def Update(self, file, key, value):
        data = self.baca(file)
        if key in data:
            data[key] = value 
            print(f"Data dengan nama '{key}' telah diperbarui.")
        else:
            data[key] = value 
            print(f"Data dengan nama '{key}' telah ditambahkan.")
        self.tulis(file, data)
        return data  

    def hapus(self, file, key):
        try:
            with open(file, 'r') as f:
                data = json.load(f)
                if key in data:
                    del data[key]
                    with open(file, 'w') as fhapus:
                        json.dump(data, fhapus, indent=4)
                    print(f"Objek bernama '{key}' telah dihapus.")
                else:
                    print(f"Tidak ada objek dengan nama '{key}'.")
        except Exception as e:
            print(f"Gagal menghapus objek: {str(e)}")