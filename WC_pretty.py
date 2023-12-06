# Replaces local pdf URL's with an external reference.
import os
import sys
import csv
from bs4 import BeautifulSoup
in_html_file = '/Users/Tim/Code/Github/BMPStaging/RiparianBMPs/WatershedConservation.html'
out_html_file = '/Users/Tim/Code/Github/BMPStaging/RiparianBMPs/WatershedConservation_pretty.html'
f = open(in_html_file, mode='r', encoding = 'utf-8')
soup = BeautifulSoup(f, 'html.parser')
f.close()
prettyHTML = soup.prettify()
of = open(out_html_file, mode='w', encoding = 'utf-8')
of.write(prettyHTML)
of.close()
