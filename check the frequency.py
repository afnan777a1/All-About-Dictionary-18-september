test_dict = {
    'codingal' : 3,
    'is' : 2,
    'best' : 2,
    'for' : 2,
    'coding' : 1,
}


print("the original dictionary : " + str(test_dict))


K = int(input("Enter the frequency : "))
res = 0

for key in test_dict:
    if test_dict[key] == K:
        res = res + 1

print("Frequency of K is : ", res)