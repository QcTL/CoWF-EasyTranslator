import csv

srcFileToTranslate = "FObjCode"
stcFileCsvObjects = "FObjProduced"

with open(f"{srcFileToTranslate}.txt", "r") as file:
    linesFile = file.readlines()

totalObjectsValues = dict()
with open(f"{stcFileCsvObjects}.csv", newline='') as csvfile:
    csv_reader = csv.reader(csvfile)
    for i, row in enumerate(csv_reader):
        totalObjectsValues[row[0]] = i

linesWordsFiles = [string.split() for string in linesFile]

dicTransformation = {"jump": "000", "jumpC": "001", "gt": "010", "lt": "011", "load": "100", "loadI": "101",
                     "act": "110", "nop": "111"}
dicLoadValues = {"VAL_UUID": "0000",
                 "VAL_ACTIVELOCATIONS": "0001",
                 "VAL_OWN": "0010",
                 "VAL_RENTEDLOCATIONS": "0011",
                 "VAL_ACTIVEFUNDS": "0100",
                 "VAL_N_OBJECT": "0101",
                 }  # To Fill
dicActValues = {"objProduce": "0000",
                "objBuy": "0001",
                "objSell": "0010",
                "cellBuy": "0011",
                "cellSell": "0100",
                "cellGiveRent": "0101",
                "cellGainRent": "0110",
                }
rCodeResult = []

for lVal in linesWordsFiles:
    lReS = dicTransformation[lVal[0]]
    if lVal[0] == "salt" or lVal[0] == "saltC" or lVal[0] == "loadI":
        lReS += bin(int(lVal[1]))[2:].zfill(61)
    elif lVal[0] == "gt" or lVal[0] == "lt":
        lReS += "0".zfill(60)
    elif lVal[0] == "load":
        lReS += dicLoadValues[lVal[1]].zfill(4)
        if lVal[1] == "VAL_N_OBJECT":
            lReS += bin(int(lVal[2]))[2:].zfill(57)
    elif lVal[0] == "act":
        lReS += dicActValues[lVal[1]].zfill(4)
        if lVal[1] == "objProduce":
            lReS += bin(totalObjectsValues[lVal[2]])[2:].zfill(57)
        elif lVal[1] == "other":
            pass
    rCodeResult.append(lReS.ljust(64, '0'))
print(linesWordsFiles)
for i in rCodeResult:
    print(f"0b{i}")
