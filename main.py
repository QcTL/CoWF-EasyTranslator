import csv
import os

srcFolder = "codeFactoryH"
stcFileCsvObjects = "FObjProduced"
txt_files = [f for f in os.listdir(srcFolder) if f.endswith('.txt')]

totalObjectsValues = dict()
with open(f"{stcFileCsvObjects}.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for i, row in enumerate(csv_reader):
        totalObjectsValues[row[0]] = i


dicTransformation = {"jump": "000", "jumpC": "001", "gt": "010", "lt": "011", "load": "100", "loadI": "101",
                     "act": "110", "nop": "111"}
dicLoadValues = {"VAL_UUID": "0000",
                 "VAL_ACTIVELOCATIONS": "0001",
                 "VAL_OWN": "0010",
                 "VAL_RENTEDLOCATIONS": "0011",
                 "VAL_ACTIVEFUNDS": "0100",
                 "VAL_N_OBJECT": "0101",
                 "VAL_NONRENTEDOWNED": "0101",
                 }
dicActValues = {"objProduce": "0000",
                "objBuy": "0001",
                "objSell": "0010",
                "cellBuy": "0011",
                "cellSell": "0100",
                "cellGiveRent": "0101",
                "cellGainRent": "0110",
                }
dicTypeCells = {"CELL_FIELD": "00000110",
                "CELL_FACT": "00000100",
                "CELL_HFACT": "00000101",
                "CELL_CIV_M1": "00000001",
                "CELL_CIV_M2": "00000010",
                "CELL_CIV_M3": "00000011"
                }

for txt_file in txt_files:
    rCodeResult = []
    print("{")
    with open(f"{srcFolder}/{txt_file}", "r") as file:
        linesFile = file.readlines()

    linesWordsFiles = [string.split() for string in linesFile]
    for lVal in linesWordsFiles:
        lReS = dicTransformation[lVal[0]]
        if lVal[0] == "jump" or lVal[0] == "jumpC" or lVal[0] == "loadI":
            lReS += bin(int(lVal[1]))[2:].zfill(61)
        elif lVal[0] == "gt" or lVal[0] == "lt":
            lReS += "0".zfill(60)
        elif lVal[0] == "load":
            lReS += dicLoadValues[lVal[1]].zfill(4)
            if lVal[1] == "VAL_N_OBJECT":
                lReS += bin(totalObjectsValues[lVal[2]])[2:].zfill(57)
        elif lVal[0] == "act":
            lReS += dicActValues[lVal[1]].zfill(4)
            if lVal[1] == "objProduce" or lVal[1] == "objBuy" or lVal[1] == "objSell":
                lReS += bin(totalObjectsValues[lVal[2]])[2:].zfill(57)
            elif lVal[1] == "cellGainRent" or lVal[1] == "cellGiveRent" or lVal[1] == "cellBuy" or lVal[1] == "cellSell":
                lReS += dicTypeCells[lVal[2]][2:].zfill(57)

        rCodeResult.append(lReS.ljust(64, '0'))
    for i in rCodeResult:
        print(f"(uint64_t) 0b{i},")
    print("},")