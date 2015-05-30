#############################
# Tae Kim
#
#
# Matrix Builder from csv  
#
# When a csv is generated, remove all the spaces, symbols, & characters (use REGEX)
# and add --> "CASEID","WORK_1","ISY","FS","STAR","UPK","SCHMREDUCE","CC","HS","DHE","BASICSTAR","CSFP","PHI_FAM","SUMM","EITC","CTC","SCHE","WIC","HEALTHY_NY","SCHMFREE","VE","PHI","SYEP","SCHMFULL","NYSUI","OST","SECT8","HEAP_OBJTV","RES","PA","SES","EnSTAR","SCRIE","DRIE","FPBP_OBJTV","CDCTC","NFP"
# to give each column names to be used as pandas input file. 
#
# This will take time to run since it is not written for efficiency.
# 
##############################


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


if __name__ == "__main__":
    programSelection ="programSelection_PRD.csv"
    step1Result = "step1Results_PRD.csv"
 #   step1Hhold = "step1HholdData_PRD.csv"
 #   stepClean = "resultOne_TKmade.csv"
    
    
#     programSelectionPD = pd.read_csv(programSelection)
    step1ResultPD = pd.read_csv(step1Result)   #3 columns
    #step1HholdPD = pd.read_csv(step1Hhold) 
    #step1CleanPD = pd.read_csv(stepClean)
    
    #print len(step1CleanPD)
