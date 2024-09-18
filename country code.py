country_code = {
    'India' : '0091',
    'Australia' : '0025',
    'Nepal' : '00977',
    'Bangladesh' : '00880',
}

print("Country code for India -")
print(country_code.get('India', 'Not found'))

print("Country code for Japan -")
print(country_code.get('Japan', 'Not found'))

print("Country code for Bangladesh -")
print(country_code.get('Bangladesh', 'Not found'))