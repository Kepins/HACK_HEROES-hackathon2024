# include <iostream>
# include <fstream>
# include <sstream>
# include <iomanip>

class produkt:
    nr: int
    w: int
    x: int
    y: int
    z: int
    q: int

def produkt_wymiary(line, ktory):
    line.split('x')
    return line[ktory-3]

def produkt_wartosci(line, ktory):
    line.split(',')
    line[3].split('x')
    return int(line[ktory])


def fit_all(paleta, punkt, x, y, z):
	xo = punkt.x;
	yo = punkt.y;
	zo = punkt.z;
	if (zo+z >= 92):
		return false;
	if (xo+x >= 60):
		return false;
	if (yo+y >= 40):
		return false;

	szukana = paleta[xo][yo];
	for i in range(xo+x):
		for j in range(yo+y):
			if (paleta[i][j] != szukana):
				return false;

	for i in range(x):
		for j in range(y):
			paleta[i][j] += z;
	return true;


def wstaw(wybrany, paleta, punkt):
	x = wybrany.x;
	y = wybrany.y;
	z = wybrany.z;

	if(fit_all(paleta, punkt, x, y, z)):
		return true;
	if (fit_all(paleta, punkt, x, z, y)):
		return true;
	if (fit_all(paleta, punkt, y, x, z)):
		return true;
	if (fit_all(paleta, punkt, y, z, x)):
		return true;
	if (fit_all(paleta, punkt, z, x, y)):
		return true;
	if (fit_all(paleta, punkt, z, y, x)):
		return true;
	return false;



def ustawianie(wybrany, paleta):
	for i in range(60):
		for j in range(40):
			punkt.x = i;
			punkt.y = j;
			punkt.z = paleta[i][j];
			if (wstaw(wybrany, paleta, punkt)):
				return true;
	return false;


def czyszczenie(paleta):
	for i in range(60):
		for j in range(40):
			paleta[i][j] = 0;


def paleciak(posortowane, bn):
	print("aaaaaaa")
	palety = 1;
	kt = 0;
	#paleta[60][40];
	paleta={}
	czyszczenie(paleta)
	while (kt < bn):
		if (posortowane[kt].q > 0):
			if (ustawianie(posortowane[kt], paleta)):
				posortowane[kt].q -= 1;
			else:
				palety += 1;
				czyszczenie(paleta);
		else:
			kt += 1;

	print(palety)


def sortowanie4(zamowione_produkty, bn):

	#cout << "aaaa" << endl;
	posortowane = {};
	for i in range(bn):
		#waga = 0;
		max=produkt(0,0,0,0,0,0)
		#max.nr = 999;
		#max.w = max.x = max.y = max.z = max.q = 0;
		#cout << max.nr << max.w << max.x << max.y << max.z << max.q << endl;
		for j in range(bn):
			tempv = 0;
			for k in range(i):
				if (zamowione_produkty[j].nr == posortowane[k].nr):
					tempv = 1;
			if (tempv == 0):
				if (zamowione_produkty[j].w >= max.w):
					max = zamowione_produkty[j];
		posortowane[i] = max;
	for i in range(bn):
		print(posortowane[i].nr , " " , posortowane[i].w , " " ,
			posortowane[i].x , " " , posortowane[i].y << " " ,
			posortowane[i].z , " " , posortowane[i].q)
	paleciak(posortowane, bn);

def main():
	plik_n=open("lista.csv","r");
	n = 0;
	while (getline(plik_n, line)):
		n += 1;
	plik_n=close();
	lista_produktow = {};
	plik_a=open("lista.csv","r");
	iii = 0;
	while (getline(plik_a, line)):
		lista_produktow[iii].nr = produkt_wartosci(line, 0) - 1;
		lista_produktow[iii].w = produkt_wartosci(line, 2);
		lista_produktow[iii].x = produkt_wartosci(line, 3);
		lista_produktow[iii].y = produkt_wartosci(line, 4);
		lista_produktow[iii].z = produkt_wartosci(line, 5);
		lista_produktow[iii].q = 0;
		iii += 1;
	plik_a=close();
	op=input()
	plik_b.open("zamowienie"+op+".csv");

	bn = 0;
	while (getline(plik_b, line)):
		bn += 1;
	plik_b=close();
	zamowione_produkty={}
	plik_c=open("zamowienie" + op + ".csv");
	iii = 0;
	while (getline(plik_c, line)):
		zamowione_produkty[iii].nr = produkt_wartosci(line, 0) - 1;
		zamowione_produkty[iii].w = lista_produktow[zamowione_produkty[iii].nr].w;
		zamowione_produkty[iii].x = lista_produktow[zamowione_produkty[iii].nr].x / 20;
		zamowione_produkty[iii].y = lista_produktow[zamowione_produkty[iii].nr].y / 20;
		zamowione_produkty[iii].z = lista_produktow[zamowione_produkty[iii].nr].z / 20;
		zamowione_produkty[iii].q = produkt_wartosci(line, 3);
		iii += 1;

	plik_c=close();
	for (int i = 0; i < bn; i++) {
		cout << zamowione_produkty[i].nr + 1 << " " << zamowione_produkty[i].w << " " << zamowione_produkty[i].x << " " << zamowione_produkty[i].y << " " << zamowione_produkty[i].z << " " << zamowione_produkty[i].q << endl;
	}
	cout << endl;
	sortowanie4(zamowione_produkty, bn);
	//sortowanie_ukladanie(zamowione_produkty, bn);
	return 0;
}
//tablica 2 wymiarowa, wysoko jako int