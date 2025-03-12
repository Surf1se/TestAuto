#anagrams

str1 = input("srt1 = ")
str2 = input("str2 = ")

str1 = str1.lower()
str2 = str2.lower()


count = 0
if (len(str1) == len(str2)):
    for i in range(0, len(str1)):
        for k in range(0, len(str2)):
            if (str1[i] == str2[k]):
                count += 1
    if count != len(str1):
        print("its not anopgrams")
    else:
        print("its anograms")

else:
    print("Слова не равны по длине")