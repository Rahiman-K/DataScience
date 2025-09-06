
lists1 = []
print(type(lists1))
<class 'list'>

List2 = ['Conjuring','The Nun','Annabelle',3, 2.5, True]
print(List2)

['Conjuring', 'The Nun', 'Annabelle', 3, 2.5, True]

print(List2[2])
Annabelle

print(List2[:3])  # prints until 3rd index value exclusing, means gives values of 0, 1, 2 indexed values
['Conjuring', 'The Nun', 'Annabelle']

print(List2[2:4])  # prints elements from 2nd index (including) to 4 index (excluding), means until 3rd index it will print.
['Annabelle', 3]

List2[4] = 12.7
print(List2)
['Conjuring', 'The Nun', 'Annabelle', 3, 12.7, True]

fruits=["apple","banana","cherry","kiwi","gauva"]

fruits[:1]
fruits[1:]  
Out[9]: ['banana', 'cherry', 'kiwi', 'gauva']

fruits.append("Watermelon")
print(fruits)

['apple', 'banana', 'cherry', 'kiwi', 'gauva', 'Watermelon']

fruits.remove("banana")
print(fruits)
['apple', 'cherry', 'kiwi', 'gauva', 'Watermelon']


popped_fruits=fruits.pop()
print(fruits)
print(popped_fruits)
['apple', 'cherry', 'kiwi', 'gauva']
Watermelon

index=fruits.index("cherry")
print(index)

1

fruits.insert(2,"banana")
print(fruits.count("banana"))
1

print(fruits)

['apple', 'cherry', 'banana', 'kiwi', 'gauva']


fruits.sort()

print(fruits)
['apple', 'banana', 'cherry', 'gauva', 'kiwi']

tuple1 = ('1','2','3','4')
print(tuple1, type(tuple1))
('1', '2', '3', '4') <class 'tuple'>

Set1 = {'1','2','3','4','5','7'}

print(Set1, type(Set1))
{'1', '2', '7', '5', '3', '4'} <class 'set'>

Dict1 = {
    "Prabhas":"Bahubali 1, Bahubali 2",
    "Ram Charan":"Magadheera, Rangasthalam, RRR",
    "Pawan Kalyan":"Kushi, Atharintiki Daredi",
    "Allu Arjun":"Pushpa 2",
    "Mahesh Babu":"Pokiri",
    "Jr NTR":" "
    }


print(Dict1)
{'Prabhas': 'Bahubali 1, Bahubali 2', 'Ram Charan': 'Magadheera, Rangasthalam, RRR', 'Pawan Kalyan': 'Kushi, Atharintiki Daredi', 'Allu Arjun': 'Pushpa 2', 'Mahesh Babu': 'Pokiri', 'Jr NTR': ' '}

print(Dict1["Ram Charan"])
Magadheera, Rangasthalam, RRR

print(Dict1.keys(),Dict1.values())
dict_keys(['Prabhas', 'Ram Charan', 'Pawan Kalyan', 'Allu Arjun', 'Mahesh Babu', 'Jr NTR']) dict_values(['Bahubali 1, Bahubali 2', 'Magadheera, Rangasthalam, RRR', 'Kushi, Atharintiki Daredi', 'Pushpa 2', 'Pokiri', ' '])

for key, value in Dict1.items():
    print(f"{key} : {value}")

Prabhas : Bahubali 1, Bahubali 2
Ram Charan : Magadheera, Rangasthalam, RRR
Pawan Kalyan : Kushi, Atharintiki Daredi
Allu Arjun : Pushpa 2
Mahesh Babu : Pokiri
Jr NTR :  
