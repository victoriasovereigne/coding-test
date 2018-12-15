from collections import defaultdict
class Cart:
	def __init__(self):
		self.cart = defaultdict(int)

	def tambahProduk(self, kodeProduk, kuantitas):
		self.cart[kodeProduk] += kuantitas

	def hapusProduk(self, kodeProduk):
		if kodeProduk in self.cart:
			self.cart.pop(kodeProduk, None)

	def tampilkanCart(self):
		for kodeProduk in self.cart:
			print(kodeProduk, '('+str(self.cart[kodeProduk])+')')

keranjang = Cart()
keranjang.tambahProduk("Topi Putih", 2)

keranjang.tambahProduk("Kemeja Hitam", 3)

keranjang.tambahProduk("Sepatu Merah", 1)
keranjang.tambahProduk("Sepatu Merah", 4)
keranjang.tambahProduk("Sepatu Merah", 2)

keranjang.hapusProduk("Kemeja Hitam")

keranjang.hapusProduk("Baju Hijau")

keranjang.tampilkanCart();
