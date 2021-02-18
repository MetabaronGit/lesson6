text1 = """In the past, I have been manually keying in the financial data for stocks into Excel and then generate charts to visualize the data. This has taken up a lot of time and it's very prone to human error.
Recently, I came to realize that Google Apps Script may be the rescue and possibly reduces all the manual work and thus automating the process of filling in financial data and generating charts."""
text2 = """The above shows the entry point that prompts dialog to accept user’s input and further validate the input before calling the API to retrieve the stock price quote. The first prompts for the stock code, followed by the time series (whether it’s 1-min, 5-min, 15-min, hourly or daily) and the number of data points. As the number of data points that will be returned can go up to thousands and this will result in very slow Google Sheet, we are adding this field with a warning to indicate that high number can cause slowness."""
# pro vsechny texty vytvor slovnik, ve kterem bude slovnik:
# 1) Poctu jednotlivych slov,
# 2) List slov zacinajici na "b"
# 3) Pocet slov s delkou 4.
# 4) Moznos vyberu pismena a delky

slovnik = dict(text1=dict(), text2=dict())

for i in range(len(slovnik)):
    key = "text" + str(i + 1)
    if key == "text1":
        text_list = text1.split()
    else:
        text_list = text2.split()

    pocet_slov = len(text_list)
    pocet_slov_delka_4 = 0
    slova_od_b = list()

    for n in range(pocet_slov):
        if len(text_list[n]) == 4:
            pocet_slov_delka_4 += 1
        if text_list[n][0] == "b":
            slova_od_b.append(text_list[n])

    slovnik[key]["pocet_slov"] = pocet_slov
    slovnik[key]["pocet_slov_delka_4"] = pocet_slov_delka_4
    slovnik[key]["slova_od_b"] = slova_od_b

print(slovnik)

# vzorové řešení
# --------------------
slovnik = {}
delka_slov = 7
slova_zacinajici_na_pismeno = "g"

for i, text in enumerate((text1, text2), 1):
  ocistena_slova = [slovo.strip(",.!?)(").lower() for slovo in text.split(" ")]
  slovnik[f"text{i}"] = {"polcet_slov":  { slovo : ocistena_slova.count(slovo) for slovo in ocistena_slova},
                         f"pocet_slov_zacinajici_na_{slova_zacinajici_na_pismeno}" : sum(1 for slovo in ocistena_slova if slovo.startswith(slova_zacinajici_na_pismeno)),
                         f"list_slov_zacinajicich_na_{slova_zacinajici_na_pismeno}" : [slovo for slovo in ocistena_slova if slovo.startswith(slova_zacinajici_na_pismeno)],
                         f"pocet_slov_s_delkou_{delka_slov}" : sum(1 for slovo in ocistena_slova if len(slovo) == delka_slov),
                         f"slova_s_delkou_{delka_slov}" : [slovo for slovo in ocistena_slova if len(slovo) == delka_slov]
                        }
print(slovnik)
