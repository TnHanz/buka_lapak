# Coded By : IqbalDev
import requests, os
banner = '''\033[96;1m
__________       __             .____                         __    
\______   \__ __|  | _______    |    |   _____  ___________  |  | __
 |    |  _/  |  \  |/ /\__  \   |    |   \__  \ \____ \__  \ |  |/ /
 |    |   \  |  /    <  / __ \_ |    |___ / __ \|  |_> > __ \|    < 
 |______  /____/|__|_ \(____  / |_______ (____  /   __(____  /__|_ \\
        \/           \/     \/          \/    \/|__|       \/     \/
 	\033[92;1m   Coded By : Iqbal Dev  / {  B U K A  L A P A K  } 
    \033[97;1m    +-----------------------------------------------------+  
	\033[92;1m   Belanja Bisa Disesuaikan Dengan Isi Dompet Kita \033[97;1m''' 

url = 'https://api.bukalapak.com/multistrategy-products?'

def masok():
	try:
		h = open('hasil.txt', 'w')
		h.write('')
		h.close()
		os.system('cls' if os.name == 'nt' else 'clear')
		print banner
		print "+"+'-'*70+'+'
		key = raw_input("\033[92;1m     {@}\033[96;1m Cari Produk = \033[97;1m")
		har = input("\033[92;1m     {$}\033[96;1m Harga Dibawah \033[97;1m= ")
		if key == '' or key == ' ':
			print "\n \033[91;1m Jangan Kosong.....!"
			raw_input('\033[92;1m\n  Tekan Enter... ')
			masok()
		print "+"+'-'*50+'+\n \033[92;1m (Prosess........)\n'
		i = 1
		for pg in range(3, 101):
		  try:
			  token = open('token.txt', 'r').read()
			  parameter = {
				'prambanan_override': True,
				'keywords': key,
				'limit': 50,
				'offset': 50,
				'page': pg,
				'facet': True,
				'access_token': token
			}
			  req = requests.get(url, params=parameter).json()
			  produk = req['data']
			  for dev in produk:
			  	nama = dev['name']
			  	harga = dev['price']
			  	stok = dev['stock']
			  	link = dev['url']
			  	if harga < har:
			  		print "\033[97;1m Produk:\033[92;1m", i
			  		print "\033[97;1m Nama  :\033[97;1m", nama
			  		print "\033[97;1m Harga :\033[93;1m \033[97;1mRp\033[92;1m"+ str(harga)
			  		print "\033[97;1m Stok  :\033[97;1m", stok
			  		print "\033[97;1m Url   :\033[93;1m", link
			  		print "\033[96;1m=="*60
			  		i += 1
			  		has = open('hasil.txt', 'a')
			  		has.write('\n Nama : '+nama+ '\n Harga: '+str(harga)+ '\n Stok : '+ str(stok)+ '\n Url  : '+ link + '\n' + '='*60)
			  		has.close()
		  except KeyboardInterrupt:
		    exit('\n Stopppp.....')
		if i == 1: 
		  print "\n   \033[93;1m Tidak Ada Produk Yang Ditemukan... \n" 	
	except KeyError:
		print '''   \033[91;1m 		Access Token Udah Kedaluarsa....
	 Silahkan Ambil Token Website BukaLapak Lagi..'''
		def inp_tok():
		  try:
			iq = raw_input('\n \033[96;1m  [in+]\033[97;1m Input Access Token = \033[93;1m')
			dat = open('token.txt', 'w')
			dat.write(iq)
			dat.close()
			token = open('token.txt', 'r').read()
			parameter = {
				'prambanan_override': True,
				'keywords': key,
				'limit': 50,
				'offset': 50,
				'page': pg,
				'facet': True,
				'access_token': token
			}
			re_cek = requests.get(url, params=parameter).json()
			cek_dev = re_cek['data']
			print "\n  \033[92;1m        Suksessss......\n"
		  except KeyError:
		  	print "\n \033[93;1m Token Salah... Silahkan Masukkan Token Yang Benar.."
		  	inp_tok()
		  except KeyboardInterrupt:
		  	exit('\n\n  Keluar.....')

		inp_tok()


	except requests.exceptions.ConnectionError:
		print " \033[91;1m  Periksa Koneksi Internet...."

	except SyntaxError:
	  try:
		print "\n \033[91;1m   Isi Yang Benar lah Cukk....!"
		raw_input('\033[92;1m\n  Tekan Enter... ')
		masok()
	  except KeyboardInterrupt:
	  	exit('\n Keluar..')
	except NameError:
	  try:
		print "\n \033[91;1m   Masukkan Harga Yg Benar....!"
		raw_input('\033[92;1m\n  Tekan Enter... ')
		masok()
	  except KeyboardInterrupt:
	  	exit('\n Keluar...')

def main():
	masok()

if __name__=='__main__':
	main()