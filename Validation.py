
def presenceCheck(dataEntry):
    while (dataEntry == ''): 
        dataEntry = input('Enter name: ')

def main():
    dataEntry = input('Enter name: ')
    presenceCheck(dataEntry)



if (__name__=="__main__"):
    main()
