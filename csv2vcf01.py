import csv
import vobject
import tkinter

print('Csv format must be NAME,PHONE NUMBER')

#Choose file dialog
from tkinter import filedialog
tkinter.Tk().withdraw()
file = filedialog.askopenfilename(filetypes=[('Csv file','*.csv'),])
name = file[:-4]+'-FINAL.vcf'

with open(file, 'r') as csvfile:
    reader = csv.reader(csvfile)
    for col in reader:
        j = vobject.vCard()
        j.add('fn')
        j.fn.value = col[0]
        j.add('tel')
        j.tel.value = col[1]
        file = open(name,'a')
        file.write(j.serialize())
        file.close()
print('Done!')
