#get binary 1
getBin1 = lambda arg1: bin(arg1).replace("0b","")

#get binary 2
getBin1 = lambda number : "{0:08b}".format(number)


#get 2,8,16 진수
getBase = lambda number : "{0:#o} {0:#x} {0:#b}".format(number)


#get comma
getComma = lambda number : '{:,}'.format(number)





#print(getBin(10))
# print(getBase(100))

