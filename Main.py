# Yunus Emre Ay / E-posta:TR.yunus.emre.ay@gmail.com

import sys
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

with open("Main.txt", "r", encoding="utf-8") as file:

    matris = list()
    boyut = int(file.readline().replace("\n",""))

    for i in range(boyut):  # dosyadaki bilgiler adim adim matrise aliniyor
        liste = file.readline().replace("\n", "").split(",")
        matris.append(liste)

alfabe = "ABCDEFGHIJKLMNOPRSTUVYZ"


def gorsel_yazdir(): # Graphs yapisini gorsel olarak yazdirmaktadir.
    edges = list()
    for i in range(boyut):
        for j in range(boyut):
            if matris[i][j] != "0":
                edges.append((alfabe[i], alfabe[j]))


    G = nx.DiGraph()
    G.add_edges_from(edges)

    nx.draw_circular(G, with_labels=True)
    plt.savefig("Graphs_yapisi.png")     # python dosyasinin buludugu dizine graphs yapisini "Graphs_yapisi.png" ismiyle yazdirmaktadir.
    plt.show()


def sonuc_yazdir(liste):
    yazdir = dict()
    for i in liste:
        yazdir[i[0]]=i[1:3]

    print(pd.DataFrame(yazdir,index=["Maliyet:","Geldigi Yer:"]))
    print()

    for i in range((boyut*4)+20): # Cizgi cekiyor
         print("-",end='')
    print("\n")


def bellman_ford_algoritmasi():
    sonuc = list()
    kenarlar = list()

    secim = alfabe[0:boyut]

    while(True):
        print("Lutfen Baslangic Node'unu ve Hedef Nodu'unu seciniz.(Buyuk harf kullaniniz)\nNode'lar: ",end="")
        for i in range(boyut-1):
            print("{} / ".format(alfabe[i]),end="")
        print(alfabe[i+1])
        start = input("Baslangic Node --> ")
        finis = input ("Hedef Node --> ")

        if (start in secim) and (finis in secim):
            break

    for i in range(boyut):
        liste = list()
        liste.append(alfabe[i])
        liste.append("∞")
        liste.append("∞")
        sonuc.append(liste)
    for i in range(len(sonuc)): # Baslangic node belirleme
        if sonuc[i][0] == start:
            sonuc[i][1] = 0
            sonuc[i][2] = start

    sonuc_yazdir(sonuc)

    for kenar in range(boyut): #Tum kenarlari liste icerisine aliyor
        for stun in range(boyut):
            if matris[kenar][stun] != '0':
                liste = list()
                liste.append(alfabe[kenar])
                liste.append(alfabe[stun])
                liste.append(int(matris[kenar][stun]))
                kenarlar.append(liste)


    for dongu in range(boyut):
        for eleman in range(len(kenarlar)):
            for ilk in sonuc:
                if kenarlar[eleman][0] == ilk[0]:
                    break
            if ilk[1] == "∞":
                continue

            for son in sonuc:
                if kenarlar[eleman][1] == son[0]:
                    break

            if (son[1] == "∞") or (ilk[1] + int(kenarlar[eleman][2]) < son[1]):
                son[1] = ilk[1] + int(kenarlar[eleman][2])
                son[2] = ilk[0]
        sonuc_yazdir(sonuc)


    mesafe = "∞"
    yol = list()
    aranan = finis
    while (True):
        for i in range(boyut):
            if sonuc[i][0] == aranan:
                if mesafe == "∞":
                    mesafe = sonuc[i][1]
                yol.append(aranan)
                aranan = sonuc[i][2]
        if aranan == start:
            break

    if start not in yol:
        yol.append(start)

    print("\n\nMesafa: {} / izlenmesi Gereken Yol: ".format(mesafe), end="")
    print(*reversed(yol), sep=" --> ")
    print("\n***Python Dosyasinin Buludugu Dizine Graphs Yapisi Gorsel olarak Yazdirilmstir.***\n")


print("--------------------------------------------------------------------------------------------------------------")
print("\n***Bilgilendirme: 'txt' Dosyasinda Bulunan '0' Simgesi 'Kenar Yok' Olarak Dergerlendirilecektir***\n")

bellman_ford_algoritmasi()
gorsel_yazdir()
