import random
import string
import os
import itertools


class PG:
    
    passwords = []


    strChar = []
    numChar = ['2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023','2024','2025']
    sChar = list(string.punctuation)

    # symbols = {
    #     "4":["a", "A"],
    #     "3":["e", "E"],
    #     "5":["s", "S"],
    #     "9":["g", "q"],
    #     "6":"G",
    #     "0":["o", "O"],
    #     "2":["z", "Z"],
    #     "8":"B",
    #     "1":["i", "I", "l"],
    #     "7":["t", "T"]
    # }


    def __init__(self, targetData, countChar, countPW, speChar, direc):
        self.targetData = targetData
        self.countChar = countChar
        self.countPW = countPW
        self.speChar = speChar
        self.direc = direc
    
    @staticmethod
    def randomChar(dataType, length):
        char = string.ascii_lowercase
        number = string.digits
        specialChar = string.punctuation
        if dataType == "character":
            return "".join(random.choices(char, k=length))
        elif dataType == "number":
            return "".join(random.choices(number, k=length))
        elif dataType == "specialChar":
            return "".join(random.choices(specialChar, k=length))

    @staticmethod
    def allForms(list, type):
        forms = []
        for element in list:
            i = 1
            while i <= len(element):
                forms.append(element[:i])
                i += 1
        if type == "character":
            PG.strChar.extend(forms)
        elif type == "number":
            PG.numChar.extend(forms)

    def createChar(self, data):
        # for seprate data
        strList = []
        numList = []
        Data = data.split()
        for item in Data:
            if item.isalpha():
                strList.append(item)
            elif item.isdigit():
                numList.append(item)

        if len(strList) == 0:
            for i in range(10):
                item = PG.randomChar("character", self.countChar)
                strList.append(item)
        elif len(numList) == 0:
            for i in range(3):
                item = PG.randomChar("number", self.countChar)
                numList.append(item)
        # create all of forms text from splited data
        PG.allForms(strList, "character")
        PG.allForms(numList, "number")
    
    def fileMaker(self):
        directory = self.direc
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, "PasswordList.txt")
        if not os.path.exists(file_path):
            file_pw = open(file_path, "x")
            file_pw.close()
        else:
            file_pw = open(file_path, "w")
            file_pw.close()

        return file_path
    
    def createPermutations(self, data_exist, Schar_exist):
        permutation = []
        if data_exist:
            if data_exist and Schar_exist:
                combination = [[x, y] for x in self.strChar for y in self.numChar]
                condition = False
                for combo in combination:
                    if len("".join(combo)) == (self.countChar-1):
                        for perm in itertools.permutations(combo, 2):
                            if len(self.passwords) < self.countPW:
                                self.passwords.append((''.join(perm) + random.choice(self.sChar)).capitalize())
                            else:
                                condition = True
                                break
                        if condition:
                            break
                
                while len(self.passwords) < self.countPW:
                    countStr = random.randint(0, self.countChar)
                    string = random.choice(self.strChar)[:countStr]
                    countNum = random.randint(0, (self.countChar - countStr))
                    number = PG.randomChar("number", countNum)
                    specialChar = PG.randomChar("specialChar", (self.countChar - (countNum + countStr)))
                    password = (string + number + specialChar).capitalize()
                    if password not in self.passwords and len(password) == self.countChar:
                        self.passwords.append(password)

            elif data_exist and not(Schar_exist):
                combination = [[x, y] for x in self.strChar for y in self.numChar]
                condition = False
                for combo in combination:
                    if len("".join(combo)) == self.countChar:
                        for perm in itertools.permutations(combo, 2):
                            if len(self.passwords) < self.countPW:
                                self.passwords.append((''.join(perm)).capitalize())
                            else:
                                condition = True
                                break
                        if condition:
                            break   

                while len(self.passwords) < self.countPW:
                    countStr = random.randint(0, self.countChar)
                    string = random.choice(self.strChar)[:countStr]
                    number = PG.randomChar("number", (self.countChar - countStr))
                    password = (string + number).capitalize()
                    if password not in self.passwords and len(password) == self.countChar:
                        self.passwords.append(password) 
        else:
            if not(data_exist) and Schar_exist:
                while len(self.passwords) < self.countPW:
                    countStr = random.randint(0, self.countChar)
                    string = PG.randomChar("character", countStr)
                    countNum = random.randint(0, (self.countChar - countStr))
                    number = PG.randomChar("number", countNum)
                    specialChar = PG.randomChar("specialChar", (self.countChar - (countNum + countStr)))
                    password = (string + number + specialChar).capitalize()
                    if password not in self.passwords and len(password) == self.countChar:
                        self.passwords.append(password)
            elif not(data_exist) and not(Schar_exist):
                while len(self.passwords) < self.countPW:
                    countStr = random.randint(0, self.countChar)
                    string = PG.randomChar("character", countStr)
                    number = PG.randomChar("number", (self.countChar - countStr))
                    password = (string + number).capitalize()
                    if password not in self.passwords and len(password) == self.countChar:
                        self.passwords.append(password) 


    def passwordGenerator(self):
        if self.targetData != None:
            self.createChar(self.targetData)
            if self.speChar is False:
                self.createPermutations(True, False)
            else:
                self.createPermutations(True, True)
        else:
            if self.speChar is False:
                self.createPermutations(False, False)
            else:
                self.createPermutations(False, True)

        filePath = self.fileMaker()
        file = open(filePath, "w")
        for password in self.passwords:
            file.write(password + "\n")
        file.close()
