#convert to all upper case
def ncLower(string):
        ncList = []
        for char in string:
                ncList.append(char)
        i = 0 # iterator
        for x in ncList:
                int = ord(x)
                if (int > 64 and int < 91):
                        ncList[i] = chr(int+32)
                else:
                        ncList[i] = ncList[i]
                i = i + 1
        string = str(''.join(ncList))
        return string

#convert to all lower case
def ncUpper(string):
        ncList = []
        for char in string:
                ncList.append(char)
        i = 0 # iterator
        for x in ncList:
                int = ord(x)
                if (int > 96 and int < 123):
                        ncList[i] = chr(int-32)
                else:
                        ncList[i] = ncList[i]
                i = i + 1
        string = str(''.join(ncList))
        return string
