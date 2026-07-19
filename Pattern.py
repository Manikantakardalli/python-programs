n = int(input("Enter number of rows:"))

print("1.Left Triangle")
print("2.Pyramid")
print("3.Reverse Pyramid")
print("4.Left Reverse Triangle")
choice = int(input("Enetr Your choice:"))


     
if choice==1:
       for i in range(1, n + 1):
              for j in range(i):
                     print("*",end = " ")
              print()
     
         

elif choice==2:
       for i in range(n):
              for j in range(n - i - 1):
                     print(" ", end ="")
              for k in range(2 * i + 1):
                     print("*", end = "")
              print()       
       
        
     
elif choice==3:   
       for i in range(n):
              for j in range(i):
                     print(" ", end ="")
              for k in range(2 * (n - i) - 1):
                     print("*", end = "")
              print()       
                     
              
       
    
          
elif choice==4: 
       for i in range(n,0,-1):
              for j in range(i):
                     print("*",end=" ")
              print()      
    
else:
       print("Invaild Choice")










 
