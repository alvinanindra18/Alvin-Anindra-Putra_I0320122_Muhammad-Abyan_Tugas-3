list = ['yeario', 'tazkiya', 'alqodriano', 'salma', 'ryan', 'sony', 'tito', 'zaneta', 'rana', 'stefani' ]
print(list)
print("isi list indeks nomor 4,6,7: ", list[4], list[6], list[7])

#mengganti nama list indeks nomor 3,5,9
list[3], list[5], list[9] = "sasa", "attar", "bagus"
print("nama yang baru pada indeks 3,5,9", list)

#menambah 2 nama teman
list.append('diva')
list.append('william')
print(list)

#menampilkan nama semua teman dengan perulangan
print(list)

#menampilkan panjang nama list
print(len(list))
