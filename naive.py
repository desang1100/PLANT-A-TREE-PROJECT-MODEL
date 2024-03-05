

# Example usage with the provided dataset
dataset = [
    [1, "sunny", "hot", "high", "weak", "no"],
    [2, "sunny", "hot", "high", "strong", "no"],
    [3, "overcast", "hot", "high", "weak", "yes"],
    [4, "rain", "mild", "high", "weak", "yes"],
    [5, "rain", "cool", "normal", "weak", "yes"],
    [6, "rain", "cool", "normal", "strong", "no"],
    [7, "overcast", "cool", "normal", "strong", "yes"],
    [8, "sunny", "mild", "high", "weak", "no"],
    [9, "sunny", "cool", "normal", "weak", "yes"],
    [10, "rain", "mild", "normal", "weak", "yes"],
    [11, "sunny", "mild", "normal", "strong", "yes"],
    [12, "overcast", "mild", "high", "strong", "yes"],
    [13, "overcast", "hot", "normal", "weak", "yes"],
    [14, "rain", "mild", "high", "strong", "no"],
]


#---------------------------------------------- T O T A L  Y E S -----------------------------------------------------> 


def yes_calculate_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_data = len(dataset)
    probability = total_yes / total_data
    print("Total Number  of 'Yes':", total_yes)
    print("Total Number  of 'Yes':", total_data)
    return probability


yes_probability = yes_calculate_probability(dataset)

print("Probability of 'Yes':", yes_probability)


#---------------------------------------------- T O T A L   N O ----------------------------------------------------->   


def no_calculate_probability(dataset):
    total_no = sum(1 for data in dataset if data[5] == "no")
    total_data = len(dataset)
    probability = total_no / total_data
    print("Total Number  of 'Yes':", total_no)
    print("Total Number  of 'Yes':", total_data)
    return probability


no_probability = no_calculate_probability(dataset)
print("Probability of 'No':", no_probability)

#----------------------------------------------   O U T L O O K  
#                                                                    S U N N Y ----------------------------------------------------->
def calculate_sunny_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    sunny_yes_count = sum(1 for data in dataset if data[1] == "sunny" and data[5] == "yes")
    sunny_no_count = sum(1 for data in dataset if data[1] == "sunny" and data[5] == "no")

    sunny_yes_probability = sunny_yes_count / total_yes
    sunny_no_probability = sunny_no_count / total_no

    return sunny_yes_probability, sunny_no_probability


sunny_yes_prob, sunny_no_prob = calculate_sunny_probability(dataset)
print("Probability of 'Sunny' given 'Yes':", sunny_yes_prob)
print("Probability of 'Sunny' given 'No':", sunny_no_prob)

#----------------------------------------------   O U T L O O K  
#                                                                       O V E R C A S T ----------------------------------------------------->

def calculate_overcast_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    yes_count = sum(1 for data in dataset if data[1] == "overcast" and data[5] == "yes")
    no_count = sum(1 for data in dataset if data[1] == "overcast" and data[5] == "no")

    overcast_yes_probability = yes_count / total_yes
    overcast_no_probability = no_count / total_no

    return overcast_yes_probability, overcast_no_probability

overcast_yes_prob, overcast_no_prob = calculate_overcast_probability(dataset)
print("Probability of 'Overcast' given 'Yes':", overcast_yes_prob)
print("Probability of 'Overcast' given 'No':", overcast_no_prob)


#----------------------------------------------   O U T L O O K  
#                                                                       R A I N ----------------------------------------------------->

def calculate_rain_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    yes_count = sum(1 for data in dataset if data[1] == "rain" and data[5] == "yes")
    no_count = sum(1 for data in dataset if data[1] == "rain" and data[5] == "no")

    rain_yes_probability = yes_count / total_yes
    rain_no_probability = no_count / total_no

    return rain_yes_probability, rain_no_probability


rain_yes_prob, rain_no_prob = calculate_rain_probability(dataset)
print("Probability of 'Rain' given 'Yes':", rain_yes_prob)
print("Probability of 'Rain' given 'No':", rain_no_prob)


