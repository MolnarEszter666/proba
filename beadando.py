#42es
# eloszor be kell kernem harom szot ezeket szet kell splitelni
# ki kell vennem az elso es utolso betujuket (first, last)
# az angol abc betuit egyenlove kell tennem szamokkal igy az elso es utolso betu egy sorszam lesz (az abc-ben elfoglalt helyuk)
# ezt a ket szamot kell osszehasonlitanom
# kivonom oket egymasbol =tav
# minusz miatt abs()
# osszehasonlitom a harom szo tavjat
# legkisebb lesz a gyoztes

def main():
    abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w',
           'x', 'y', 'z']
    gyoztes=""
    txt = input("Adjon meg három szót!")
    x = txt.split()
    szo1=x[0]
    szo2=x[1]
    szo3=x[2]
    for ch in szo1:
        first=abc.index(szo1[0])+1
        last=abc.index(szo1[len(szo1)-1])+1
        tav1 = abs(first - last)
        print(tav1)
        break
    for ch in szo2:
        first=abc.index(szo2[0])+1
        last=abc.index(szo2[len(szo2)-1])+1
        tav2 = abs(first - last)
        print(tav2)
        break
    for ch in szo3:
        first = abc.index(szo3[0]) + 1
        last = abc.index(szo3[len(szo3) - 1]) + 1
        tav3 = abs(first - last)
        print(tav3)
        break

    gyoztes=min(tav1,tav2,tav3)
    print(gyoztes)

main()

