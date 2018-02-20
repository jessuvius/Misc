s=s+"0"
abc = "abcdefghijklmnopqrstuvwxyz0"
lastInd = 0
longSeq = ""
longSeq2 = ""
for letter in s:
	abcInd=0
	for comp in abc:
		abcInd+=1
		if comp == letter:
			if lastInd <= abcInd:
				longSeq=longSeq+letter
				lastInd=abcInd
			if lastInd > abcInd:
				if len(longSeq)>len(longSeq2):
					longSeq2=longSeq
					longSeq=letter
					lastInd=abcInd
				else:
					longSeq=letter
					lastInd=abcInd
print("Longest substring in alphabetical order is: "+longSeq2)
