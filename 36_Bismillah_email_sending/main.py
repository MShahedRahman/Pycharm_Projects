
string_name = input("Please enter a String: ")
print(string_name)

count = 0
for i in range(len(string_name)):
    if string_name[i] == 'a' or string_name[i] == 'A':
       count = count + 1

    elif string_name[i] == 'e' or string_name[i] == 'E':
        count = count + 1

    elif string_name[i] == 'i' or string_name[i] == 'I':
        count = count + 1

    elif string_name[i] == 'o' or string_name[i] == 'O':
        count = count + 1

    elif string_name[i] == 'u' or string_name[i] == 'U':
        count = count + 1

print("The number of vowels is : ", count)