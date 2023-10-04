###FA 4.1 
### Find the (a) first, (b) second, (c) third, and (d ) fourth moments for each of the sets of data 
### (normal, skewed-right, skewed-left, uniform)
zero = 0
sum = 0
numbers = [67, 70, 63, 65, 68, 60, 70, 64, 69, 61, 66, 65, 71, 62, 66, 68, 64, 67, 62, 66, 65, 63, 66, 65, 63, 
           69, 62, 67, 59, 66, 65, 63, 65, 60, 67, 64, 68, 61, 69, 65, 62, 67, 70, 64, 63, 68, 64, 65, 61, 66]

for number in numbers:
    sum = sum + (number-zero)
first = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**2
second = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**3
third = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**4
fourth = sum/len(numbers)

print(f"Normal")
print(f"First moment: {first}")
print(f"Second moment: {second}")
print(f"Third moment: {third}")
print(f"Fourth moment: {fourth}")

###

### 
zero = 0
sum = 0
numbers = [31, 43, 30, 30, 38, 26, 29, 55, 46, 26, 29, 57, 34, 34, 36, 40, 28, 26, 66, 63, 30, 33, 24, 35, 34, 
           40, 24, 29, 24, 27, 35, 33, 75, 38, 34, 85, 29, 40, 41, 35, 26, 34, 19, 23, 28, 26, 31, 25, 22, 28]

for number in numbers:
    sum = sum + (number-zero)
first = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**2
second = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**3
third = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**4
fourth = sum/len(numbers)

print(f"Skewed-Right")
print(f"First moment: {first}")
print(f"Second moment: {second}")
print(f"Third moment: {third}")
print(f"Fourth moment: {fourth}")

###

###
zero = 0
sum = 0
numbers = [102, 55, 70, 95, 73, 79, 60, 73, 89, 85, 72, 92, 76, 93, 76, 97, 10, 70, 85, 25, 83, 58, 10, 92, 82, 
           87, 104, 75, 80, 66, 93, 90, 84, 73, 98, 79, 35, 71, 90, 71, 63, 58, 82, 72, 93, 44, 65, 77, 81, 77]

for number in numbers:
    sum = sum + (number-zero)
first = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**2
second = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**3
third = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**4
fourth = sum/len(numbers)

print(f"Skewed-Left")
print(f"First moment: {first}")
print(f"Second moment: {second}")
print(f"Third moment: {third}")
print(f"Fourth moment: {fourth}")

###

###

zero = 0
sum = 0
numbers = [12.1, 12.1, 12.4, 12.1, 12.1, 12.2, 12.2, 12.2, 11.9, 12.2, 12.3, 12.3, 11.7, 12.3, 12.3, 12.4, 12.4, 12.1, 12.4, 12.4, 12.5, 11.8, 12.5, 12.5, 12.5, 
           11.6, 11.6, 12, 11.6, 11.6, 11.7, 12.3, 11.7, 11.7, 11.7, 11.8, 12.5, 11.8, 11.8, 11.8, 11.9, 11.9, 11.9, 12.2, 11.9, 12, 11.9, 12, 12, 12]

for number in numbers:
    sum = sum + (number-zero)
first = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**2
second = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**3
third = sum/len(numbers)
sum = 0

for number in numbers:
    sum = sum + (number-zero)**4
fourth = sum/len(numbers)

print(f"Uniform")
print(f"First moment: {first}")
print(f"Second moment: {second}")
print(f"Third moment: {third}")
print(f"Fourth moment: {fourth}")

###

### Find the (a) first, (b) second, (c) third, and (d ) fourth moments about the mean for each of the sets of data 
### (normal, skewed-right, skewed-left, uniform).

import numpy as np
sum = 0
numbers = [67, 70, 63, 65, 68, 60, 70, 64, 69, 61, 66, 6, 71, 62, 66, 68, 64, 67, 62, 66, 65, 63, 66, 65, 63, 
           69, 62, 67, 59, 66, 65, 63, 65, 60, 67, 64, 68, 61, 69, 65, 62, 67, 70, 64, 63, 68, 64, 65, 61, 66]
zero = np.mean(numbers)

for number in numbers:
    sum = sum + (number-zero)
first = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**2
second = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**3
third = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**4
fourth = sum/len(numbers)

