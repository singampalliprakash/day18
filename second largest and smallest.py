def getSecondOrderElements(n: int, a: list[int]) -> list[int]:
    li = sorted(a)
    second_largest = li[-2]
    second_smallest = li[1]
    
    return [second_largest, second_smallest]

n = int(input("Enter the number of elements: "))
a = list(map(int, input("Enter the list here: ").split()))
result = getSecondOrderElements(n, a)
print(f"The second largest number: {result[0]} and the second smallest number: {result[1]}")
