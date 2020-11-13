from os import system
from datetime import datetime
import random

def daftar_movie():
	system("cls")
	movie = """
	   ***Daftar Movie***
	1. Konosuba : The Movie
	2. Avengers : Endgame	
	3. Overflow(Sold Out)
	4. Tampilkan tiket yang telah dibeli
	0. Keluar
	"""
	print(movie)

tiket = {
}
today = datetime.now()
code1 = random.randint(0,9999)
code2 = random.randint(0,9999)
code3 = random.randint(0,9999)
code4 = random.randint(0,9999)
month = today.month
hari = today.day
id_tiket1 = str("%04d%02d%02d1" % (code1, hari, month))
id_tiket2 = str("%04d%02d%02d2" % (code2, hari, month))
id_tiket3 = str("%04d%02d%02d3" % (code3, hari, month))
id_tiket4 = str("%04d%02d%02d4" % (code4, hari, month))

def pilih_waktu_kono():
	print("""
	1. 15.00
	2. 18.00
	""")
	jam_tayang = int(input("Pilih jam tayang : "))
	if jam_tayang == 1:
		konosuba1()
	elif jam_tayang == 2:
		konosuba2()
	else:
		return pilih_waktu_kono()

def pilih_waktu_av():
	print("""
	1. 10.00
	2. 21.00
	""")
	jam_tayang = int(input("Pilih jam tayang : "))
	if jam_tayang == 1:
		avengers1()
	elif jam_tayang == 2:
		avengers2()
	else:
		return pilih_waktu_av()

kursi_bioskop = {
	"A":[1, 2, 3, 4, 5],
	"B":[1, 2, 3, 4, 5],
	"C":[1, 2, 3, 4, 5],
	"D":[1, 2, 3, 4, 5],
	"E":[1, 2, 3, 4, 5]
}
def kursi_konosuba1():
	kursi_kon1 = {
	"A":["X", "X", "X", 4, 5],
	"B":[1, "X", "X", 4, 5],
	"C":[1, 2, 3, 4, 5],
	"D":[1, 2, 3, 4, 5],
	"E":[1, 2, 3, 4, 5]
}
	print(f"A = {kursi_kon1['A']}")
	print(f"B = {kursi_kon1['B']}")
	print(f"C = {kursi_kon1['C']}")
	print(f"D = {kursi_kon1['D']}")
	print(f"E = {kursi_kon1['E']}")


def kursi_konosuba2():
	kursi_kon2 = {
	"A":[1, "X", 3, "X", 5],
	"B":["X", 2, "X", 4, "X"],
	"C":[1, "X", 3, 4, 5],
	"D":[1, 2, 3, 4, 5],
	"E":[1, 2, 3, 4, 5]
}
	print(f"A = {kursi_kon2['A']}")
	print(f"B = {kursi_kon2['B']}")
	print(f"C = {kursi_kon2['C']}")
	print(f"D = {kursi_kon2['D']}")
	print(f"E = {kursi_kon2['E']}")

def kursi_avengers1():
	kursi_av1 = {
	"A":[1, "X", "X", 4, 5],
	"B":[1, 2, 3, 4, 5],
	"C":[1, 2, 3, "X", "X"],
	"D":[1, 2, 3, 4, 5],
	"E":[1, 2, 3, 4, 5]
}
	print(f"A = {kursi_av1['A']}")
	print(f"B = {kursi_av1['B']}")
	print(f"C = {kursi_av1['C']}")
	print(f"D = {kursi_av1['D']}")
	print(f"E = {kursi_av1['E']}")

def kursi_avengers2():
	kursi_av2 = {
	"A":[1, "X", "X", "X", 5],
	"B":[1, 2, 3, 4, 5],
	"C":["X", "X", "X", "X", "X"],
	"D":[1, 2, 3, 4, 5],
	"E":[1, 2, 3, 4, 5]
}
	print(f"A = {kursi_av2['A']}")
	print(f"B = {kursi_av2['B']}")
	print(f"C = {kursi_av2['C']}")
	print(f"D = {kursi_av2['D']}")
	print(f"E = {kursi_av2['E']}")

def verify_ans(char):
	char = char.upper()
	if char == "Y":
		return True
	else:
		return False

def cek_kursi_row(row):
	if row.upper() != "A" and row.upper() != "B" and row.upper() != "C" and row.upper() != "D" and row.upper() != "E":
		pilih_row = input("Masukkan row dari A ke E : ")
		return cek_kursi_row(pilih_row)
	else:
		return True

def cek_kursi_angka(angka):
	if angka >= 6 or angka <= 0:
		pilih_angka = int(input("Masukkan angka dari 1 ke 5 : "))
		return cek_kursi_angka(pilih_angka)
	else:
		return True 

