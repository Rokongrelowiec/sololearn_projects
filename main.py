'''
To check function, please remove '#' symbol before name of function
'''

def exponent():
    num = int(input("Number: "))
    exp = int(input("Exponent: "))
    res = 1
    if exp < 0:
        num = 1/num
        exp = abs(exp)
        for i in range(exp):
            res *= num
    else:
        for i in range(exp):
            res *= num
    print(res)
#exponent

def books():
    file = open("books.txt", "r")
    text = file.readlines()
    for i in text:
        i = i.rstrip()
        word = i[0]+str(len(i))
        print(word)
    file.close()

books()

def longest():
    txt = input("Word: ")
    txt = txt.split()
    max = txt[0]
    for i in txt:
        if len(i) > len(max):
            max = i
    print(max)

#longest()

def blocks_tower():
    blocks = int(input("Enter number of blocks: "))

    if blocks == 0:
        return "Height is 0 levels"
    elif blocks < 0:
        return "Number of blocks must be positive number"
    else:
        levels = 0
        i = 1
        while True:
            if blocks - i >= 0:
                blocks -= i
                levels += 1
                i += 1
            else:
                break
        return levels

# print(blocks_tower())

def juice():
    class Juice:
        def __init__(self, name, capacity):
            self.name = name
            self.capacity = capacity
        def __str__(self):
            return (self.name + " ("+str(self.capacity)+"L)")
        def __add__(self, sec):
            return Juice(self.name+"&"+sec.name, self.capacity+sec.capacity)
    a = Juice("Orange", 1.5)
    b = Juice("Apple", 2.0)
    c = a+b
    print(c)

#juice()

def phone():
    '''
    Valid number must contain 8 digits:
    first digit must be: 1 or 8 or 9
    and the rest (7 last digits) must be between 0 and 9
    '''

    phone = input("Phone num: ")
    import re
    if re.match("^[1|8|9]([0-9]{7})$", phone):
        print("Valid")
    else:
        print("Invalid")

#phone()

def geometric_sequence(n, a1=1, q=2):
    return a1*pow(q, n-1)
#print(geometric_sequence(6))

def specialCode():
    word = input("Word: ")
    count = int(input("Count: "))
    res = ""

    for i in word:
        if i == " ":
            res += i
        else:
            i = ord(i)
            i = chr(i+count)
            res += i
    print(res)

#specialCode()

def revenueGrowth():
    data = {"100-90": 25, "42-01": 48, "55-09": 12, "128-64": 71, "002-22": 18, "321-54": 19, "097-32": 33, "065-135": 64, "99-043": 80, "111-99": 11, "123-019": 5, "109-890": 72, "132-123": 27, "32-908": 27, "008-09": 25, "055-967": 35, "897-99": 44, "890-98": 56, "344-32": 65, "43-955": 59, "001-233": 9, "089-111": 15, "090-090": 17, "56-777": 23, "44-909": 27, "13-111": 21, "87-432": 15, "87-433": 14, "87-434": 23, "87-435": 11, "87-436": 12, "87-437": 16, "94-121": 15, "94-122": 35, "80-089": 10, "87-456": 8, "87-430": 40}
    age = int(input("Age: "))
    org = 0
    for i in data.values():
        if i < 18:
            org += 5
        else:
            org += 20
    dis = 0
    for i in data.values():
        if i < age:
            dis += 5
        else:
            dis += 20
    res = ((dis-org)/org)*100
    print(int(res))

#revenueGrowth()

def avg():
    #  in polish schools ratings are between 1 and 6
    amount_ratings = int(input("Enter count of ratings: "))
    i = 0
    lst = []
    res = 0
    r = 0
    while i < amount_ratings:
        a = int(input("Enter rating: "))
        if a > 0 and a < 7:
            lst.append(a)
            i += 1
    print(lst)
    while r < len(lst):
        res += lst[r]
        r += 1
    print(res/len(lst))

#avg()

class Enemy:
  def __init__(self, name, lives):
    self.name = name
    self.lives = lives

  def hit(self):
    self.lives -= 1
    if self.lives <= 0:
       print(self.name + ' killed')
    else:
        print(self.name + ' has '+ str(self.lives) + ' lives')

class Monster(Enemy):
  def __init__(self):
    super().__init__('Monster', 3)

class Alien(Enemy):
  def __init__(self):
    super().__init__('Alien', 5)

m = Monster()
a = Alien()
'''
while True:
    x = input("Your weapon: ")
    x = x.lower()
    if x == 'exit':
        break
    else:
        if x == 'gun':
            m.hit()
        elif x == 'laser':
            a.hit()
'''