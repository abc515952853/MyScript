import xlrd
import xlwt
from xlutils.copy import copy
import os

import json


class AreaWd:
    def __init__(self):
        proDir = os.path.split(os.path.realpath(__file__))[0]
        xls_name = 'Area.xls'
        self.xlsPath = os.path.join(proDir,xls_name)
        self.openfile = xlrd.open_workbook(self.xlsPath,'w',formatting_info= True)
        self.newfile = copy(self.openfile)

        self.areaData = []

    def GetWriteArea(self,sheet_name):
        sheet = self.openfile.sheet_by_name(sheet_name)
        row = sheet.row_values(0)
        rowNum  = sheet.nrows
        colNum = sheet.ncols 
        
        curRowNo = 1
        while self.HasNext(rowNum,curRowNo):
            s = {}  
            col = sheet.row_values(curRowNo)  
            i = colNum  
            for x in range(i):
                s[row[x]] =  self.ConversionCell(sheet,curRowNo,x,col[x])
            # self.WriteParentCode(curRowNo,s,sheet_name)
            self.GetJson(s)
            curRowNo += 1
        self.WriteJson()

    def HasNext(self,rownum,curRowNo):  
        if rownum == 0 or rownum <= curRowNo :  
            return False  
        else:  
            return True  

    def ConversionCell(self,sheet,curRowNo,curColNo,cell):
        if sheet.cell(curRowNo,curColNo).ctype == 2:
             no = int(cell)
        else:
             no = cell
        return no

    def SetCell(self,sheet_name,curRowNo,curColNo,value):
        newsheet = self.newfile.get_sheet(sheet_name)
        newsheet.write(curRowNo,curColNo,value)

    def Save(self):
        self.newfile.save(self.xlsPath)

    def WriteParentCode(self,curRowNo,s,sheet_name):
        code = str(s['code'])
        if code[2:6] =='0000':
            self.SetCell(sheet_name,curRowNo,2,100000)
            self.Save()
        if code[2:4] !='00' and code[4:6] =='00' :
            parentcode = code[0:2]+'0000'
            self.SetCell(sheet_name,curRowNo,2,int(parentcode))
            self.Save()
        if code[2:4] !='00' and code[4:6] !='00' and code[0:2] !='00':
            parentcode = code[0:4]+'00'
            self.SetCell(sheet_name,curRowNo,2,int(parentcode))
            self.Save()
    
    def GetJson(self,s):
        code = str(s['code'])
        name = str(s['name'])
        parentcode = str(s['parentcode'])
        if code[2:6] =='0000':
            AreaProvince = {'name':name,'code':code,'sub':[]}
            self.areaData.append(AreaProvince)
            return
        if code[2:4] !='00' and code[4:6] =='00':
            AreaCity = {'name':name,'code':code,'sub':[]}
            for i in range(0, len(self.areaData)):  
                if parentcode == self.areaData[i]['code']:
                    self.areaData[i]['sub'].append(AreaCity)
            return          
        if code[2:4] !='00' and code[4:6] !='00' and code[0:2] !='00':
            AreaConutry = {'name':name,'code':code}
            for i in range(0, len(self.areaData)):
                for ii in range(0,len(self.areaData[i]['sub'])):
                    if parentcode == self.areaData[i]['sub'][ii]['code']:
                        self.areaData[i]['sub'][ii]['sub'].append(AreaConutry)
            return
    
    def WriteJson(self):
        with open('data.json','w',encoding='utf-8') as json_file:
            json_file.write(json.dumps(self.areaData,ensure_ascii=False))
            
if __name__ == "__main__":
    a = AreaWd()
    print('11')
    AreaData =a.GetWriteArea('Area')