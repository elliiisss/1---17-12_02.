count = int(input("введите количество слов "))
str_ = ""
for i in range(1, count + 1):
    word = input("введите слово ")
    str_ = str(str_)+ (" ") + word
    i = i + 1
print(str_)
