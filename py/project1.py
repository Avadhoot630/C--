def game():
    print('|',row[0],'|',row[1],'|',row[2],
          '|',row[3],'|',row[4],'|',row[5],
          '|',row[6],'|',row[7],'|',row[8])

row=['','','','','','','','','']
Ans=''
while Ans!="Yes" or Ans!="No":
    Ans=input("Can we start the game?\n")
    if Ans=="Yes":
        game()
