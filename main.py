from passwordList import PG

index = input("""┌──(Master)-[~CUPP tools]
└─$ please enter your Data from Target with space : [None]""")
if index == "":
    targetData = None
else:
    targetData = index
index = input("""┌──(Master)-[~CUPP tools]
└─$ please enter count character of password you need : [8]""")
if index == "":
    countChar = 8
elif index.isdigit():
    countChar = int(index)
else:
    print("""┌──(Master)-[~CUPP tools]
└─$ Your insert is wrong and set default o\\/o: [8]""")
    countChar = 8
index = input("""┌──(Master)-[~CUPP tools]
└─$ please enter count Password you want: [1000]""")
if index == "":
    countPW = 1000
elif index.isdigit():
    countPW = int(index)
else:
    print("""┌──(Master)-[~CUPP tools]
└─$ Your insert is wrong and set default o\\/o: [1000]""")
    countChar = 1000
index = input("""┌──(Master)-[~CUPP tools]
└─$ would you like special character in password? [Y/N]""")
if index == "N" or index == "n":
    speChar = False
elif index == "Y" or index == "y":
    speChar = True
else:
    print("""┌──(Master)-[~CUPP tools]
└─$ Your insert is wrong and set default o\\/o: [N]""")
    speChar = False
index = input("""┌──(Master)-[~CUPP tools]
└─$ please enter directory you want copy the file to it: """)
direc = index

print("""┌──(Master)-[~CUPP tools]
└─$ Password List is creating...""")

operation = PG(targetData, countChar, countPW, speChar, direc)
operation.passwordGenerator()

print(f"""┌──(Master)-[~CUPP tools]
└─$ Your password list in {direc} directory has been created :)""")
