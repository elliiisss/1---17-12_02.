str_ = ""
n = ""
while n != "stop":
    n = input("введите слово ")
    if n != "stop": str_ = str(str_) + (" ") + n
print(str_)