import sys
def update(new): #user defined function to show the updated tic-tac 
      print(new[0:3])
      print(new[3:6])
      print(new[6:9])

flag=1
new=[]
rows, cols = (3, 3)#rows and columns are 3,3 
arr = [[0]*cols]*rows #defining 2d matrix of order 3
 
new=[j for sub in arr for j in sub] #converting 2d array to 1d array
print("Welcome to the game!\n") #entering the game
while(flag!=0):


 ########Player 1############################################

 print("\nPlayer 1's chance\n") #Player 1 chance
 print("Enter the position and number to be entered:")
 p,n=input().split() #enter position and number
 p=int(p)
 n=int(n)
 if p<1 and p>9:
     print("Enter correct position!!\n") #Checking position
     continue
 if n==2 or n==4 or n==6 or n==8 or n<1 or n>9: #Checking number
     print("Enter correct number!!\n")
     continue
 new[int(p)-1]=int(n) #updating 1d array
 update(new) #calling to print 2d array
 if (new[0]+new[3]+new[6]==15) or (new[1]+new[4]+new[7]==15) or (new[2]+new[5]+new[8]==15) or (new[0]+new[1]+new[2]==15) or (new[3]+new[4]+new[5]==15) or (new[6]+new[7]+new[8]==15) or (new[0]+new[4]+new[8]==15) or (new[2]+new[4]+new[6]==15):
  print("Player 1 is the winner\n")
  flag=0
  sys.exit()
  

 #################Player 2#############################################
 
 print("\nPlayer 2's chance\n") #Player 2 chance
 print("Enter the position and number to be entered:") #enter position and number
 p,n=input().split()
 p=int(p)
 n=int(n)
 if p<1 and p>9: #checking position
       print("Enter correct position!!\n")
       continue
 if n==1 or n==3 or n==5 or n==7 or n==9 or n<1 or n>9:#checking number
       print("Enter correct number!!\n")
       continue
 new[int(p)-1]=int(n) #updating 1d array
 update(new) #calling to print 2d array
 if (new[0]+new[3]+new[6]==15) or (new[1]+new[4]+new[7]==15) or (new[2]+new[5]+new[8]==15) or (new[0]+new[1]+new[2]==15) or (new[3]+new[4]+new[5]==15) or (new[6]+new[7]+new[8]==15) or (new[0]+new[4]+new[8]==15) or (new[2]+new[4]+new[6]==15):
    print("Player 2 is the winner\n")
    flag=0
    sys.exit()




        






