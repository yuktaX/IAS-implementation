m=list(range(1000)) #memory list/array
pc=0  #global variables 
ac=0
ir=0
ibr=0
mar=0
mbr=0
mq=0

def address(n): #returns 12 bit address
    adrs=str(bin(n)).replace("0b","00")
    ans='0'*(12-len(adrs))+adrs
    return (ans)

def fetch_execute(p): #function that fetches, decodes and executes
    global pc
    global ac
    global ir
    global ibr
    global mbr
    global mar
    global mq
    mar=pc            #Fetch cycle
    mbr=p             
    ir=mbr[0:8]
    ibr=mbr[20:40]
    mar=mbr[8:20]

    #store
    if(p[0:8]=='00100001'):    
        mbr=ac
        m[int(mar,2)]=bin(mbr)    #decode and execute

    #store-rhs
    if(p[20:28]=='00100001'):    
        mbr=ac
        m[int(mar,2)]=bin(mbr)    #decode and execute
    
    #Load MQ M(x)
    if(p[0:8]=='00001001'):
        mbr=int(m[int(mar, 2)],2)
        mq=mbr
    #loadMQ
    if(p[20:28]=='00001010'):#decode and execute
        ac=mq

    #load
    if(p[0:8]=='00000001'):
        mbr=int(m[int(mar, 2)],2) #decode and execute
        ac=mbr

    #add-RHS
    if(p[20:28]=='00000101'):
        ir=ibr[0:8]
        mar=ibr[8:20]                    #decode and execute
        mbr=int(m[int(mar,2)],2)
        ac=ac+mbr

    #subtract
    if(p[20:28]=='00000110'):
        ir=ibr[0:8]
        mar=ibr[8:20]               #decode and execute
        mbr=int(m[int(mar,2)],2)
        ac=ac-mbr

    #mul-rhs
    if(p[20:28]=='00001011'):
        ir=ibr[0:8]
        mar=ibr[8:20]
        mbr=int(m[int(mar, 2)],2)   #decode and execute
        tmp=format(mq*mbr,'080b')
        ac=int(tmp[0:40],2)
        mq=int(tmp[40:80],2)

    pc=pc+1 #incrementing pc at the end of every cycle
        
    #halt
    if(ir=='0000000'):
        pass

    
#main
print('Enter the operation you want to perform\n1-->Add 2 numbers\n2-->Subtract 2 numbers\n3-->Perimeter of isosceles triangle\n4-->Subtraction of 2x2 matrix\n5-->Multiplication of 2 numbers\n6-->Total surface area of cuboid')
choice=int(input('choice: '))
if(choice==1):
    x=int(input("number 1: "))
    y=int(input("number 2: "))
    m[100]=format(x,'040b') #converting int into 40-bit data
    m[101]=format(y,'040b')
    m[0]=('00000001'+ address(100)+'00000101' + address(101)) #LOAD M(100), ADD M(101)
    m[1]=('00100001'+ address(102)+'00000000000000000000') #STOR M(102)
    fetch_execute(m[0])
    fetch_execute(m[1])
    print(int(m[102],2))

if(choice==2):
    x=int(input("number 1: "))
    y=int(input("number 2: "))
    m[200]=format(x,'040b') #converting int into 40-bit data
    m[201]=format(y,'040b')
    m[0]=('00000001'+ address(200)+'00000110'+address(201))#LOAD M(200), SUB M(201)
    m[1]=('00100001'+ address(202)+'00000000000000000000')#STOR M(202)
    fetch_execute(m[0])
    fetch_execute(m[1])
    print(int(m[202],2))

if(choice==3):
    x=int(input("Equal side length: "))
    y=int(input("Other side: "))
    m[300]=format(x,'040b') #converting int into 40-bit data
    m[301]=format(x,'040b')
    m[302]=format(y,'040b')
    m[0]=('00000001'+ address(300)+'00000101'+address(301))#LOAD M(300), ADD M(300)
    m[1]=('00100001'+address(303)+'00000000000000000000')#STOR M(302)
    m[2]=('00000001'+ address(303)+'00000101'+address(302))#LOAD M(302), ADD M(301)
    m[3]=('00100001'+address(304)+'00000000000000000000')#STOR M(303)
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    print('Perimeter = ',int(m[304],2))

