#Anyijukire Janet
x = [100,110,120,130,140,150]
y=[]
for i in x:
    a=i*5
    y.append(a)
print(y) 
def divisible_by_three(n): 
    c=range(n+1)
    d=[]  
    for u in c:
        if u%3==0:
            d.append(u) 
    print(d)
divisible_by_three(39)
def list_flattener():
   x = [[1,2],[3,4],[5,6]]
   b = [value for sublist in x for value in sublist]
   print(b)
list_flattener()   

def smallest(args):
    print(min(args))
smallest([5,6,7,2,3,1,4])
smallest([90,86,64,34,3,23,55,66,11]) 

def remove_duplicates(x):
    y=set(x)
    print(y)
remove_duplicates(['a','b','a','e','d','b','c','e','f','g','h']
)    

def divisible_by_seven():
    v=range(100,200)
    b=[]
    for i in v:
        if i%7==0:
            b.append(i)
    print(b)  
divisible_by_seven()  
def greet_students(students): 
  for i in students:
    print( f"Hi {i['name']}, you are {i['age']} years old")
greet_students([{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]  
)    