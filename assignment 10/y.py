#




class Data :
    def __init__(self,day,month,year) :
        self.dey=day
        self.month=month
        self.year=year
    
    def show (self,data1):
        print("Date entered:", data1 )

    def add (self,data1,data2):
        Command=input("Do you want to combine or subtract now?")
        if Command == "combine":
             print(data1.sum(data2))
        if Command == "subtract":
             print(data1.minus(data2))

    def GetMonthName (self,data3):
        if data3 == "1":
            print("January")
        elif data3 == "2":
            print("February")
        elif data3 == "3":
            print("March")
        elif data3 == "4":
            print("April")
        elif data3 == "5":
            print("May")
        elif data3 == "6":
            print("June")
        elif data3 == "7":
            print("July")
        elif data3 == "8":
            print("August")
        elif data3 == "9":
            print("September")
        elif data3 == "10":
            print("October")
        elif data3 == "11":
            print("November")
        elif data3 == "12":
            print("December")
        else :
            print("You are wrong, brother")
    def IsLeapYear ():
        pass
    def IsValidDate (self,day,month,year):

        if 1 >= day <= 30 : 
            print ("False!")
        if 1 >= month <= 12 :
            print("False!")
        if 1 >= year <=9999 :
            print("False!")


data1=Data(int(input("1.1.year?")),int(input("2.1.month?")),int(input("3.1.day?")))
data2=Data(int(input("1.2.year?")),int(input("2.2.month?")),int(input("2.3.day?")))
data3=Data(int(input("What month is it?")))