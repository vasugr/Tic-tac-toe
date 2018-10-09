def display_board(li):
        for i in range(6,-1,-3):
                print("%s|%s|%s"%(li[0+i],li[1+i],li[2+i]))
                if i==0: break
                print("-----")

def check(li,n,a):
        x = n%3
        if n == 0:
                if li[n+1]==a and li[n+2]==a:
                        return 1
        if n== 1:
                if li[n-1]==a and li[n+1]==a:
                        return 1
        if n == 2:
                if li[n-2]==a and li[n-1]==a:
                        return 1
        return 0
                

def append(n,a,li):
        if li[n]==' ':
                li[n]=a
                return check(li,n,a)
        else: return -1
                


print("Player1 : x\nPlayer2 : o")
#print(play1)
play1 = 'x'
play2='o'
li = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
display_board(li)
flag=0
while(flag==0):
        flag = append(int(input("Player1 : "))-1,play1,li)
        if flag==0:
                flag = append(int(input("Player2 : "))-1,play2,li)
        display_board(li)


        
