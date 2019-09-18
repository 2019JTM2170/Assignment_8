def update(new):
      print(new[0:3])
      print(new[3:6])
      print(new[6:9])

new1=[]
k=0
new=[]
rows, cols = (3, 3) 
arr = [[0]*cols]*rows 
for row in arr:
    print(row)
new=[j for sub in arr for j in sub]
print("Welcome to the game!\n")
while(1):
 print("\nPlayer 1's chance\n")
 print("Enter the position and number to be entered:")
 p,n=input().split()
 new[int(p)-1]=int(n)
 print(new)
 update(new)
 print("\nPlayer 2's chance\n")
 print("Enter the position and number to be entered:")
 p,n=input().split()
 new[int(p)-1]=int(n)
 print(new)
 update(new)


        






