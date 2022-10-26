def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

digi_list =[]
symbols = [',','.','/','?','<','>','/','""',"''",' ','[',']','{','}','|','!','@','#','$','%','^','&','*','(',')','-','+','_','=']

def is_valid(s):
    s= s.lower()
    if s[0:2].isalpha():
        if 2 <= len(s) <= 6:
            for i in s[2:len(s)]:
                digi_list.append(i)
        else:
            return False
    if digi_list[0] == '0':
        return False
    if digi_list[-1].isalnum():
        if s.isalpha():
            return True
        elif digi_list[-2].isalpha() :
            return False
    for i in range(0,len(digi_list)):
        if digi_list[i] in symbols:
            return False
    else:
        return True

main()
