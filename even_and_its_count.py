start_range=int(input("enter the start range:"))
end_range=int(input("enter the end range:"))
even_count=0
for num in range(start_range,end_range + 1):
    if num % 2 ==0:
        print(num)
        even_count+=1
print("The Number of even no in given range:", even_count)