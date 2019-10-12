
"""
Check if string first half and last half are same or not. you can replace empty string in middle
tata => Yes
hah => Yes after replacing "a"
xyz => No
"""

a = "tayhellozta"

length = len(a)
first_length = int(round(len(a)/2))
print first_length
if not length % 2 == 0:
    a = a[0 : first_length : ] + a[first_length + 1 : :]

first_half = a[0:first_length].lower()
second_half = a[first_length:].lower()
print first_half, second_half
if first_half == second_half:
    print "Yes"

for i in range(len(first_half)):
    print 16, i, first_half[0: len(first_half)-i], second_half[i:len(first_half)]
    if first_half[0: len(first_half)-i] == second_half[i:len(first_half)]:
        print "Yes"
        break
