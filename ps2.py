


k=0
new=[]
rows, cols = (3, 3) 
arr = [[0]*cols]*rows 
for row in arr:
    print(row)
new=[j for sub in arr for j in sub]
print("Welcome to the game!\n")
print("Player 1's chance\n")
print("Enter the position and number to be entered:")
p,n=input().split()

new.insert(int(p)-1,int(n))
for i in range(3):
    for j in range(3):
        arr[i][j]=new[k]
        k=k+1

print(arr)



