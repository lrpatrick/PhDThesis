"""
Author: LRP
Date: 23-02-2016
Description:
Scrape the ads abstract service for the bibtex entries I don't have for the
ngc6822.tex file

"""
import numpy as np
import urllib

urls = np.genfromtxt('abstracturls.txt', dtype='S')

for i, j in enumerate(urls):
    name = 'abs' + str(i)
    print(name)
    urllib.urlretrieve(j, filename=name)
