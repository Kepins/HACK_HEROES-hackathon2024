def produkt_wartosci(line, ktory):
    line.split(',')
    line[3].split('x')
    return line[ktory]
def sort_by_weight(zamowione_produkty, bn):
	#cout << "aaaa" << endl;
	posortowane = {}
	for i in range(bn):
		#waga = 0;
		max=(0,0,0,0,0,0)
		#max.nr = 999;
		#max.w = max.x = max.y = max.z = max.q = 0;
		#cout << max.nr << max.w << max.x << max.y << max.z << max.q << endl;
		for j in range(bn):
			tempv = 0
			for k in range(i):
				if (zamowione_produkty[j].nr == posortowane[k].nr):
					tempv = 1
			if (tempv == 0):
				if (zamowione_produkty[j].w >= max.w):
					max = zamowione_produkty[j]
		posortowane[i] = max
	for i in range(bn):
		print(posortowane[i].nr , " " , posortowane[i].w , " " ,
			posortowane[i].x , " " , posortowane[i].y << " " ,
			posortowane[i].z , " " , posortowane[i].q)
	#paleciak(posortowane, bn);

def main():
    plik_n = open("lista.csv", "r");
    n = 0
    while True:
        n += 1
        line = plik_n.readline()
        if not line:
            break
    plik_n.close();
    lista_produktow = [];
    plik_a = open("lista.csv", "r");
    while True:
        dane_produktu=[]
        line = plik_a.readline()
        if not line:
            break
        dane_produktu.append((produkt_wartosci(line, 0)) - 1)
        dane_produktu.append(produkt_wartosci(line, 2))
        dane_produktu.append(produkt_wartosci(line, 3))
        dane_produktu.append(produkt_wartosci(line, 4))
        dane_produktu.append(produkt_wartosci(line, 5))
        dane_produktu.append(0)
        lista_produktow.append(dane_produktu)
    plik_a.close();
    op = input()
    plik_b=open("zamowienie" + op + ".csv", "r");
    iii = 0;
    zamowione_jeden= []
    while True:
        dane_produktu = []
        line = plik_a.readline()
        iii += 1
        if not line:
            break
        dane_produktu.append((produkt_wartosci(line, 0) - 1))
        dane_produktu.append(produkt_wartosci(line, 2))
        dane_produktu.append(produkt_wartosci(line, 3))
        zamowione_jeden.append(dane_produktu)
    plik_a.close();
    zamowione_path=[]
    for i in range(iii):
        dane_produktu=[]
        dane_produktu.append(int(zamowione_jeden[i][0]))
        dane_produktu.append(int(lista_produktow[int(zamowione_jeden[i][0])][2]))
        dane_produktu.append(int(zamowione_jeden[i][2]))
        dane_produktu.append(int(zamowione_jeden[i][1]))
        zamowione_path.append(dane_produktu)

    bn = 0;
    while (getline(plik_b, line)):
        bn += 1;
    plik_b = close();

    plik_c = open("zamowienie" + op + ".csv");
    iii = 0;
    while (getline(plik_c, line)):
        zamowione_produkty[iii].nr = produkt_wartosci(line, 0) - 1;
        zamowione_produkty[iii].w = lista_produktow[zamowione_produkty[iii].nr].w;
        zamowione_produkty[iii].x = lista_produktow[zamowione_produkty[iii].nr].x / 20;
        zamowione_produkty[iii].y = lista_produktow[zamowione_produkty[iii].nr].y / 20;
        zamowione_produkty[iii].z = lista_produktow[zamowione_produkty[iii].nr].z / 20;
        zamowione_produkty[iii].q = produkt_wartosci(line, 3);
        iii += 1;

    plik_c = close();
    for (int i = 0; i < bn; i++) {
        cout << zamowione_produkty[i].nr + 1 << " " << zamowione_produkty[i].w << " " << zamowione_produkty[
            i].x << " " << zamowione_produkty[i].y << " " << zamowione_produkty[i].z << " " << zamowione_produkty[
            i].q << endl;
    }
    cout << endl;
    sortowanie4(zamowione_produkty, bn);
