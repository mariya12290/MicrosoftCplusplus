print(type("suri"))

print(len("suri"))

#string concatenation
string1 ="suri"
string2 =" kumar"

string3 = string1 + string2
print(string3)

print(string1+" "+string2)

#indexing

for i in range(len(string3)):
    print(string3[i])

#negative indexing  -1,-2,-3,-4
print(string3[-1]) #prints r

#string slicing
print(string3[0:3])
print(string3[:5])
print(string3[5:])

#string are immutable
#string3[0] = 'p' #no possible
string3  ="p"+string3[1:]
print(string3)

print(string3.upper())

print(string3.lower())

#striping
string4 = "   Suri Kumar  "
string5 = string4
string6 = string4
print(string4.strip())
print(string5.lstrip())
print(string6.rstrip())


print(string3.startswith("Su"))

print(string3.endswith("ar"))


#user_input = input(string3)
#print("User said: ",user_input)

#string arithmetic operation


#find a string in a string

phrase = "I  am suri"
print(phrase.find("monday"))

phrase ="I am telling you the truth, not but the truth"

phrase  = phrase.replace("the truth", "lies")
print(phrase)