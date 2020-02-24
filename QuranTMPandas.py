import pandas as pd
from tkinter import filedialog
import re

print("Choose your file from the popped-up window \n")

root = filedialog.Tk
root.filename = filedialog.askopenfilename(initialdir = "C:/Users/lab/PycharmProjects/excel1", title="choose your file", filetypes=(("excel files","*.xlsm"),("excel files","*.xlsx"),("excel files","*.xls"),("all files","*.*")))
root.withdraw

print("Reading the file to display 1670 root words for you to choose from ........\n")

df = pd.read_excel(root.filename, 'QuranTM')
(rows, column) = df.shape

column = 5
dslist = []
dslistfinal = []
intlist = []


for r in range(1, rows):
    for c in range(0, column + 1):
        if isinstance(df.values[r, c], str):
            ds = df.values[r, c]
            found = ""
            m = re.search('Root(.*) ]', ds)
            if m:
                found = m.group(1)
                ds = found
                ds = re.sub(" *", "", ds)
                dslist.append(ds)

for ds in dslist:
    if ds not in dslistfinal:
        dslistfinal.append(ds)

for i in range(1, 1672):
    intlist.append(i)
dictdslistfinal = dict(zip(intlist, dslistfinal))

print('Here is the list of roots for which Allah SWT has chosen words in Quran')
print('--- is the entry for Prepositions, Conjunctions, Emphasis particles, etc. which have no roots\n')

for keys in dictdslistfinal:
    print(dictdslistfinal[keys], keys)

dr = ""


def display():
    print('You chose the root word ' + dictdslistfinal[int(dr)] + ' , here is the info in Quran for this root')
    for r in range(1, rows):
        for c in range(0, column + 1):
            if isinstance(df.values[r, c], str):
                ds = df.values[r, c]
                found = ""
                m = re.search('Root(.*) ]', ds)
            if m:
                found = m.group(1)
                ds = found
                ds = re.sub(" *", "", ds)
                if ds == dictdslistfinal[int(dr)]:
                    dw = df.values[r - 1, c]
                    dw1 = df.values[r - 1, 0]
                    dw2 = df.values[r - 1, 1]
                    dw3 = df.values[r - 1, 2]
                    dw4 = df.values[r - 1, 3]
                    dw5 = df.values[r - 1, 4]
                    dw6 = df.values[r - 1, 5]
                    ds1 = df.values[r, c]
                    ds1 = re.sub('\[.*\]', "", ds1)
                    ds1 = re.sub('_x000D_', "", ds1)
                    # ds1 = re.sub(None, "-", ds1)
                    nrc = "?,-().\""
                    for char in nrc:
                        ds1 = ds1.replace(char, "")  # english phrase left
                    print('\n', dw, '\n', ds1, dw1, dw2, dw3, dw4, dw5, dw6)


choice = 'y'
search = input("\nWould you like to explore the Allah\'s wording and their meanings in Quran? \n" + "\nEnter y for Yes or any other key to quit the program : ")
while search.lower() == 'y':
    if choice == 'y':
        dr = input("Enter the root number from the list above ")
        try:
            if int(dr) in dictdslistfinal.keys():
                display()
            else:
                print("Sorry, the number must be amongst the list above")
        except:
            print("Ooops! integer expected")
    choice = input("\nYou may enter y again to choose another root number or enter any other key to exit the program : ")
    if choice.lower() == 'y':
        search = choice
    else:
        break
