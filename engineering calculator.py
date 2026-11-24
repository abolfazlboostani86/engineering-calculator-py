import math as riazi

def jam(a, b):
    return a + b

def tafrigh(a, b):
    return a - b

def zarb(a, b):
    return a * b

def taghsim(a, b):
    if b == 0:
        return "Taghsim bar sefr mamnoo ast!"
    return a / b

def tavan(a, b):
    return a ** b

def baghimande(a, b):
    if b == 0:
        return "Taghsim bar sefr mamnoo ast!"
    return a % b

def sin(a):
    return riazi.sin(riazi.radians(a))

def cos(a):
    return riazi.cos(riazi.radians(a))

def tan(a):
    if a % 180 == 90:
        return "Tarif nashode ast!"
    return riazi.tan(riazi.radians(a))

def cot(a):
    if a % 180 == 0:
        return "Tarif nashode ast!"
    return 1 / riazi.tan(riazi.radians(a))

def factoriel(a):
    if a < 0 or not a.is_integer():
        return "Adad sahih vared konid!"
    return riazi.factorial(int(a))

def jazr(a):
    if a < 0:
        return "Adad manfi nemitavanad jazr dashte bashad!"
    return riazi.sqrt(a)

def logaritm(a):
    if a <= 0:
        return "Adad bayad mosbat bashad!"
    return riazi.log10(a)


while True:
    print("\nMashin Hesab Mohandesi")
    print("1. Jam")
    print("2. Tafrigh")
    print("3. Zarb")
    print("4. Taghsim")
    print("5. Tavan")
    print("6. Baghimande")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Cot")
    print("11. Factoriel")
    print("12. Jazr")
    print("13. Logaritm")
    print("0. Khorooj")

    entekhab = input("Entekhab konid: ")

    if entekhab == "0":
        print("Khoda negahdar!")
        break

    if entekhab not in ["1", "2", "3", "4", "5", "6",
                        "7", "8", "9", "10", "11", "12", "13"]:
        print("Entekhab eshtebah ast!")
        continue

    if entekhab in ["1", "2", "3", "4", "5", "6"]:
        adad1 = float(input("Adad aval: "))
        adad2 = float(input("Adad dovom: "))
    else:
        adad1 = float(input("Adad ra vared konid: "))

    match entekhab:
        case "1":
            natije = jam(adad1, adad2)
        case "2":
            natije = tafrigh(adad1, adad2)
        case "3":
            natije = zarb(adad1, adad2)
        case "4":
            natije = taghsim(adad1, adad2)
        case "5":
            natije = tavan(adad1, adad2)
        case "6":
            natije = baghimande(adad1, adad2)
        case "7":
            natije = sin(adad1)
        case "8":
            natije = cos(adad1)
        case "9":
            natije = tan(adad1)
        case "10":
            natije = cot(adad1)
        case "11":
            natije = factoriel(adad1)
        case "12":
            natije = jazr(adad1)
        case "13":
            natije = logaritm(adad1)

    print("Natije mohasebe:")
    print(natije)

    dobare = input("Mohasebe jadid? (y/n): ")

    if dobare == "n":
        print("Barname baste shod!")
        break
    elif dobare == "y":
        continue