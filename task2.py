print("Please select the type of transaction to be performed")
print("                                                     ")
print("1.Add","\n2.Subtract","\n3.Divide","\n4.Multiply")

selection=input("What is your selection? (1-2-3-4): ")
Number1=int(input("1.Number: "))
Number2=int(input("2.Number: "))

if selection =="1":
    print(Number1,"+",Number2,"=",Number1+Number2)
elif selection =="2":
    print(Number1,"-",Number2,"=",Number1-Number2)
elif selection =="3":
    print(Number1,"*",Number2,"=",Number1*Number2)
elif selection =="4":
    print(Number1,"/",Number2,"=",Number1/Number2)
else:
    print("Faulty selection")