def cek_kursi_konosuba1(row, angka):
	if row.upper() =="A":
		if angka == 1 or angka == 2 or angka == 3:
			print("Maaf tempat ini sdh diduduki, silahkan pilih kursi lain")
			pilih_row = input("Pilih Row(Huruf) : ")
			cek_kursi_row(pilih_row)
			pilih_angka = int(input("Pilih Kursi(Angka): "))
			cek_kursi_angka(pilih_angka)
			return cek_kursi_konosuba1(pilih_row, pilih_angka)
		else:
			return angka
	elif row.upper() == "B":
		if angka == 2 or angka == 3:
			print("Maaf tempat ini sdh diduduki, silahkan pilih kursi lain")
			pilih_row = input("Pilih Row(Huruf) : ")
			cek_kursi_row(pilih_row)
			pilih_angka = int(input("Pilih Kursi(Angka): "))
			cek_kursi_angka(pilih_angka)
			return cek_kursi_konosuba1(pilih_row, pilih_angka)
		else:
			return angka
	else:
		return True

def cek_kursi_konosuba2(row,angka):
	if row.upper() =="A":
		if angka == 2 or angka == 4:
			print("Maaf tempat ini sdh diduduki, silahkan pilih kursi lain")
			pilih_row = input("Pilih Row(Huruf) : ")
			cek_kursi_row(pilih_row)
			pilih_angka = int(input("Pilih Kursi(Angka): "))
			cek_kursi_angka(pilih_angka)
			return cek_kursi_konosuba2(pilih_row, pilih_angka)
		else:
			return angka
	elif row.upper() == "B":
		if angka == 1 or angka == 3 or angka == 5:
			print("Maaf tempat ini sdh diduduki, silahkan pilih kursi lain")
			pilih_row = input("Pilih Row(Huruf) : ")
			cek_kursi_row(pilih_row)
			pilih_angka = int(input("Pilih Kursi(Angka): "))
			cek_kursi_angka(pilih_angka)
			return cek_kursi_konosuba2(pilih_row, pilih_angka)
		else:
			return angka
	elif row.upper() == "C":
		if angka == 2:
			print("Maaf tempat ini sdh diduduki, silahkan pilih kursi lain")
			pilih_row = input("Pilih Row(Huruf) : ")
			cek_kursi_row(pilih_row)
			pilih_angka = int(input("Pilih Kursi(Angka): "))
			cek_kursi_angka(pilih_angka)
			return cek_kursi_konosuba2(pilih_row, pilih_angka)
		else:
			return angka
	else:
		return True

def cek_kursi_avengers1(row, angka):
	if row.upper() == "A":
		if angka == 2 or angka == 3:
			print("Maaf tempat ini sdh diduduki, silahkan pilih kursi lain")
			pilih_row = input("Pilih Row(Huruf) : ")
			cek_kursi_row(pilih_row)
			pilih_angka = int(input("Pilih Kursi(Angka): "))
			cek_kursi_angka(pilih_angka)
			return cek_kursi_avengers1(pilih_row, pilih_angka)
		else:
			return angka
	elif row.upper() == "C":
		if angka == 4 or angka == 5:
			print("Maaf tempat ini sdh diduduki, silahkan pilih kursi lain")
			pilih_row = input("Pilih Row(Huruf) : ")
			cek_kursi_row(pilih_row)
			pilih_angka = int(input("Pilih Kursi(Angka): "))
			cek_kursi_angka(pilih_angka)
			return cek_kursi_avengers1(pilih_row, pilih_angka)
		else:
			return angka
	else:
		return True

def cek_kursi_avengers2(row, angka):
	if row.upper() == "A":
		if angka == 2 or angka == 3 or angka == 4:
			print("Maaf tempat ini sdh diduduki, silahkan pilih kursi lain")
			pilih_row = input("Pilih Row(Huruf) : ")
			cek_kursi_row(pilih_row)
			pilih_angka = int(input("Pilih Kursi(Angka): "))
			cek_kursi_angka(pilih_angka)
			return cek_kursi_avengers2(pilih_row, pilih_angka)
		else:
			return angka
	elif row.upper() == "C":
		print("Maaf tempat ini sdh diduduki, silahkan pilih kursi lain")
		pilih_row = input("Pilih Row(Huruf) : ")
		cek_kursi_row(pilih_row)			
		pilih_angka = int(input("Pilih Kursi(Angka): "))
		cek_kursi_angka(pilih_angka)
		return cek_kursi_avengers2(pilih_row, pilih_angka)
	else:
		return True

def konosuba1():
	system("cls")
	kursi_konosuba1()
	pilih_row = input("Pilih Row(Huruf) : ")
	cek_kursi_row(pilih_row)
	pilih_angka = int(input("Pilih Kursi(Angka): "))
	cek_kursi_angka(pilih_angka)
	if cek_kursi_konosuba1(pilih_row, pilih_angka):
		ans = input("Apakah anda yakin untuk membeli tiket ini? (Y/N) : ")
		verify_ans(ans)
		if verify_ans(ans):
			#kursi_kon1[pilih_row][pilih_angka-1] = "X"
			tiket[id_tiket1] = {
			"Movie" : "Konosuba",
			"Row" : pilih_row.upper(),
			"Angka" : pilih_angka,
			"Jam Tayang" : "15.00"
			}
			print(tiket)
			ans2 = input("Terima kasih, apakah anda ingin membeli tiket lagi?(Y/N) : ")
			if verify_ans(ans2):
				return
			else:
				print("Terima kasih sudah membeli")
				exit()
		else:
			return

