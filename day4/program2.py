L = int(input("Enter the no of tuples you want to add in the list: "))
T = int(input("Enter the no of elements you want to add in each tuple: "))
List = []
for i in range(L):
    print("Enter the elements in Tuple", i + 1)
    Tup = []
    for j in range(T):
        Tuple.append(int(input("Enter the element " + str(j + 1) + ": ")))
    List.append(tuple(Tup))
N = int(input("Enter the Nth index about which you want to sort the list: "))
List.sort(key = lambda x : x[N])
print("After sorting tuple List by Nth index sort:",List)