#----------------------------------------------   T E M P E R  A T U R E 
#                                                                               H O T ----------------------------------------------------->

def calculate_hot_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    yes_count = sum(1 for data in dataset if data[2] == "hot" and data[5] == "yes")
    no_count = sum(1 for data in dataset if data[2] == "hot" and data[5] == "no")

    hot_yes_probability = yes_count / total_yes
    hot_no_probability = no_count / total_no

    return hot_yes_probability, hot_no_probability


hot_yes_prob, hot_no_prob = calculate_hot_probability(dataset)
print("Probability of 'Hot' given 'Yes':", hot_yes_prob)
print("Probability of 'Hot' given 'No':", hot_no_prob)


#----------------------------------------------   T E M P E R  A T U R E 
#                                                                               M I L D ----------------------------------------------------->

def calculate_mild_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    yes_count = sum(1 for data in dataset if data[2] == "mild" and data[5] == "yes")
    no_count = sum(1 for data in dataset if data[2] == "mild" and data[5] == "no")

    mild_yes_probability = yes_count / total_yes
    mild_no_probability = no_count / total_no

    return mild_yes_probability, mild_no_probability


mild_yes_prob, mild_no_prob = calculate_mild_probability(dataset)
print("Probability of 'Mild' given 'Yes':", mild_yes_prob)
print("Probability of 'Mild' given 'No':", mild_no_prob)


#----------------------------------------------   T E M P E R  A T U R E 
#                                                                               C O O L ----------------------------------------------------->

def calculate_cool_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    yes_count = sum(1 for data in dataset if data[2] == "cool" and data[5] == "yes")
    no_count = sum(1 for data in dataset if data[2] == "cool" and data[5] == "no")

    cool_yes_probability = yes_count / total_yes
    cool_no_probability = no_count / total_no

    return cool_yes_probability, cool_no_probability


cool_yes_prob, cool_no_prob = calculate_cool_probability(dataset)
print("Probability of 'Cool' given 'Yes':", cool_yes_prob)
print("Probability of 'Cool' given 'No':", cool_no_prob)


#----------------------------------------------   H U M I D I T Y 
#                                                                               H I G H  ----------------------------------------------------->

def calculate_high_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    yes_count = sum(1 for data in dataset if data[3] == "high" and data[5] == "yes")
    no_count = sum(1 for data in dataset if data[3] == "high" and data[5] == "no")

    high_yes_probability = yes_count / total_yes
    high_no_probability = no_count / total_no

    return high_yes_probability, high_no_probability


high_yes_prob, high_no_prob = calculate_high_probability(dataset)
print("Probability of 'High' given 'Yes':", high_yes_prob)
print("Probability of 'High' given 'No':", high_no_prob)


#----------------------------------------------   H U M I D I T Y 
#                                                                               N O R M A L  ----------------------------------------------------->

def calculate_normal_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    yes_count = sum(1 for data in dataset if data[3] == "normal" and data[5] == "yes")
    no_count = sum(1 for data in dataset if data[3] == "normal" and data[5] == "no")

    normal_yes_probability = yes_count / total_yes
    normal_no_probability = no_count / total_no

    return normal_yes_probability, normal_no_probability


normal_yes_prob, normal_no_prob = calculate_normal_probability(dataset)
print("Probability of 'Normal' given 'Yes':", normal_yes_prob)
print("Probability of 'Normal' given 'No':", normal_no_prob)


#----------------------------------------------   W I N D 
#                                                                               S T R O N G  ----------------------------------------------------->

def calculate_strong_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    yes_count = sum(1 for data in dataset if data[4] == "strong" and data[5] == "yes")
    no_count = sum(1 for data in dataset if data[4] == "strong" and data[5] == "no")

    strong_yes_probability = yes_count / total_yes
    strong_no_probability = no_count / total_no

    return strong_yes_probability, strong_no_probability


