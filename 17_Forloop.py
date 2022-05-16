friends = ["Mona", "Sona", "Tona"]#array
print("1st program")
for letter in "Giraffe Academy" :
    print(letter)

print("\n2nd program")
for friend in friends:
    print(friends)

print("\n3rd program")
for anyname in friends:
    print(anyname)
#we can name the friend or ayname variable anything

print("\n4th program")
for index in range(10):
    print(index)

print("\n5th program")
print("Range from 3 to 10")
for index in range(3,10):
    print(index)

print("\n6th program")
len(friends)#this will let us know the length of the array
for index in range(len(friends)):
    print(friends[index])

print("\n7th program")
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")