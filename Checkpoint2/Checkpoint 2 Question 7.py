Price=int(input("Enter a price "))

if Price>500:
    NewPrice=Price*0.5
    print("New price", NewPrice)
elif Price<500 and Price>=200:
    NewPrice=Price*0.7
    print("New price", NewPrice)
elif Price > 200:
    NewPrice=Price*0.9
    print("New price", NewPrice)