strong_yes_prob, strong_no_prob = calculate_strong_probability(dataset)
print("Probability of 'Strong' given 'Yes':", strong_yes_prob)
print("Probability of 'Strong' given 'No':", strong_no_prob)


#----------------------------------------------   W I N D 
#                                                                               W E A K  ----------------------------------------------------->

def calculate_weak_probability(dataset):
    total_yes = sum(1 for data in dataset if data[5] == "yes")
    total_no = sum(1 for data in dataset if data[5] == "no")

    yes_count = sum(1 for data in dataset if data[4] == "weak" and data[5] == "yes")
    no_count = sum(1 for data in dataset if data[4] == "weak" and data[5] == "no")

    weak_yes_probability = yes_count / total_yes
    weak_no_probability = no_count / total_no

    return weak_yes_probability, weak_no_probability

weak_yes_prob, weak_no_prob = calculate_weak_probability(dataset)
print("Probability of 'Weak' given 'Yes':", weak_yes_prob)
print("Probability of 'Weak' given 'No':", weak_no_prob)
print(calculate_sunny_probability(dataset))



# Given input
user_input = ["sunny", "cool", "high", "strong"]

# Calculate probabilities
probability_yes = no_calculate_probability(dataset)
probability_no = yes_calculate_probability(dataset)



"""
# Calculate the final formula based on user input
attribute_formulas = {
    "sunny": calculate_sunny_probability(dataset),
    "cool": calculate_cool_probability(dataset),
    "high": calculate_high_probability(dataset),
    "strong": calculate_strong_probability(dataset)
}

probability_formula = probability_yes
for attr in user_input:
    if attr in attribute_formulas:
        attr_formula = attribute_formulas[attr]
        probability_formula *= attr_formula()

print("Probability formula based on user input:", probability_formula)
"""

for input in user_input:
    formula = 0 
    if 'sunny' == input:
        data_one_yes = sunny_yes_prob
        data_one_no = sunny_no_prob
    
    if 'overcast' == input:
        data_one_yes = overcast_yes_prob
        data_one_no = overcast_no_prob

    if 'rain' == input:
        data_one_yes = rain_yes_prob
        data_one_no = rain_no_prob

#------------------------------------------------------------>   
  
    if 'cool' == input:
        data_two_yes = cool_yes_prob
        data_two_no = cool_no_prob

    if 'mild' == input:
        data_two_yes = mild_yes_prob
        data_two_no = mild_no_prob

    if 'hot' == input:
        data_two_yes = hot_yes_prob
        data_two_no = hot_no_prob
#------------------------------------------------------------> 
    
    if 'high' == input:
        data_three_yes = high_yes_prob
        data_three_no = high_no_prob 

    if 'normal' == input:
        data_three_yes = normal_yes_prob
        data_three_no = normal_no_prob 
    
  
    if 'strong' == input:
        data_four_yes = strong_yes_prob
        data_four_no = strong_no_prob 
    
    if 'weak' == input:
        data_four_yes = weak_yes_prob
        data_four_no = weak_no_prob 

        
final_probablity_yes = (data_one_yes * data_two_yes * data_three_yes *data_four_yes )* yes_probability
final_probablity_no = (data_one_no * data_two_no * data_three_no *data_four_no )* no_probability
print("Final Probability:",round(final_probablity_yes,4))
print("Final Probability:",round(final_probablity_no,4))


# Create a list of data variables
data_list_yes = [data_one_yes, data_two_yes, data_three_yes, data_four_yes, ]
data_list_no = [data_one_no, data_two_no, data_three_no, data_four_no, ]

# Filter out variables with zero value
filtered_data_list_A = [data for data in data_list_yes if data != 0.0]
filtered_data_list_B = [data for data in data_list_no if data != 0.0]

# Calculate the final probability
final_yes_probability = 1.0
for data in filtered_data_list_A:
    final_yes_probability *= data
    a = final_yes_probability * yes_probability 
print("Final yes Probability:", a)

final_no_probability = 1.0
for data in filtered_data_list_B:
    final_no_probability *= data
    a = final_no_probability * no_probability 
print("Final no Probability:", a)