print(f"Normal")
print(f"First moment: {first}")
print(f"Second moment: {second}")
print(f"Third moment: {third}")
print(f"Fourth moment: {fourth}")

###

import numpy as np
sum = 0
numbers = [31, 43, 30, 30, 38, 26, 29, 55, 46, 26, 29, 57, 34, 34, 36, 40, 28, 26, 66, 63, 30, 33, 24, 35, 34, 
           40, 24, 29, 24, 27, 35, 33, 75, 38, 34, 85, 29, 40, 41, 35, 26, 34, 19, 23, 28, 26, 31, 25, 22, 28]
zero = np.mean(numbers)

for number in numbers:
    sum = sum + (number-zero)
first = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**2
second = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**3
third = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**4
fourth = sum/len(numbers)

print(f"Skewed-Right")
print(f"First moment: {first}")
print(f"Second moment: {second}")
print(f"Third moment: {third}")
print(f"Fourth moment: {fourth}")

###

import numpy as np
sum = 0
numbers = [102, 55, 70, 95, 73, 79, 60, 73, 89, 85, 72, 92, 76, 93, 76, 97, 10, 70, 85, 25, 83, 58, 10, 92, 82, 
           87, 104, 75, 80, 66, 93, 90, 84, 73, 98, 79, 35, 71, 90, 71, 63, 58, 82, 72, 93, 44, 65, 77, 81, 77]
zero = np.mean(numbers)

for number in numbers:
    sum = sum + (number-zero)
first = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**2
second = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**3
third = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**4
fourth = sum/len(numbers)

print(f"Skewed-Left")
print(f"First moment: {first}")
print(f"Second moment: {second}")
print(f"Third moment: {third}")
print(f"Fourth moment: {fourth}")

###

import numpy as np
sum = 0
numbers = [12.1, 12.1, 12.4, 12.1, 12.1, 12.2, 12.2, 12.2, 11.9, 12.2, 12.3, 12.3, 11.7, 12.3, 12.3, 12.4, 12.4, 12.1, 12.4, 12.4, 12.5, 11.8, 12.5, 12.5, 12.5, 
           11.6, 11.6, 12, 11.6, 11.6, 11.7, 12.3, 11.7, 11.7, 11.7, 11.8, 12.5, 11.8, 11.8, 11.8, 11.9, 11.9, 11.9, 12.2, 11.9, 12, 11.9, 12, 12, 12]
zero = np.mean(numbers)

for number in numbers:
    sum = sum + (number-zero)
first = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**2
second = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**3
third = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-zero)**4
fourth = sum/len(numbers)

print(f"Uniform")
print(f"First moment: {first}")
print(f"Second moment: {second}")
print(f"Third moment: {third}")
print(f"Fourth moment: {fourth}")

###
#### Find the (a) first, (b) second, (c) third, and (d ) fourth moments about the number 75 for the set of female height measurements. 
### (normal distribution only)

start = 75
sum = 0
numbers = [67, 70, 63, 65, 68, 60, 70, 64, 69, 61, 66, 6, 71, 62, 66, 68, 64, 67, 62, 66, 65, 63, 66, 65, 63, 
           69, 62, 67, 59, 66, 65, 63, 65, 60, 67, 64, 68, 61, 69, 65, 62, 67, 70, 64, 63, 68, 64, 65, 61, 66]

for number in numbers:
    sum = sum + (number-start)
first = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-start)**2
second = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-start)**3
third = sum/len(numbers)
sum

for number in numbers:
    sum = sum + (number-start)**4
fourth = sum/len(numbers)
print(f"Find the (a) first, (b) second, (c) third, and (d ) fourth moments about the number 75 for the set of female height measurements.")
print(f"First moment: {first}")
print(f"Second moment: {second}")
print(f"Third moment: {third}")
print(f"Fourth moment: {fourth}")

###
### Using the results of items 2 and 3 for the set of female height measurements, verify the relations between the moments
m2nd = second - ((first)**2)
m3rd = third - (3*first*second) + (2*(first**3))
m4th = fourth - (4*first*third) + (6*(first**2)*second) - (3*(first**4))
print(m2nd)
print(m3rd)
print(m4th)
print("They are all the same from the 5th cell")