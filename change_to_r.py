import csv
import os

inputFileName = "prosperLoanData.csv"
outputFileName = os.path.splitext(inputFileName)[0] + "_modified.csv"

def convert_to_r(x):
	y = x[0].lower()
	for i in range(1,len(x)):
		if (not x[i].isupper()) :
			y = y + str(x[i])
		else:
			y = y + str('.') + str(x[i]).lower()
	return y

with open(inputFileName) as inFile, open(outputFileName, 'w') as outfile:
    r = csv.reader(inFile)
    w = csv.writer(outfile)

    new_header = list()

    x = next(r, None)  # skip the first row from the reader, the old header
    for item in x:
    	new_header.append(convert_to_r(item))
    print(new_header)
    # write new header
    w.writerow(new_header)

    # copy the rest
    for row in r:
        w.writerow(row)