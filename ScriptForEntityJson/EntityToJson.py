import xlrd
import xlwt
from xlutils.copy import copy
import os

import json


class EntityToJson:
    def __init__(self):
        proDir = os.path.split(os.path.realpath(__file__))[0]
        xls_name = '病种明细与标签1.3.xls'
        self.xlsPath = os.path.join(proDir,xls_name)
        self.openfile = xlrd.open_workbook(self.xlsPath,'w',formatting_info= True)
        self.newfile = copy(self.openfile)

        self.Disesses = []
        self.disesseid = 1
        self.id = 1

        self.Entity = {}

    def GetWriteEntity(self,sheet_name):
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

    # def SetCell(self,sheet_name,curRowNo,curColNo,value):
    #     newsheet = self.newfile.get_sheet(sheet_name)
    #     newsheet.write(curRowNo,curColNo,value)

    # def Save(self):
    #     self.newfile.save(self.xlsPath)

    # def WriteParentCode(self,curRowNo,s,sheet_name):
    #     code = str(s['code'])
    #     if code[2:6] =='0000':
    #         self.SetCell(sheet_name,curRowNo,2,100000)
    #         self.Save()
    #     if code[2:4] !='00' and code[4:6] =='00' :
    #         parentcode = code[0:2]+'0000'
    #         self.SetCell(sheet_name,curRowNo,2,int(parentcode))
    #         self.Save()
    #     if code[2:4] !='00' and code[4:6] !='00' and code[0:2] !='00':
    #         parentcode = code[0:4]+'00'
    #         self.SetCell(sheet_name,curRowNo,2,int(parentcode))
    #         self.Save()
    
    def GetJson(self,s):
        parentname = str(s['ParentName'])
        childname = str(s['ChildName'])
        disessename = []
        
        for i in range(len(self.Disesses)):
            disessename.append(self.Disesses[i]['Name'])
        
        if parentname in disessename:
            for ii in range(len(self.Disesses)):
                if self.Disesses[ii]['Name'] == parentname:
                    entity = {}
                    entity['Id'] = self.id
                    entity['Name'] = childname
                    self.id = self.id + 1

                    self.Disesses[ii]['Childs'].append(entity)
        else:
            disesse = {}
            disesse['Id'] = self.disesseid
            disesse['Name'] = parentname
            disesse['Childs'] = []

            entity = {}
            entity['Id'] = self.id
            entity['Name'] = childname
            self.id = self.id + 1

            disesse['Childs'].append(entity)
            self.Disesses.append(disesse)
            self.disesseid = self.disesseid + 1

        self.Entity['Disesses'] = self.Disesses

        
    def WriteJson(self):
        with open('Entity.json','w',encoding='utf-8') as json_file:
            json_file.write(json.dumps(self.Entity,ensure_ascii=False))
            
if __name__ == "__main__":
    a = EntityToJson()
    a.GetWriteEntity('病种名称及分类')