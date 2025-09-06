
for i in range(5):
    print(i)

0
1
2
3
4

print("\n")


# While Loop
i = 0
while i<5:
    print(i)
    i = i + 1


0
1
2
3
4





print("Break")
for i in range(10):
    if i == 5:
        break  # stops the loop where the break condidtion met.
    print(i)

Break
0
1
2
3
4

print("Continue")

for i in range(15):
    if i%2==0:
        continue    # skips the number and continue to loop until the condition meets
    print(i)


Continue
1
3
5
7
9
11
13

for i in range(5):
    if i==3:
        pass  ## it is like null statement which does nothing.. if your for or if statement does not have any condition.. you can use pass keyword.
    print(i)


0
1
2
3
4



for i in range(3):
    for j in range(2):
        print(f"i:{i} and j:{j}")



i:0 and j:0
i:0 and j:1
i:1 and j:0
i:1 and j:1
i:2 and j:0
i:2 and j:1

n = 10
sum = 0
count = 1

while count<=n:
    sum = sum+count
    count=count+i

print("Sum of first 10 natural numbers", sum)

Sum of first 10 natural numbers 25

for i in range(11):
    sum = sum+i

print(sum)

80

for num in range(1, 101):
    if num>1:
        for i in range(2, num):
            if num%i ==0:
                break
        else:
            print(num)
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
