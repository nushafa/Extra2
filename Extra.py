str1 = input("Please enter a sentence: ")
total = 1

for i in range(len(str1)):
    if str1[i] == ' ':
        total = total + 1
print("Total number of words in the string:", total)