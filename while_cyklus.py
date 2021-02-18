prepinac = True
cislo = 2
while prepinac:
  kontrola = input("Pro ukonceni napis  q: ").lower()
  if kontrola == "q":
    prepinac = False
  else:
    cislo *= cislo
    print(cislo)
else:
  print("Uz jsi venku ze smycky")



cislo = 2
while True:
      kontrola = input("Pro ukonceni napis  q: ").lower()
      if kontrola == "q":
          break
      else:
          cislo *= cislo
          print(cislo)
else:
      print("Uz jsi venku ze smycky")


x = 0
while True:
  x += 1
  if x == 5:
    continue
  elif x == 10:
    print(x)
    break
  else:
    print(x)


index = 0
Jmena_simpsonovych = ["Homer", "Bart", "Marge", "Lisa", "Maggy"]
while index < len(Jmena_simpsonovych):
    if Jmena_simpsonovych[index][0].lower() == "m":
        print(Jmena_simpsonovych[index])
    index += 1