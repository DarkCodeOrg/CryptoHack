
def convert(s):
  
    # initialization of string to ""
    new = ""
  
    # traverse in the string 
    for x in s:
        new += x 
  
    # return string 
    return new
      
      


string = 'label'

to_array = [char for char in string]

for i in range(len(to_array)):
    to_array[i] = ord(to_array[i])


for i in range(len(to_array)):
    to_array[i] = to_array[i] ^ 13

for i in range(len(to_array)):
    to_array[i] = chr(to_array[i])

print("crypto[{}]".format(convert(to_array)))




