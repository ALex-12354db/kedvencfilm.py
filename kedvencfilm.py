for i in range(3):
    cim = input("Add meg egy film címét: ")
    perc = int(input("Hány perces a film: "))

    ora = perc // 60
    perc_maradek = perc % 60

    print(f"A(z) {cim} című film {ora} óra {perc_maradek} perc hosszú.")