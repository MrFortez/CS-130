def test():
    x = input("give num  ")
    print("epic")
    print(x)
    num = x
    try:
        x = float(x)
    except:
        print("no")
        return test()
    else:
        return num
    
print(test())
        
