
import pandas as pd

data=pd.read_csv('datanew.csv')
data

data['Time'].value_counts()
A=10/49
B=12/49
C=9/49
D=9/49
E=9/49

print(A)
print(B)
print(C)
print(D)
print(E)

pd.crosstab(data['Area Size'], data['Time'])

large_A = 3/10
medium_A = 3/10
small_A = 4/10
verylarge_A = 0
verysmall_A = 0


large_B = 3/12
medium_B = 3/12
small_B = 5/12
verylarge_B = 0
verysmall_B = 1/12

large_C = 2/9
medium_C = 5/9
small_C = 1/9
verylarge_C = 1/9
verysmall_C = 0

large_D = 0
medium_D = 1/9
small_D = 1/9
verylarge_D = 4/9
verysmall_D = 3/9


large_E = 2/9
medium_E = 0
small_E = 0
verylarge_E = 2/9
verysmall_E = 5/9

pd.crosstab(data['Project Scope'],data['Time'])

agroforestry_A = 7/10
reforestation_A = 3/10
urbanplanting_A = 0

agroforestry_B = 3/12
reforestation_B = 4/12
urbanplanting_B = 5/12

agroforestry_C = 3/9
reforestation_C = 2/9
urbanplanting_C = 4/9

agroforestry_D = 6/9
reforestation_D = 1/9
urbanplanting_D = 2/9

agroforestry_E = 0/9
reforestation_E = 5/9
urbanplanting_E = 4/9


pd.crosstab(data['Soil Condition'],data['Time'])

fair_A = 1/10
good_A = 5/10
poor_A = 4/10

fair_B = 3/12
good_B = 6/12
poor_B = 3/12

fair_C = 5/9
good_C = 1/9
poor_C = 3/9

fair_D = 2/9
good_D = 7/9
poor_D = 0

fair_E = 8/9
good_E = 1/9
poor_E = 0/9

pd.crosstab(data['weather condition'],data['Time'])

cloudy_A = 6/10
rainy_A = 1/10
sunny_A = 3/10

cloudy_B = 3/12
rainy_B = 4/12
sunny_B = 5/12

cloudy_C = 1/9
rainy_C = 5/9
sunny_C = 3/9

cloudy_D = 5/9
rainy_D = 2/9
sunny_D = 2/9

cloudy_E = 1/9
rainy_E = 3/9
sunny_E = 5/9

pd.crosstab(data['participant'],data['Time'])

_large_A = 3/10
_medium_A= 2/10
_small_A = 5/10
very_large_A= 0
very_small_A = 0

_large_B = 2/12
_medium_B= 3/12
_small_B = 5/12
very_large_B= 0
very_small_B = 2/12

_large_C = 3/9
_medium_C= 5/9
_small_C = 1/9
very_large_C= 0
very_small_C = 0

_large_D = 4/9
_medium_D= 1/9
_small_D = 1/9
very_large_D= 0
very_small_D = 3/9

_large_E = 3/9
_medium_E= 0
_small_E = 0
very_large_E= 1/9
very_small_E = 5/9


    # Initialize the lists
data_list_A = []
data_list_B = []
data_list_C = []
data_list_D = []
data_list_E = []