def konosuba2():
	system("cls")
	kursi_konosuba2()
	pilih_row = input("Pilih Row(Huruf) : ")
	cek_kursi_row(pilih_row)
	pilih_angka = int(input("Pilih Kursi(Angka): "))
	cek_kursi_angka(pilih_angka)
	if cek_kursi_konosuba2(pilih_row, pilih_angka):
		ans = input("Apakah anda yakin untuk membeli tiket ini? (Y/N) : ")
		verify_ans(ans)
		if verify_ans(ans):
			#kursi_kon2[pilih_row][pilih_angka-1] = "X"
			tiket[id_tiket2] = {
			"Movie" : "Konosuba",
			"Row" : pilih_row.upper(),
			"Angka" : pilih_angka,
			"Jam Tayang" : "18.00"
			}
			print(tiket)
			ans2 = input("Terima kasih, apakah anda ingin membeli tiket lagi?(Y/N) : ")
			if verify_ans(ans2):
				return
			else:
				print("Terima kasih sudah membeli")
				exit()
		else:
			return

def avengers1():
	system("cls")
	kursi_avengers1()
	pilih_row = input("Pilih Row(Huruf) : ")
	cek_kursi_row(pilih_row)
	pilih_angka = int(input("Pilih Kursi(Angka): "))
	cek_kursi_angka(pilih_angka)
	if cek_kursi_avengers1(pilih_row, pilih_angka):
		ans = input("Apakah anda yakin untuk membeli tiket ini? (Y/N) : ")
		verify_ans(ans)
		if verify_ans(ans):
			#kursi_kon2[pilih_row][pilih_angka-1] = "X"
			tiket[id_tiket3] = {
			"Movie" : "Avengers : Endgame",
			"Row" : pilih_row.upper(),
			"Angka" : pilih_angka,
			"Jam Tayang" : "10.00"
			}
			print(tiket)
			ans2 = input("Terima kasih, apakah anda ingin membeli tiket lagi?(Y/N) : ")
			if verify_ans(ans2):
				return
			else:
				print("Terima kasih sudah membeli")
				exit()
		else:
			return

def avengers2():
	system("cls")
	kursi_avengers2()
	pilih_row = input("Pilih Row(Huruf) : ")
	cek_kursi_row(pilih_row)
	pilih_angka = int(input("Pilih Kursi(Angka): "))
	cek_kursi_angka(pilih_angka)
	if cek_kursi_avengers2(pilih_row, pilih_angka):
		ans = input("Apakah anda yakin untuk membeli tiket ini? (Y/N) : ")
		verify_ans(ans)
		if verify_ans(ans):
			#kursi_kon2[pilih_row][pilih_angka-1] = "X"
			tiket[id_tiket4] = {
			"Movie" : "Avengers : Endgame",
			"Row" : pilih_row.upper(),
			"Angka" : pilih_angka,
			"Jam Tayang" : "21.00"
			}
			print(tiket)
			ans2 = input("Terima kasih, apakah anda ingin membeli tiket lagi?(Y/N) : ")
			if verify_ans(ans2):
				return
			else:
				print("Terima kasih sudah membeli")
				exit()
		else:
			return

def overflow():
	system("cls")
	kursi_over = {
	"A":["X", "X", "X", "X", "X"],
	"B":["X", "X", "X", "X", "X"],
	"C":["X", "X", "X", "X", "X"],
	"D":["X", "X", "X", "X", "X"],
	"E":["X", "X", "X", "X", "X"]
}	
	print(f"A = {kursi_over['A']}")
	print(f"B = {kursi_over['B']}")
	print(f"C = {kursi_over['C']}")
	print(f"D = {kursi_over['D']}")
	print(f"E = {kursi_over['E']}")
	input("Maaf movie ini telah dibooking penuh, tekan ENTER untuk kembali ke menu")

def tampil():
	if len(tiket) == 0:
		system("cls")
		print(tiket)
		input("Belum ada tiket yang dibeli, tekan ENTER untuk kembali ke menu")
	elif len(tiket) >=1:
		system("cls")
		print(tiket)
		input("Tekan ENTER untuk kembali ke menu")


def check_movie(char):
	if char == 0:
		exit()
	elif nama_movie == 1:
		pilih_waktu_kono()
	elif nama_movie == 2:
		pilih_waktu_av()
	elif nama_movie == 3:
		overflow()
	elif nama_movie == 4:
		tampil()

stop = False

while not stop:
	daftar_movie()
	nama_movie = int(input("Pilihan : "))
	stop = check_movie(nama_movie)
		