if(choice==4):
    print("Enter elements in a single line:")
    print("Matrix A[]\n")
    p,q,r,s=(input().split())
    print("Matrix B[]\n")
    a,b,c,d=(input().split())

    m[400]=format(int(p),'040b') #converting int data into 40 bit binary address and storing in memory
    m[401]=format(int(q),'040b')
    m[402]=format(int(r),'040b')
    m[403]=format(int(s),'040b')
    m[500]=format(int(a),'040b')
    m[501]=format(int(b),'040b')
    m[502]=format(int(c),'040b')
    m[503]=format(int(d),'040b')
    m[0]=('00000001'+ address(400)+'00000110'+address(500))#LOAD M(400), SUB M(500)
    m[1]=('00100001'+ address(600)+'00000000000000000000')#STOR M(600)
    m[2]=('00000001'+ address(401)+'00000110'+address(501))#LOAD M(401), SUB M(501)
    m[3]=('00100001'+ address(601)+'00000000000000000000')#STOR M(601)
    m[4]=('00000001'+ address(402)+'00000110'+address(502))#LOAD M(402), SUB M(502)
    m[5]=('00100001'+ address(602)+'00000000000000000000')#STOR M(602)
    m[6]=('00000001'+ address(403)+'00000110'+address(503))#LOAD M(403), SUB M(503)
    m[7]=('00100001'+ address(603)+'00000000000000000000')#STOR M(603)
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    print('[',int(m[600],2),',',int(m[601],2),']')
    print('[',int(m[602],2),',',int(m[603],2),']')

if(choice==5):
    x=int(input('Number 1:'))
    y=int(input('Number 2:'))
    m[700]=format(x,'040b')
    m[701]=format(y,'040b')
    m[0]=('00001001'+address(700)+'00001011'+address(701)) #LOAD MX MQ, MUL MX
    m[1]=('00100001'+ address(710)+'00001010'+'000000000000') #address(702))#STOR MX,LOAD MQ
    m[2]=('00100001'+address(711))#STOR MX
    fetch_execute(m[0])
    fetch_execute(m[1])
    fetch_execute(m[2])
    print(int(m[710],2),end='')
    print(int(m[711],2))

if(choice==6):
    x=int(input('side a: '))
    y=int(input('side b: '))
    z=int(input('side c: '))
    m[800]=format(x,'040b')
    m[801]=format(y,'040b')
    m[802]=format(z,'040b')
    m[0]=('00001001'+address(800)+'00001011'+address(801)) #LOAD MX MQ, MUL MX
    m[1]=('00100001'+ address(810)+'00001010'+'000000000000') #address(702))#STOR MX,LOAD MQ
    m[2]=('00100001'+address(811)+'00000000000000000000')#STOR MX
    m[3]=('00001001'+address(801)+'00001011'+address(802)) #LOAD MX MQ, MUL MX
    m[4]=('00100001'+ address(820)+'00001010'+'000000000000') #address(702))#STOR MX,LOAD MQ
    m[5]=('00100001'+address(821)+'00000000000000000000')#STOR MX
    m[6]=('00001001'+address(802)+'00001011'+address(800)) #LOAD MX MQ, MUL MX
    m[7]=('00100001'+ address(830)+'00001010'+'000000000000')#STOR MX,LOAD MQ
    m[8]=('00100001'+address(831)+'00000000000000000000')#STOR MX
    m[9]=('00000001'+ address(811)+'00000101'+address(821))# LOAD MX, ADD MX
    m[10]=('00100001'+address(900)+'000000000000') #STOR MX
    m[11]=('00000001'+ address(900)+'00000101'+ address(831))#LOAD MX, ADD MX
    m[12]=('00100001'+address(901)+'000000000000')#STOR MX
    m[13]=('00000001'+ address(901)+'00000101'+address(901))# LOAD MX, ADD MX
    m[14]=('00100001'+address(902)+'000000000000')#STOR MX
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
    fetch_execute(m[pc])
   
    print('TSA = ', int(m[902],2),'sq units')

else:
    exit
    



 
