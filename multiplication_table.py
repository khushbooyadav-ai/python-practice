number = int(input("Enter a number: "))
limit=int(input("Table up to:"))

for i in range(1, limit+1):
    print(f"{number}x{i}={number*i}")