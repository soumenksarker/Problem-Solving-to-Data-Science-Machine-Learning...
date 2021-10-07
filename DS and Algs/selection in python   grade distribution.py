score = int(input("plz enter a number"))
if score<0:
    print("Sorry u just enterd a non positive number")
else:
   if score >= 90:
      print('A')
   else:
        if score >= 80:
             print('B')
        else:
            if score >= 70:
                    print('C')
            else:
                if score >= 60:
                    print('D')
                else:
                    print("U just fail in the exam")
