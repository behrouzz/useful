import img2pdf
from datetime import date
from glob import glob

today = date.today()

src = 'data/*.jpg'
out = 'data/BS_' + today.strftime("%Y-%m-%d") + '.pdf'

files_list = glob(src)

with open(out, 'wb') as f:
    f.write(img2pdf.convert(files_list))
