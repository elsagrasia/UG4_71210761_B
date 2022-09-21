import json

KaryawanBaru = int((input('Masukkan jumlah Karyawan baru: ')))
for i in range(KaryawanBaru):
    nama = input('Masukkan nama : ')
    list_karyawan = list()
    dict_kolega = dict()
    dict_Alamat = dict()
    alamat = input("Masukan Alamat : ")
    jml_kolega = int(input('Masukkan jumlah kolega: '))
    list_kolega = list()
    for j in range(jml_kolega):
        kolega = input('Masukkan kolega ke-{}: '.format(str(j + 1)))
        list_kolega.append(kolega)
    dict_kolega['Kolega'] = list_kolega
    dict_Alamat['Alamat'] = alamat
    list_karyawan.append(dict_Alamat)
    list_karyawan.append(dict_kolega)
    with open('karyawan.json', 'r') as datafile: 
        data = json.load(datafile)
        data[nama] = list_karyawan
    with open('karyawan.json', 'w') as datafile:
        json.dump(data, datafile)
    print('=== Data berhasil ditambahkan ===\n')