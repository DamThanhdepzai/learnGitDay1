import helloWorld;
arr =[]
def inputNumber():
    n = int(input("Input quantity number you want: "))
    return n
def appendInArr(n):
    for i in range(n):
        x= int(input("Number "+str(i+1)+":"))
        arr.append(x)
    return arr
def findNumBigest(n):
    return print("Number bigest: "+str(max(n)))
appendInArr(inputNumber())
print(arr)
findNumBigest(arr)