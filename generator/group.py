import getopt
import sys
import os
import random
import string
import time
from model.group import Group

import clr

clr.AddReferenceByName(
    'Microsoft.Office.Interop.Excel, Version=15.0.0.0, Culture=neutral, PublicKeyToken=71e9bce111e9429c')
from Microsoft.Office.Interop import Excel

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = 'data/groups.xlsx'

for o, a in opts:
    if o == '-n':
        n = int(a)
    elif o == '-f':
        f = a


def random_string(prefix, max_len):
    symbols = string.ascii_letters + string.digits + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(max_len))])


# testdata
test_data = [Group(name="")] + [Group(name=random_string('name', 10)) for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', f)
data = os.path.exists("..\data")
datafile = os.path.isfile("..\data\groups.xlsx")
if data is False:
    mkdir = os.mkdir("..\data")
elif datafile is True:
    os.remove(file)

excel = Excel.ApplicationClass()
excel.Visible = True
workbook = excel.Workbooks.Add()
sheet = workbook.ActiveSheet
for i in range(len(test_data)):
    sheet.Range["A%s" % (i + 1)].Value2 = test_data[i].name
workbook.SaveAs(file)
excel.Quit()
