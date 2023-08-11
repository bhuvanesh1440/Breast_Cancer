import xlwt;
from datetime import datetime;
from xlrd import open_workbook;
from xlsxwriter import Workbook;
from xlutils.copy import copy
from pathlib import Path

def output(ct,ucsize,ucshape,ma,secs,bn,bc,nn,mi):
    my_file = Path('test.xlsx');
    if my_file.is_file():
        rb = open_workbook('test.xlsx');
        book = copy(rb);
        sh = book.get_sheet(0)
        # file exists
    else:
        book = xlwt.Workbook()
        sh = book.add_sheet(sheet)

    sh.write(num,0,int(ct));
    sh.write(num,1,int(ucsize));
    sh.write(num,2,int(ucshape));
    sh.write(num,3,int(ma));
    sh.write(num,4,int(secs));
    sh.write(num,5,int(bn));
    sh.write(num,6,int(bc));
    sh.write(num,7,int(nn));
    sh.write(num,8,int(mi));
    
    #sh.write(num+1, 2, present);
    #You may need to group the variables together
    #for n, (v_desc, v) in enumerate(zip(desc, variables)):
    fullname='test.xlsx';
    book.save(fullname)
    return fullname;
