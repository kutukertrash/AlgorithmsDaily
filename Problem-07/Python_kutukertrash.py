# Name : Hyim
# College Name : ITK
# Year/Department : 2nd/CSE
# E-Mail Id : ktkrtsh@gmail.com

def roman_decimal(inp):
    a = list(inp)
    ans = 0
    for i in range(len(a)):
        if a[i] == "I":
            ans += 1
        elif a[i] == "V":
            ans += 5
        elif a[i] == "X":
            ans += 10
        elif a[i] == "L":
            ans += 50
        elif a[i] == "C":
            ans += 100
        elif a[i] == "D":
            ans += 500
        elif a[i] == "M":
            ans += 1000
    return ans
print(roman_decimal("MMXXI"))