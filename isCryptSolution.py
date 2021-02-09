def isCryptSolution(crypt, solution):
    encList = []
    for string in crypt:
        if encrypt(string,solution) == False:
            return False
        else : 
            encList.append(int(encrypt(string,solution)))
        
    if(encList[0]+encList[1]) == encList[2]:
        return True
    else :
        return False
 
# Text to Number encryption        
def encrypt(string, solution):
    encryptedText=""
    for i in range(len(string)):
        for j in range(len(solution)):                    
            if string[i] == solution[j][0]:
                encryptedText = encryptedText + solution[j][1]
    
   
    #Zero can be placed first when the lenth of the text is 1
    #Otherwise, return False
    if len(encryptedText)!=1 and encryptedText[0] =='0':
        return False
    else :
        return encryptedText
    