#     
#     t= step1ResultPD.groupby('CASEID')  
#     print t.count()
    
    
    #for name, group in t:
     #   print group['OBJECTIVEID'].count()
    groupedR = step1ResultPD.groupby('CASEID')
    
    
    thisN={}
    for name, groups in groupedR: 
         if name in thisN:
            if groups["OBJECTIVEID"].str.contains('HEALTHY_NY').any() == True:
                thisN[name]['HEALTHY_NY']=1
            if groups["OBJECTIVEID"].str.contains('SECT8').any() == True:
                thisN[name]['SECT8']=1
            if groups["OBJECTIVEID"].str.contains('PHI').any() == True:
                thisN[name]['PHI']=1
            if groups["OBJECTIVEID"].str.contains('CC').any() == True:
                thisN[name]['CC']=1
            if groups["OBJECTIVEID"].str.contains('OST').any() == True:
                thisN[name]['OST']=1
            if groups["OBJECTIVEID"].str.contains('FS').any() == True:
                thisN[name]['FS']=1
            if groups["OBJECTIVEID"].str.contains('EITC').any() == True:
                thisN[name]['EITC']=1
            if groups["OBJECTIVEID"].str.contains('CTC').any() == True:
                thisN[name]['CTC']=1
            if groups["OBJECTIVEID"].str.contains('CDCTC').any() == True:
                thisN[name]['CDCTC']=1
            if groups["OBJECTIVEID"].str.contains('UPK').any() == True:
                thisN[name]['UPK']=1
            if groups["OBJECTIVEID"].str.contains('PHI_FAM').any() == True:
                thisN[name]['PHI_FAM']=1
            if groups["OBJECTIVEID"].str.contains('STAR').any() == True:
                thisN[name]['STAR']=1
            if groups["OBJECTIVEID"].str.contains('PA').any() == True:
                thisN[name]['PA']=1
            if groups["OBJECTIVEID"].str.contains('SCRIE').any() == True:
                thisN[name]['SCRIE']=1
            if groups["OBJECTIVEID"].str.contains('HS').any() == True:
                thisN[name]['HS']=1
            if groups["OBJECTIVEID"].str.contains('DRIE').any() == True:
                thisN[name]['DRIE']=1
            if groups["OBJECTIVEID"].str.contains('SCHE').any() == True:
                thisN[name]['SCHE']=1
            if groups["OBJECTIVEID"].str.contains('BASICSTAR').any() == True:
                thisN[name]['BASICSTAR']=1
            if groups["OBJECTIVEID"].str.contains('SCHMFULL').any() == True:
                thisN[name]['SCHMFULL']=1
            if groups["OBJECTIVEID"].str.contains('VE').any() == True:
                thisN[name]['VE']=1
            if groups["OBJECTIVEID"].str.contains('NYSUI').any() == True:
                thisN[name]['NYSUI']=1
            if groups["OBJECTIVEID"].str.contains('SUMM').any() == True:
                thisN[name]['SUMM']=1
            if groups["OBJECTIVEID"].str.contains('SCHMFREE').any() == True:
                thisN[name]['SCHMFREE']=1
            if groups["OBJECTIVEID"].str.contains('WIC').any() == True:
                thisN[name]['WIC']=1
            if groups["OBJECTIVEID"].str.contains('HEAP_OBJTV').any() == True:
                thisN[name]['HEAP_OBJTV']=1
            if groups["OBJECTIVEID"].str.contains('EnSTAR').any() == True:
                thisN[name]['EnSTAR']=1
            if groups["OBJECTIVEID"].str.contains('SCHMREDUCE').any() == True:
                thisN[name]['SCHMREDUCE']=1
            if groups["OBJECTIVEID"].str.contains('DHE').any() == True:
                thisN[name]['DHE']=1
            if groups["OBJECTIVEID"].str.contains('CSFP').any() == True:
                thisN[name]['CSFP']=1
            if groups["OBJECTIVEID"].str.contains('WORK_1').any() == True:
                thisN[name]['WORK_1']=1
            if groups["OBJECTIVEID"].str.contains('RES').any() == True:
                thisN[name]['RES']=1
            if groups["OBJECTIVEID"].str.contains('NFP').any() == True:
                thisN[name]['NFP']=1
            if groups["OBJECTIVEID"].str.contains('SES').any() == True:
                thisN[name]['SES']=1
            if groups["OBJECTIVEID"].str.contains('ISY').any() == True:
                thisN[name]['ISY']=1
            if groups["OBJECTIVEID"].str.contains('SYEP').any() == True:
                thisN[name]['SYEP']=1
            if groups["OBJECTIVEID"].str.contains('FPBP_OBJTV').any() == True:
                thisN[name]['FPBP_OBJTV']=1
            else:
                pass
         else:
            thisN[name]={'HEALTHY_NY':0, 'SECT8':0, 'PHI':0, 'CC':0 ,'OST':0, 'FS':0, 'EITC':0, 'CTC':0, 
                          'CDCTC':0, 'UPK':0, 'PHI_FAM':0, 'STAR':0 ,'PA':0, 'SCRIE':0, 'HS':0 ,'DRIE':0,'SCHE':0,
                          'BASICSTAR':0, 'SCHMFULL':0,'VE':0 ,'NYSUI':0 ,'SUMM':0 ,'SCHMFREE':0, 'WIC' :0,
                           'HEAP_OBJTV':0, 'EnSTAR':0 ,'SCHMREDUCE':0,'DHE':0, 'CSFP':0, 'WORK_1':0 ,'RES' :0,
                            'NFP':0, 'SES':0 ,'ISY':0, 'SYEP' :0,'FPBP_OBJTV':0}
            if groups["OBJECTIVEID"].str.contains('HEALTHY_NY').any() == True:
                thisN[name]['HEALTHY_NY']=1
            if groups["OBJECTIVEID"].str.contains('SECT8').any() == True:
                thisN[name]['SECT8']=1
            if groups["OBJECTIVEID"].str.contains('PHI').any() == True:
                thisN[name]['PHI']=1
            if groups["OBJECTIVEID"].str.contains('CC').any() == True:
                thisN[name]['CC']=1
            if groups["OBJECTIVEID"].str.contains('OST').any() == True:
                thisN[name]['OST']=1
            if groups["OBJECTIVEID"].str.contains('FS').any() == True:
                thisN[name]['FS']=1
            if groups["OBJECTIVEID"].str.contains('EITC').any() == True:
                thisN[name]['EITC']=1
            if groups["OBJECTIVEID"].str.contains('CTC').any() == True:
                thisN[name]['CTC']=1
            if groups["OBJECTIVEID"].str.contains('CDCTC').any() == True:
                thisN[name]['CDCTC']=1
            if groups["OBJECTIVEID"].str.contains('UPK').any() == True:
                thisN[name]['UPK']=1
            if groups["OBJECTIVEID"].str.contains('PHI_FAM').any() == True:
                thisN[name]['PHI_FAM']=1
            if groups["OBJECTIVEID"].str.contains('STAR').any() == True:
                thisN[name]['STAR']=1
            if groups["OBJECTIVEID"].str.contains('PA').any() == True:
                thisN[name]['PA']=1
            if groups["OBJECTIVEID"].str.contains('SCRIE').any() == True:
                thisN[name]['SCRIE']=1
            if groups["OBJECTIVEID"].str.contains('HS').any() == True:
                thisN[name]['HS']=1
            if groups["OBJECTIVEID"].str.contains('DRIE').any() == True:
                thisN[name]['DRIE']=1
            if groups["OBJECTIVEID"].str.contains('SCHE').any() == True:
                thisN[name]['SCHE']=1
            if groups["OBJECTIVEID"].str.contains('BASICSTAR').any() == True:
                thisN[name]['BASICSTAR']=1
            if groups["OBJECTIVEID"].str.contains('SCHMFULL').any() == True:
                thisN[name]['SCHMFULL']=1
            if groups["OBJECTIVEID"].str.contains('VE').any() == True:
                thisN[name]['VE']=1
            if groups["OBJECTIVEID"].str.contains('NYSUI').any() == True:
                thisN[name]['NYSUI']=1
            if groups["OBJECTIVEID"].str.contains('SUMM').any() == True:
                thisN[name]['SUMM']=1
            if groups["OBJECTIVEID"].str.contains('SCHMFREE').any() == True:
                thisN[name]['SCHMFREE']=1
            if groups["OBJECTIVEID"].str.contains('WIC').any() == True:
                thisN[name]['WIC']=1
            if groups["OBJECTIVEID"].str.contains('HEAP_OBJTV').any() == True:
                thisN[name]['HEAP_OBJTV']=1
            if groups["OBJECTIVEID"].str.contains('EnSTAR').any() == True:
                thisN[name]['EnSTAR']=1
            if groups["OBJECTIVEID"].str.contains('SCHMREDUCE').any() == True:
                thisN[name]['SCHMREDUCE']=1
            if groups["OBJECTIVEID"].str.contains('DHE').any() == True:
                thisN[name]['DHE']=1
            if groups["OBJECTIVEID"].str.contains('CSFP').any() == True:
                thisN[name]['CSFP']=1
            if groups["OBJECTIVEID"].str.contains('WORK_1').any() == True:
                thisN[name]['WORK_1']=1
            if groups["OBJECTIVEID"].str.contains('RES').any() == True:
                thisN[name]['RES']=1
            if groups["OBJECTIVEID"].str.contains('NFP').any() == True:
                thisN[name]['NFP']=1
            if groups["OBJECTIVEID"].str.contains('SES').any() == True:
                thisN[name]['SES']=1
            if groups["OBJECTIVEID"].str.contains('ISY').any() == True:
                thisN[name]['ISY']=1
            if groups["OBJECTIVEID"].str.contains('SYEP').any() == True:
                thisN[name]['SYEP']=1
            if groups["OBJECTIVEID"].str.contains('FPBP_OBJTV').any() == True:
                thisN[name]['FPBP_OBJTV']=1
            else:
                pass
            
    with open('resultOne_TKmade333.csv','wb') as f:
        w = csv.writer(f)
        w.writerows(thisN.items())
#      
