#############################
# Tae Kim
#
#
# Plotter   
#
##############################

import csv
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np


if __name__ == "__main__":
    programSelection ="programSelection_PRD.csv"
    step1Result = "step1Results_PRD.csv"
    step1Hhold = "step1HholdData_PRD.csv"
    stepClean = "resultOne_TKmade.csv"
    
    programSelectionPD = pd.read_csv(programSelection)
    step1ResultPD = pd.read_csv(step1Result)   #3 columns
    step1HholdPD = pd.read_csv(step1Hhold) 
    joinedR = pd.read_csv(stepClean)
    thisList= list(joinedR.columns.values)
    fig = plt.figure(figsize=(14, 8), dpi=90)
    ax1 = plt.subplot(111) 
    #for i in thisList[1:]:
    #    print i, joinedR[i].sum()
    plt.bar(xrange(len(thisList[1:])), [joinedR[i].sum() for i in thisList[1:]], width=0.7, color=['#a6d96a','#2c7bb6','#f03b20'], align='center')
    ax1.set_xlim([-0.5, len(thisList[1:])])
    ax1.set_xticks([x for x in xrange(len(thisList[1:]))])
    ax1.set_xticklabels([x for x in thisList[1:]])
    
    for i, j in enumerate(thisList[1:]):
        ax1.annotate("%d, %.2f" %(joinedR[j].sum(), int(joinedR[j].sum())/float(752873)), (i,joinedR[j].sum()), va='bottom', ha='center', rotation=90, size=10)
    plt.xticks(rotation=90)
    ax1.set_xlabel('Overall Step 1 by Benefits - 752,873 records')
    
    plt.tight_layout()
    plt.show()
    
    