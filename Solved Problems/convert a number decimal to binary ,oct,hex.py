dec = int(input("please  enter a decimal number:"))
x = int(input("please choose what u wanna want Press1.Dec to binary\n Press 2:  dec to octal\n Press 3: dec to hexadecimal"))
if x == 1:
  print(bin(dec),"in binary.")
elif x==2:
  print(oct(dec),"in octal.")
elif x==3:
  print(hex(dec),"in hexadecimal.")