user_input =['small', 'urban planting', 'fair', 'rainy', 'very_small']
for input in user_input:


    if 'very small' == input:
        data_list_A.append(verysmall_A)
        data_list_B.append(verysmall_B)
        data_list_C.append(verysmall_C)
        data_list_D.append(verysmall_D)
        data_list_E.append(verysmall_E)
        print("m:",data_list_B)
    

    if 'small' == input:
        data_list_A.append(small_A)
        data_list_B.append(small_B)
        data_list_C.append(small_C)
        data_list_D.append(small_D)
        data_list_E.append(small_E)
       

    if 'medium' == input:
        data_list_A.append(medium_A)
        data_list_B.append(medium_B)
        data_list_C.append(medium_C)
        data_list_D.append(medium_D)
        data_list_E.append(medium_E)

    if 'large' == input:
        data_list_A.append(large_A)
        data_list_B.append(large_B)
        data_list_C.append(large_C)
        data_list_D.append(large_D)
        data_list_E.append(large_E)

    if 'very large' == input:
        data_list_A.append(verylarge_A)
        data_list_B.append(verylarge_B)
        data_list_C.append(verylarge_C)
        data_list_D.append(verylarge_D)
        data_list_E.append(verylarge_E)

    if 'reforestion' == input:
        data_list_A.append(reforestation_A)
        data_list_B.append(reforestation_B)
        data_list_C.append(reforestation_C)
        data_list_D.append(reforestation_D)
        data_list_E.append(reforestation_E)

    if 'urban planting' == input:
        data_list_A.append(urbanplanting_A)
        data_list_B.append(urbanplanting_B)
        data_list_C.append(urbanplanting_C)
        data_list_D.append(urbanplanting_D)
        data_list_E.append(urbanplanting_E)

    if 'agroforestry' == input:
        data_list_A.append(agroforestry_A)
        data_list_B.append(agroforestry_B)
        data_list_C.append(agroforestry_C)
        data_list_D.append(agroforestry_D)
        data_list_E.append(agroforestry_E)

    if 'good' == input:
        data_list_A.append(good_A)
        data_list_B.append(good_B)
        data_list_C.append(good_C)
        data_list_D.append(good_D)
        data_list_E.append(good_E)

    if 'fair' == input:
        data_list_A.append(fair_A)
        data_list_B.append(fair_B)
        data_list_C.append(fair_C)
        data_list_D.append(fair_D)
        data_list_E.append(fair_E)

    if 'poor' == input:
        data_list_A.append(poor_A)
        data_list_B.append(poor_B)
        data_list_C.append(poor_C)
        data_list_D.append(poor_D)
        data_list_E.append(poor_E)

    if 'sunny' == input:
        data_list_A.append(sunny_A)
        data_list_B.append(sunny_B)
        data_list_C.append(sunny_C)
        data_list_D.append(sunny_D)
        data_list_E.append(sunny_E)

    if 'rainy' == input:
        data_list_A.append(rainy_A)
        data_list_B.append(rainy_B)
        data_list_C.append(rainy_C)
        data_list_D.append(rainy_D)
        data_list_E.append(rainy_E)

    if 'cloudy' == input:
        data_list_A.append(cloudy_A)
        data_list_B.append(cloudy_B)
        data_list_C.append(cloudy_C)
        data_list_D.append(cloudy_D)
        data_list_E.append(cloudy_E)

    if 'very_small' == input:
        data_list_A.append(very_small_A)
        data_list_B.append(very_small_B)
        data_list_C.append(very_small_C)
        data_list_D.append(very_small_D)
        data_list_E.append(very_small_E)

    if '_small' == input:
        data_list_A.append(_small_A)
        data_list_B.append(_small_B)
        data_list_C.append(_small_C)
        data_list_D.append(_small_D)
        data_list_E.append(_small_E)

    if '_medium' == input:
        data_list_A.append(_medium_A)
        data_list_B.append(_medium_B)
        data_list_C.append(_medium_C)
        data_list_D.append(_medium_D)
        data_list_E.append(_medium_E)

    if '_large' == input:
        data_list_A.append(_large_A)
        data_list_B.append(_large_B)
        data_list_C.append(_large_C)
        data_list_D.append(_large_D)
        data_list_E.append(_large_E)

    if 'very_large' == input:
        data_list_A.append(very_large_A)
        data_list_B.append(very_large_B)
        data_list_C.append(very_large_C)
        data_list_D.append(very_large_D)
        data_list_E.append(very_large_E)

print("data A",data_list_A[0],data_list_A[1],data_list_A[2],data_list_A[3],data_list_A[4])
print("data B",data_list_B[0],data_list_B[1],data_list_B[2],data_list_B[3],data_list_B[4])


data_lists = [data_list_A, data_list_B, data_list_C, data_list_D, data_list_E]
final_values = []

for data_list in data_lists:
    result = 1
    for value in data_list:
        result *= value
    final_values.append(result)

Final_A, Final_B, Final_C, Final_D, Final_E = final_values[0]*A, final_values[1]*B, final_values[2]*C, final_values[3]*D, final_values[4]*E

print("Final A:",Final_A)
print("Final B:",Final_B)
print("Final C:",Final_C)
print("Final D:",Final_D)
print("Final E:",Final_E)



