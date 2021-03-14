
import os
import pandas as pd


def create_training_text(sheets):

    #fileList = os.listdir("audio-original")
    for sheet in sheets:
        excel = pd.read_excel("Audio IDs.xlsx",sheet_name=sheet,usecols="B:C")
        #print(fileList)
        #print(excel.values[0])
        #print(excel.values[0][0])

        with open("audio-original/training-text.txt","a") as f:
            for row in excel.values:
                if(pd.isna(row[1]) or pd.isna(row[0])):
                    print(str(row[0])+": TEXT EMPTY")
                    continue
                #print(str(row[0])+".ogg"+"\t"+row[1])
                f.write(str(row[0])+".ogg"+"\t"+row[1]+"\n")

    




