# Nama, Hobi, Sosmed, Lagufav, Makananfav
dict = {'Name' : 'Alvin Anindra Putra',
        'hobby' : ['olahraga','nonton film', 'travelling', 'main game'],
        'sosialmedia' : {'IG' : 'alvinanindra', 'line' : 'alvinanindra5', 'facebook' : 'alvinanindra'},
        'lagukesukaan' : ['iris', 'night changes', 'to the bone'],
        'makanankesukaan' : ['cumi goreng tepung', 'ayam kfc', 'mendoan']}

# Mengubah salah satu hobi dan sosmed
dict['hobby'][0] = 'koleksi jaket'
dict['sosialmedia']['line'] = 'alvinanindra'

# Menghapus 2 makanan favorit
del dict['makanankesukaan'][0]
del dict['makanankesukaan'][1]

# Menambahkan 1 hobi
dict['hobby'].append('berantem')
print (*dict['hobby'], sep= ", ")