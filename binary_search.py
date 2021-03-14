'''
Have you ever heard the saying "Find a needle in a haystack"? This program is designed to do
just that - using a binary search algorithm. You can create a list of random numbers,
and search for an index of a specific number that you choose
'''

def search(list, value):
    low = 0
    high = len(list)-1
    while low <= high:
        mid = low + ( high - low ) // 2
        mid_value = list[mid]
        if mid_value == value:
            return "Index for your input is "+str(mid)
        elif mid_value > value:
            high = mid - 1
        else:
            low = mid + 1

    return "Your input is not on the list !"

print("Welcome 👋")
leng = int(input("Enter length of list : "))
print(" ")
list = []
for n in range(leng):
    try:
        element = int(input("Enter the element : "))
    except:
        print("Please check your input !")
        exit()
    list.append(element)

list.sort()

try:
  value = int(input("\nPlease enter your number : "))
except:
  print("\nPlease check your input !")
  exit()

print(search(list, value))
