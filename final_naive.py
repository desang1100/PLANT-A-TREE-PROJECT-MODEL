dataset = [
    
    [2, "small", "urban planting", "fair", "rainy", "_small",'C'],
    [3, "small", "agroforestry", "poor", "cloudy", "very_small","B"],
    [4, "medium", "agroforestry", "good", "sunny", "_medium","A"],
    [5, "medium", "urban planting", "fair", "rainy", "_small",'B'],
    [6, "medium", "reforestation", "good", "cloudy", "_small",'A'],
    [7, "very small", "agroforestry", "poor", "sunny", "very_small","B"],
    [8, "small", "agroforestry", "fair", "rainy", "_small","D"],
    [9, "large", "reforestation", "good", "cloudy", "_medium","B"],
    [10, "very large", "urban planting", "fair", "sunny", "very_large","E"],
    [11, "large", "reforestation", "poor", "sunny", "_large", "C"],
    [12, "medium", "urban planting", "good", "rainy", "_medium", "B"],
    [13, "small", "agroforestry", "fair", "cloudy", "_small", "A"],
    [14, "very small", "urban planting", "good", "sunny", "very_small", "D"],
    [15, "very large", "reforestation", "fair", "rainy", "_large", "E"],
    [16, "large", "agroforestry", "poor", "cloudy", "_large", "A"],
    [17, "small", "reforestation", "good", "sunny", "_small", "B"],
    [18, "medium", "urban planting", "fair", "rainy", "_medium", "C"],
    [19, "very large", "agroforestry", "good", "cloudy", "_large", "D"],
    [20, "very small", "reforestation", "fair", "sunny", "very_small", "E"],
    [21, "small", "reforestation", "good", "sunny", "_small", "A"],
    [22, "large", "urban planting", "fair", "rainy", "_large", "B"],
    [23, "medium", "agroforestry", "poor", "cloudy", "_medium", "C"],
    [24, "very large", "agroforestry", "good", "sunny", "_large", "D"],
    [25, "very small", "urban planting", "fair", "rainy", "very_small", "E"],
    [26, "large", "reforestation", "good", "cloudy", "_large", "A"],
    [27, "small", "agroforestry", "poor", "sunny", "_small", "B"],
    [28, "medium", "agroforestry", "good", "rainy", "_medium", "C"],
    [29, "very small", "urban planting", "fair", "cloudy", "very_small", "D"],
    [30, "large", "reforestation", "good", "sunny", "_large", "E"],
    [31, "small", "agroforestry", "poor", "rainy", "_small", "A"],
    [32, "medium", "urban planting", "good", "cloudy", "_medium", "B"],
    [33, "very large", "agroforestry", "fair", "sunny", "_large", "C"],
    [34, "very small", "reforestation", "good", "rainy", "very_small", "D"],
    [35, "large", "urban planting", "fair", "cloudy", "_large", "E"],
    [36, "medium", "agroforestry", "poor", "sunny", "_medium", "A"],
    [37, "small", "reforestation", "good", "rainy", "_small", "B"],
    [38, "large", "urban planting", "fair", "sunny", "_large", "C"],
    [39, "medium", "agroforestry", "good", "cloudy", "_medium", "D"],
    [40, "very small", "reforestation", "fair", "rainy", "very_small", "E"],
    [41, "small", "agroforestry", "good", "cloudy", "_small", "A"],
    [42, "large", "urban planting", "fair", "sunny", "_large", "B"],
    [43, "medium", "reforestation", "poor", "rainy", "_medium", "C"],
    [44, "very large", "agroforestry", "good", "cloudy", "_large", "D"],
    [45, "very small", "urban planting", "fair", "sunny", "very_small", "E"],
    [46, "large", "agroforestry", "poor", "cloudy", "_large", "A"],
    [47, "small", "reforestation", "good", "sunny", "_small", "B"],
    [48, "medium", "urban planting", "fair", "rainy", "_medium", "C"],
    [49, "very large", "agroforestry", "good", "cloudy", "_large", "D"],
    [50, "very small", "reforestation", "fair", "sunny", "very_small", "E"],
    # Add more data sets here
]




#---------------------------------------------- PREDICTION  A PROBABILITY -----------------------------------------------------> 


def A_calculate_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_data = len(dataset)
    probability = total_A / total_data
    print("Total  of A:", total_A)
    print("Total Number  of data in dataset:", total_data)
    return probability


A_probability = A_calculate_probability(dataset)

print(f"Probability of A: {A_probability}")
print("-------------------------------------------->\n")



#---------------------------------------------- PREDICTION  B PROBABILITY -----------------------------------------------------> 


def B_calculate_probability(dataset):
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_data = len(dataset)
    probability = total_B / total_data
    print("Total Number  of B:", total_B)
    print("Total Number  of data in dataset:", total_data)
    return probability


B_probability = B_calculate_probability(dataset)
print("Probability of B:", B_probability)
print("-------------------------------------------->\n")


#---------------------------------------------- PREDICTION  C PROBABILITY -----------------------------------------------------> 


def C_calculate_probability(dataset):
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_data = len(dataset)
    probability = total_C / total_data
    print("Total Number  of C:", total_C)
    print("Total Number  of data in dataset:", total_data)
    return probability


C_probability = C_calculate_probability(dataset)
print("Probability of C:", C_probability)
print("-------------------------------------------->\n")


#---------------------------------------------- PREDICTION  D PROBABILITY -----------------------------------------------------> 


def D_calculate_probability(dataset):
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_data = len(dataset)
    probability = total_D / total_data
    print("Total Number  of D:", total_D)
    print("Total Number  of data in dataset:", total_data)
    return probability


D_probability = D_calculate_probability(dataset)
print("Probability of D:", D_probability)
print("-------------------------------------------->\n")

#---------------------------------------------- PREDICTION  B PROBABILITY -----------------------------------------------------> 


def E_calculate_probability(dataset):
    total_E = sum(1 for data in dataset if data[6] == "E")
    total_data = len(dataset)
    probability = total_E / total_data
    print("Total Number  of E:", total_E)
    print("Total Number  of data in dataset:", total_data)
    return probability


E_probability = E_calculate_probability(dataset)
print("Probability of E:", E_probability)
print("-------------------------------------------->\n")


#---------------------------------------------- END OF A - E PROBABILITY -----------------------------------------------------> 
#---------------------------------------------- END OF A - E PROBABILITY -----------------------------------------------------> 
#---------------------------------------------- END OF A - E PROBABILITY -----------------------------------------------------> 
#---------------------------------------------- END OF A - E PROBABILITY -----------------------------------------------------> 




#-----------------------------------   A R E A   S I Z E 
#                                                                           V E R Y   S M A L L ---------------------------------------->

def calculate_very_small_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    very_small_A_count = sum(1 for data in dataset if data[1] == "very small" and data[6] == "A")
    very_small_B_count = sum(1 for data in dataset if data[1] == "very small" and data[6] == "B")
    very_small_C_count = sum(1 for data in dataset if data[1] == "very small" and data[6] == "C")
    very_small_D_count = sum(1 for data in dataset if data[1] == "very small" and data[6] == "D")
    very_small_E_count = sum(1 for data in dataset if data[1] == "very small" and data[6] == "E")


    very_small_A_probability = very_small_A_count / total_A
    very_small_B_probability = very_small_B_count / total_B
    very_small_C_probability = very_small_C_count / total_C
    very_small_D_probability = very_small_D_count / total_D
    very_small_E_probability = very_small_E_count / total_E
    

    return very_small_A_probability, very_small_B_probability, very_small_C_probability,very_small_D_probability,very_small_E_probability


very_small_A_probability, very_small_B_probability, very_small_C_probability,very_small_D_probability,very_small_E_probability = calculate_very_small_probability(dataset)
print("Probability of 'very small' given 'A': ", very_small_A_probability)
print("Probability of 'very small' given 'B': ", very_small_B_probability)
print("Probability of 'very small' given 'C': ", very_small_C_probability)
print("Probability of 'very small' given 'D': ", very_small_D_probability)
print("Probability of 'very small' given 'E': ", very_small_E_probability)
print("--------------------------------------------------------------------->\n")

#-----------------------------------   A R E A   S I Z E 
#                                                                             S M A L L ---------------------------------------->


def calculate_small_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    small_A_count = sum(1 for data in dataset if data[1] == "small" and data[6] == "A")
    small_B_count = sum(1 for data in dataset if data[1] == "small" and data[6] == "B")
    small_C_count = sum(1 for data in dataset if data[1] == "small" and data[6] == "C")
    small_D_count = sum(1 for data in dataset if data[1] == "small" and data[6] == "D")
    small_E_count = sum(1 for data in dataset if data[1] == "small" and data[6] == "E")


    small_A_probability = small_A_count / total_A
    small_B_probability = small_B_count / total_B
    small_C_probability = small_C_count / total_C
    small_D_probability = small_D_count / total_D
    small_E_probability = small_E_count / total_E
    

    return small_A_probability, small_B_probability, small_C_probability,small_D_probability,small_E_probability


small_A_probability, small_B_probability, small_C_probability,small_D_probability,small_E_probability = calculate_small_probability(dataset)
print("Probability of 'small' given 'A': ", small_A_probability)
print("Probability of 'small' given 'B': ", small_B_probability)
print("Probability of 'small' given 'C': ", small_C_probability)
print("Probability of 'small' given 'D': ", small_D_probability)
print("Probability of 'small' given 'E': ", small_E_probability)
print("--------------------------------------------------------------------->\n")


#-----------------------------------   A R E A   S I Z E 
#                                                                             M E D I U M ---------------------------------------->


def calculate_medium_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    medium_A_count = sum(1 for data in dataset if data[1] == "medium" and data[6] == "A")
    medium_B_count = sum(1 for data in dataset if data[1] == "medium" and data[6] == "B")
    medium_C_count = sum(1 for data in dataset if data[1] == "medium" and data[6] == "C")
    medium_D_count = sum(1 for data in dataset if data[1] == "medium" and data[6] == "D")
    medium_E_count = sum(1 for data in dataset if data[1] == "medium" and data[6] == "E")


    medium_A_probability = medium_A_count / total_A
    medium_B_probability = medium_B_count / total_B
    medium_C_probability = medium_C_count / total_C
    medium_D_probability = medium_D_count / total_D
    medium_E_probability = medium_E_count / total_E
    

    return medium_A_probability, medium_B_probability, medium_C_probability,medium_D_probability,medium_E_probability


medium_A_probability, medium_B_probability, medium_C_probability,medium_D_probability,medium_E_probability = calculate_medium_probability(dataset)
print("Probability of 'medium' given 'A': ", medium_A_probability)
print("Probability of 'medium' given 'B': ", medium_B_probability)
print("Probability of 'medium' given 'C': ", medium_C_probability)
print("Probability of 'medium' given 'D': ", medium_D_probability)
print("Probability of 'medium' given 'E': ", medium_E_probability)
print("--------------------------------------------------------------------->\n")


#-----------------------------------   A R E A   S I Z E 
#                                                                             L A R G E ---------------------------------------->


def calculate_large_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    large_A_count = sum(1 for data in dataset if data[1] == "large" and data[6] == "A")
    large_B_count = sum(1 for data in dataset if data[1] == "large" and data[6] == "B")
    large_C_count = sum(1 for data in dataset if data[1] == "large" and data[6] == "C")
    large_D_count = sum(1 for data in dataset if data[1] == "large" and data[6] == "D")
    large_E_count = sum(1 for data in dataset if data[1] == "large" and data[6] == "E")


    large_A_probability = large_A_count / total_A
    large_B_probability = large_B_count / total_B
    large_C_probability = large_C_count / total_C
    large_D_probability = large_D_count / total_D
    large_E_probability = large_E_count / total_E
    

    return large_A_probability, large_B_probability, large_C_probability,large_D_probability,large_E_probability


large_A_probability, large_B_probability, large_C_probability,large_D_probability,large_E_probability = calculate_large_probability(dataset)
print("Probability of 'large' given 'A': ", large_A_probability)
print("Probability of 'large' given 'B': ", large_B_probability)
print("Probability of 'large' given 'C': ", large_C_probability)
print("Probability of 'large' given 'D': ", large_D_probability)
print("Probability of 'large' given 'E': ", large_E_probability)
print("--------------------------------------------------------------------->\n")


#-----------------------------------   A R E A   S I Z E 
#                                                                             V E R Y   L A R G E ---------------------------------------->


def calculate_very_large_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    very_large_A_count = sum(1 for data in dataset if data[1] == "very large" and data[6] == "A")
    very_large_B_count = sum(1 for data in dataset if data[1] == "very large" and data[6] == "B")
    very_large_C_count = sum(1 for data in dataset if data[1] == "very large" and data[6] == "C")
    very_large_D_count = sum(1 for data in dataset if data[1] == "very large" and data[6] == "D")
    very_large_E_count = sum(1 for data in dataset if data[1] == "very large" and data[6] == "E")


    very_large_A_probability = very_large_A_count / total_A
    very_large_B_probability = very_large_B_count / total_B
    very_large_C_probability = very_large_C_count / total_C
    very_large_D_probability = very_large_D_count / total_D
    very_large_E_probability = very_large_E_count / total_E
    

    return very_large_A_probability, very_large_B_probability, very_large_C_probability,very_large_D_probability,very_large_E_probability


very_large_A_probability, very_large_B_probability, very_large_C_probability,very_large_D_probability,very_large_E_probability = calculate_very_large_probability(dataset)
print("Probability of 'very large' given 'A': ", very_large_A_probability)
print("Probability of 'very large' given 'B': ", very_large_B_probability)
print("Probability of 'very large' given 'C': ", very_large_C_probability)
print("Probability of 'very large' given 'D': ", very_large_D_probability)
print("Probability of 'very large' given 'E': ", very_large_E_probability)
print("--------------------------------------------------------------------->\n")


#----------------------------   P R O J E C T   S C O P E 
#                                                                      R E F O R E S T A T I O N  ---------------------------------------->

def calculate_reforestation_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    reforestation_A_count = sum(1 for data in dataset if data[2] == "reforestation" and data[6] == "A")
    reforestation_B_count = sum(1 for data in dataset if data[2] == "reforestation" and data[6] == "B")
    reforestation_C_count = sum(1 for data in dataset if data[2] == "reforestation" and data[6] == "C")
    reforestation_D_count = sum(1 for data in dataset if data[2] == "reforestation" and data[6] == "D")
    reforestation_E_count = sum(1 for data in dataset if data[2] == "reforestation" and data[6] == "E")


    reforestation_A_probability = reforestation_A_count / total_A
    reforestation_B_probability = reforestation_B_count / total_B
    reforestation_C_probability = reforestation_C_count / total_C
    reforestation_D_probability = reforestation_D_count / total_D
    reforestation_E_probability = reforestation_E_count / total_E
    

    return reforestation_A_probability, reforestation_B_probability, reforestation_C_probability,reforestation_D_probability,reforestation_E_probability


reforestation_A_probability, reforestation_B_probability, reforestation_C_probability,reforestation_D_probability,reforestation_E_probability = calculate_reforestation_probability(dataset)
print("Probability of 'reforestation' given 'A': ", reforestation_A_probability)
print("Probability of 'reforestation' given 'B': ", reforestation_B_probability)
print("Probability of 'reforestation' given 'C': ", reforestation_C_probability)
print("Probability of 'reforestation' given 'D': ", reforestation_D_probability)
print("Probability of 'reforestation' given 'E': ", reforestation_E_probability)
print("--------------------------------------------------------------------->\n")


#----------------------------   P R O J E C T   S C O P E 
#                                                                      U R B A N   P  L A N T I N G  ---------------------------------------->

def calculate_urban_planting_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    urban_planting_A_count = sum(1 for data in dataset if data[2] == "urban planting" and data[6] == "A")
    urban_planting_B_count = sum(1 for data in dataset if data[2] == "urban planting" and data[6] == "B")
    urban_planting_C_count = sum(1 for data in dataset if data[2] == "urban planting" and data[6] == "C")
    urban_planting_D_count = sum(1 for data in dataset if data[2] == "urban planting" and data[6] == "D")
    urban_planting_E_count = sum(1 for data in dataset if data[2] == "urban planting" and data[6] == "E")


    urban_planting_A_probability = urban_planting_A_count / total_A
    urban_planting_B_probability = urban_planting_B_count / total_B
    urban_planting_C_probability = urban_planting_C_count / total_C
    urban_planting_D_probability = urban_planting_D_count / total_D
    urban_planting_E_probability = urban_planting_E_count / total_E
    

    return urban_planting_A_probability, urban_planting_B_probability, urban_planting_C_probability,urban_planting_D_probability,urban_planting_E_probability


urban_planting_A_probability, urban_planting_B_probability, urban_planting_C_probability,urban_planting_D_probability,urban_planting_E_probability = calculate_urban_planting_probability(dataset)
print("Probability of 'urban planting' given 'A': ", urban_planting_A_probability)
print("Probability of 'urban planting' given 'B': ", urban_planting_B_probability)
print("Probability of 'urban planting' given 'C': ", urban_planting_C_probability)
print("Probability of 'urban planting' given 'D': ", urban_planting_D_probability)
print("Probability of 'urban planting' given 'E': ", urban_planting_E_probability)
print("--------------------------------------------------------------------->\n")


#----------------------------   P R O J E C T   S C O P E 
#                                                                      A G R O F O R E S T R Y  ---------------------------------------->

def calculate_agroforestry_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    agroforestry_A_count = sum(1 for data in dataset if data[2] == "agroforestry" and data[6] == "A")
    agroforestry_B_count = sum(1 for data in dataset if data[2] == "agroforestry" and data[6] == "B")
    agroforestry_C_count = sum(1 for data in dataset if data[2] == "agroforestry" and data[6] == "C")
    agroforestry_D_count = sum(1 for data in dataset if data[2] == "agroforestry" and data[6] == "D")
    agroforestry_E_count = sum(1 for data in dataset if data[2] == "agroforestry" and data[6] == "E")


    agroforestry_A_probability = agroforestry_A_count / total_A
    agroforestry_B_probability = agroforestry_B_count / total_B
    agroforestry_C_probability = agroforestry_C_count / total_C
    agroforestry_D_probability = agroforestry_D_count / total_D
    agroforestry_E_probability = agroforestry_E_count / total_E
    

    return agroforestry_A_probability, agroforestry_B_probability, agroforestry_C_probability,agroforestry_D_probability,agroforestry_E_probability


agroforestry_A_probability, agroforestry_B_probability, agroforestry_C_probability,agroforestry_D_probability,agroforestry_E_probability = calculate_agroforestry_probability(dataset)
print("Probability of 'agroforestry' given 'A': ", agroforestry_A_probability)
print("Probability of 'agroforestry' given 'B': ", agroforestry_B_probability)
print("Probability of 'agroforestry' given 'C': ", agroforestry_C_probability)
print("Probability of 'agroforestry' given 'D': ", agroforestry_D_probability)
print("Probability of 'agroforestry' given 'E': ", agroforestry_E_probability)
print("--------------------------------------------------------------------->\n")

#----------------------------   S O I L   C O  N  D I T I O N 
#                                                                        G O O D  ---------------------------------------->


def calculate_good_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    good_A_count = sum(1 for data in dataset if data[3] == "good" and data[6] == "A")
    good_B_count = sum(1 for data in dataset if data[3] == "good" and data[6] == "B")
    good_C_count = sum(1 for data in dataset if data[3] == "good" and data[6] == "C")
    good_D_count = sum(1 for data in dataset if data[3] == "good" and data[6] == "D")
    good_E_count = sum(1 for data in dataset if data[3] == "good" and data[6] == "E")


    good_A_probability = good_A_count / total_A
    good_B_probability = good_B_count / total_B
    good_C_probability = good_C_count / total_C
    good_D_probability = good_D_count / total_D
    good_E_probability = good_E_count / total_E
    

    return good_A_probability, good_B_probability, good_C_probability,good_D_probability,good_E_probability


good_A_probability, good_B_probability, good_C_probability,good_D_probability,good_E_probability = calculate_good_probability(dataset)
print("Probability of 'good' given 'A': ", good_A_probability)
print("Probability of 'good' given 'B': ", good_B_probability)
print("Probability of 'good' given 'C': ", good_C_probability)
print("Probability of 'good' given 'D': ", good_D_probability)
print("Probability of 'good' given 'E': ", good_E_probability)
print("--------------------------------------------------------------------->\n")


#-----------------------------------   S O I L   C O  N  D I T I O N  
#                                                                        F A I R ---------------------------------------->


def calculate_fair_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    fair_A_count = sum(1 for data in dataset if data[3] == "fair" and data[6] == "A")
    fair_B_count = sum(1 for data in dataset if data[3] == "fair" and data[6] == "B")
    fair_C_count = sum(1 for data in dataset if data[3] == "fair" and data[6] == "C")
    fair_D_count = sum(1 for data in dataset if data[3] == "fair" and data[6] == "D")
    fair_E_count = sum(1 for data in dataset if data[3] == "fair" and data[6] == "E")


    fair_A_probability = fair_A_count / total_A
    fair_B_probability = fair_B_count / total_B
    fair_C_probability = fair_C_count / total_C
    fair_D_probability = fair_D_count / total_D
    fair_E_probability = fair_E_count / total_E
    

    return fair_A_probability, fair_B_probability, fair_C_probability,fair_D_probability,fair_E_probability


fair_A_probability, fair_B_probability, fair_C_probability,fair_D_probability,fair_E_probability = calculate_fair_probability(dataset)
print("Probability of 'fair' given 'A': ", fair_A_probability)
print("Probability of 'fair' given 'B': ", fair_B_probability)
print("Probability of 'fair' given 'C': ", fair_C_probability)
print("Probability of 'fair' given 'D': ", fair_D_probability)
print("Probability of 'fair' given 'E': ", fair_E_probability)
print("--------------------------------------------------------------------->\n")

#-----------------------------------   S O I L   C O  N  D I T I O N   
#                                                                        P O O R ---------------------------------------->


def calculate_poor_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    poor_A_count = sum(1 for data in dataset if data[3] == "poor" and data[6] == "A")
    poor_B_count = sum(1 for data in dataset if data[3] == "poor" and data[6] == "B")
    poor_C_count = sum(1 for data in dataset if data[3] == "poor" and data[6] == "C")
    poor_D_count = sum(1 for data in dataset if data[3] == "poor" and data[6] == "D")
    poor_E_count = sum(1 for data in dataset if data[3] == "poor" and data[6] == "E")


    poor_A_probability = poor_A_count / total_A
    poor_B_probability = poor_B_count / total_B
    poor_C_probability = poor_C_count / total_C
    poor_D_probability = poor_D_count / total_D
    poor_E_probability = poor_E_count / total_E
    

    return poor_A_probability, poor_B_probability, poor_C_probability,poor_D_probability,poor_E_probability


poor_A_probability, poor_B_probability, poor_C_probability,poor_D_probability,poor_E_probability = calculate_poor_probability(dataset)
print("Probability of 'poor' given 'A': ", poor_A_probability)
print("Probability of 'poor' given 'B': ", poor_B_probability)
print("Probability of 'poor' given 'C': ", poor_C_probability)
print("Probability of 'poor' given 'D': ", poor_D_probability)
print("Probability of 'poor' given 'E': ", poor_E_probability)
print("--------------------------------------------------------------------->\n")


#------------------------   W E A T H E R   C O N D I T  I O N  
#                                                                              S U N N Y -------------------------------------->


def calculate_sunny_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    sunny_A_count = sum(1 for data in dataset if data[4] == "sunny" and data[6] == "A")
    sunny_B_count = sum(1 for data in dataset if data[4] == "sunny" and data[6] == "B")
    sunny_C_count = sum(1 for data in dataset if data[4] == "sunny" and data[6] == "C")
    sunny_D_count = sum(1 for data in dataset if data[4] == "sunny" and data[6] == "D")
    sunny_E_count = sum(1 for data in dataset if data[4] == "sunny" and data[6] == "E")


    sunny_A_probability = sunny_A_count / total_A
    sunny_B_probability = sunny_B_count / total_B
    sunny_C_probability = sunny_C_count / total_C
    sunny_D_probability = sunny_D_count / total_D
    sunny_E_probability = sunny_E_count / total_E
    

    return sunny_A_probability, sunny_B_probability, sunny_C_probability,sunny_D_probability,sunny_E_probability


sunny_A_probability, sunny_B_probability, sunny_C_probability,sunny_D_probability,sunny_E_probability = calculate_sunny_probability(dataset)
print("Probability of 'sunny' given 'A': ", sunny_A_probability)
print("Probability of 'sunny' given 'B': ", sunny_B_probability)
print("Probability of 'sunny' given 'C': ", sunny_C_probability)
print("Probability of 'sunny' given 'D': ", sunny_D_probability)
print("Probability of 'sunny' given 'E': ", sunny_E_probability)
print("--------------------------------------------------------------------->\n")


#------------------------   W E A T H E R   C O N D I T  I O N  
#                                                                             R A I N Y  -------------------------------------->


def calculate_rainy_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    rainy_A_count = sum(1 for data in dataset if data[4] == "rainy" and data[6] == "A")
    rainy_B_count = sum(1 for data in dataset if data[4] == "rainy" and data[6] == "B")
    rainy_C_count = sum(1 for data in dataset if data[4] == "rainy" and data[6] == "C")
    rainy_D_count = sum(1 for data in dataset if data[4] == "rainy" and data[6] == "D")
    rainy_E_count = sum(1 for data in dataset if data[4] == "rainy" and data[6] == "E")


    rainy_A_probability = rainy_A_count / total_A
    rainy_B_probability = rainy_B_count / total_B
    rainy_C_probability = rainy_C_count / total_C
    rainy_D_probability = rainy_D_count / total_D
    rainy_E_probability = rainy_E_count / total_E
    

    return rainy_A_probability, rainy_B_probability, rainy_C_probability,rainy_D_probability,rainy_E_probability


rainy_A_probability, rainy_B_probability, rainy_C_probability,rainy_D_probability,rainy_E_probability = calculate_rainy_probability(dataset)
print("Probability of 'rainy' given 'A': ", rainy_A_probability)
print("Probability of 'rainy' given 'B': ", rainy_B_probability)
print("Probability of 'rainy' given 'C': ", rainy_C_probability)
print("Probability of 'rainy' given 'D': ", rainy_D_probability)
print("Probability of 'rainy' given 'E': ", rainy_E_probability)
print("--------------------------------------------------------------------->\n")



#------------------------   W E A T H E R   C O N D I T  I O N  
#                                                                            C L O U D Y -------------------------------------->


def calculate_cloudy_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    cloudy_A_count = sum(1 for data in dataset if data[4] == "cloudy" and data[6] == "A")
    cloudy_B_count = sum(1 for data in dataset if data[4] == "cloudy" and data[6] == "B")
    cloudy_C_count = sum(1 for data in dataset if data[4] == "cloudy" and data[6] == "C")
    cloudy_D_count = sum(1 for data in dataset if data[4] == "cloudy" and data[6] == "D")
    cloudy_E_count = sum(1 for data in dataset if data[4] == "cloudy" and data[6] == "E")


    cloudy_A_probability = cloudy_A_count / total_A
    cloudy_B_probability = cloudy_B_count / total_B
    cloudy_C_probability = cloudy_C_count / total_C
    cloudy_D_probability = cloudy_D_count / total_D
    cloudy_E_probability = cloudy_E_count / total_E
    

    return cloudy_A_probability, cloudy_B_probability, cloudy_C_probability,cloudy_D_probability,cloudy_E_probability


cloudy_A_probability, cloudy_B_probability, cloudy_C_probability,cloudy_D_probability,cloudy_E_probability = calculate_cloudy_probability(dataset)
print("Probability of 'cloudy' given 'A': ", cloudy_A_probability)
print("Probability of 'cloudy' given 'B': ", cloudy_B_probability)
print("Probability of 'cloudy' given 'C': ", cloudy_C_probability)
print("Probability of 'cloudy' given 'D': ", cloudy_D_probability)
print("Probability of 'cloudy' given 'E': ", cloudy_E_probability)
print("--------------------------------------------------------------------->\n")




#-----------------------------------   P A R T I C I P A N T S 
#                                                                           V E R Y   S M A L L ---------------------------------------->

def calculate_participant_very_small_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    participant_very_small_A_count = sum(1 for data in dataset if data[5] == "very_small" and data[6] == "A")
    participant_very_small_B_count = sum(1 for data in dataset if data[5] == "very_small" and data[6] == "B")
    participant_very_small_C_count = sum(1 for data in dataset if data[5] == "very_small" and data[6] == "C")
    participant_very_small_D_count = sum(1 for data in dataset if data[5] == "very_small" and data[6] == "D")
    participant_very_small_E_count = sum(1 for data in dataset if data[5] == "very_small" and data[6] == "E")


    participant_very_small_A_probability = participant_very_small_A_count / total_A
    participant_very_small_B_probability = participant_very_small_B_count / total_B
    participant_very_small_C_probability = participant_very_small_C_count / total_C
    participant_very_small_D_probability = participant_very_small_D_count / total_D
    participant_very_small_E_probability = participant_very_small_E_count / total_E
    

    return participant_very_small_A_probability, participant_very_small_B_probability, participant_very_small_C_probability,participant_very_small_D_probability,participant_very_small_E_probability


participant_very_small_A_probability, participant_very_small_B_probability, participant_very_small_C_probability,participant_very_small_D_probability,participant_very_small_E_probability = calculate_participant_very_small_probability(dataset)
print("Probability of 'very small' given 'A': ", participant_very_small_A_probability)
print("Probability of 'very small' given 'B': ", participant_very_small_B_probability)
print("Probability of 'very small' given 'C': ", participant_very_small_C_probability)
print("Probability of 'very small' given 'D': ", participant_very_small_D_probability)
print("Probability of 'very small' given 'E': ", participant_very_small_E_probability)
print("--------------------------------------------------------------------->\n")

#-----------------------------------   P A R T I C I P A N T S 
#                                                                             S M A L L ---------------------------------------->


def calculate_participant_small_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    participant_small_A_count = sum(1 for data in dataset if data[5] == "_small" and data[6] == "A")
    participant_small_B_count = sum(1 for data in dataset if data[5] == "_small" and data[6] == "B")
    participant_small_C_count = sum(1 for data in dataset if data[5] == "_small" and data[6] == "C")
    participant_small_D_count = sum(1 for data in dataset if data[5] == "_small" and data[6] == "D")
    participant_small_E_count = sum(1 for data in dataset if data[5] == "_small" and data[6] == "E")


    participant_small_A_probability = participant_small_A_count / total_A
    participant_small_B_probability = participant_small_B_count / total_B
    participant_small_C_probability = participant_small_C_count / total_C
    participant_small_D_probability = participant_small_D_count / total_D
    participant_small_E_probability = participant_small_E_count / total_E
    

    return participant_small_A_probability, participant_small_B_probability, participant_small_C_probability,participant_small_D_probability,participant_small_E_probability


participant_small_A_probability, participant_small_B_probability, participant_small_C_probability,participant_small_D_probability,participant_small_E_probability = calculate_participant_small_probability(dataset)
print("Probability of 'small' given 'A': ", participant_small_A_probability)
print("Probability of 'small' given 'B': ", participant_small_B_probability)
print("Probability of 'small' given 'C': ", participant_small_C_probability)
print("Probability of 'small' given 'D': ", participant_small_D_probability)
print("Probability of 'small' given 'E': ", participant_small_E_probability)
print("--------------------------------------------------------------------->\n")


#-----------------------------------    P A R T I C I P A N T S 
#                                                                             M E D I U M ---------------------------------------->


def calculate_participant_medium_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    participant_medium_A_count = sum(1 for data in dataset if data[5] == "_medium" and data[6] == "A")
    participant_medium_B_count = sum(1 for data in dataset if data[5] == "_medium" and data[6] == "B")
    participant_medium_C_count = sum(1 for data in dataset if data[5] == "_medium" and data[6] == "C")
    participant_medium_D_count = sum(1 for data in dataset if data[5] == "_medium" and data[6] == "D")
    participant_medium_E_count = sum(1 for data in dataset if data[5] == "_medium" and data[6] == "E")


    participant_medium_A_probability = participant_medium_A_count / total_A
    participant_medium_B_probability = participant_medium_B_count / total_B
    participant_medium_C_probability = participant_medium_C_count / total_C
    participant_medium_D_probability = participant_medium_D_count / total_D
    participant_medium_E_probability = participant_medium_E_count / total_E
    

    return participant_medium_A_probability, participant_medium_B_probability, participant_medium_C_probability,participant_medium_D_probability,participant_medium_E_probability


participant_medium_A_probability, participant_medium_B_probability, participant_medium_C_probability,participant_medium_D_probability,participant_medium_E_probability = calculate_participant_medium_probability(dataset)
print("Probability of 'medium' given 'A': ", participant_medium_A_probability)
print("Probability of 'medium' given 'B': ", participant_medium_B_probability)
print("Probability of 'medium' given 'C': ", participant_medium_C_probability)
print("Probability of 'medium' given 'D': ", participant_medium_D_probability)
print("Probability of 'medium' given 'E': ", participant_medium_E_probability)
print("--------------------------------------------------------------------->\n")


#-----------------------------------    P A R T I C I P A N T S 
#                                                                             L A R G E ---------------------------------------->


def calculate_participant_large_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    participant_large_A_count = sum(1 for data in dataset if data[5] == "_large" and data[6] == "A")
    participant_large_B_count = sum(1 for data in dataset if data[5] == "_large" and data[6] == "B")
    participant_large_C_count = sum(1 for data in dataset if data[5] == "_large" and data[6] == "C")
    participant_large_D_count = sum(1 for data in dataset if data[5] == "_large" and data[6] == "D")
    participant_large_E_count = sum(1 for data in dataset if data[5] == "_large" and data[6] == "E")


    participant_large_A_probability = participant_large_A_count / total_A
    participant_large_B_probability = participant_large_B_count / total_B
    participant_large_C_probability = participant_large_C_count / total_C
    participant_large_D_probability = participant_large_D_count / total_D
    participant_large_E_probability = participant_large_E_count / total_E
    

    return participant_large_A_probability, participant_large_B_probability, participant_large_C_probability,participant_large_D_probability,participant_large_E_probability


participant_large_A_probability, participant_large_B_probability, participant_large_C_probability,participant_large_D_probability,participant_large_E_probability = calculate_participant_large_probability(dataset)
print("Probability of 'large' given 'A': ", participant_large_A_probability)
print("Probability of 'large' given 'B': ", participant_large_B_probability)
print("Probability of 'large' given 'C': ", participant_large_C_probability)
print("Probability of 'large' given 'D': ", participant_large_D_probability)
print("Probability of 'large' given 'E': ", participant_large_E_probability)
print("--------------------------------------------------------------------->\n")


#-----------------------------------    P A R T I C I P A N T S 
#                                                                             V E R Y   L A R G E ---------------------------------------->


def calculate_participant_very_large_probability(dataset):
    total_A = sum(1 for data in dataset if data[6] == "A")
    total_B = sum(1 for data in dataset if data[6] == "B")
    total_C = sum(1 for data in dataset if data[6] == "C")
    total_D = sum(1 for data in dataset if data[6] == "D")
    total_E = sum(1 for data in dataset if data[6] == "E")
    
    participant_verylarge_A_count = sum(1 for data in dataset if data[5] == "very_large" and data[6] == "A")
    participant_verylarge_B_count = sum(1 for data in dataset if data[5] == "very_large" and data[6] == "B")
    participant_verylarge_C_count = sum(1 for data in dataset if data[5] == "very_large" and data[6] == "C")
    participant_verylarge_D_count = sum(1 for data in dataset if data[5] == "very_large" and data[6] == "D")
    participant_verylarge_E_count = sum(1 for data in dataset if data[5] == "very_large" and data[6] == "E")


    participant_verylarge_A_probability = participant_verylarge_A_count / total_A
    participant_verylarge_B_probability = participant_verylarge_B_count / total_B
    participant_verylarge_C_probability = participant_verylarge_C_count / total_C
    participant_verylarge_D_probability = participant_verylarge_D_count / total_D
    participant_verylarge_E_probability = participant_verylarge_E_count / total_E
    

    return participant_verylarge_A_probability, participant_verylarge_B_probability, participant_verylarge_C_probability,participant_verylarge_D_probability,participant_verylarge_E_probability


participant_verylarge_A_probability, participant_verylarge_B_probability, participant_verylarge_C_probability,participant_verylarge_D_probability,participant_verylarge_E_probability = calculate_participant_very_large_probability(dataset)
print("Probability of 'very large' given 'A': ", participant_verylarge_A_probability)
print("Probability of 'very large' given 'B': ", participant_verylarge_B_probability)
print("Probability of 'very large' given 'C': ", participant_verylarge_C_probability)
print("Probability of 'very large' given 'D': ", participant_verylarge_D_probability)
print("Probability of 'very large' given 'E': ", participant_verylarge_E_probability)
print("--------------------------------------------------------------------->\n")




# Given input
user_input = ["very small", "agroforestry", "good", "sunny","very_small"]

# Calculate probabilities
probability_A = A_calculate_probability(dataset)
probability_B = A_calculate_probability(dataset)
probability_C = A_calculate_probability(dataset)
probability_D = A_calculate_probability(dataset)
probability_E = A_calculate_probability(dataset)
print(probability_A)
print(probability_B)
print(probability_B)
print(probability_D)
print(probability_E)





for input in user_input:
    formula = 0
    if 'very small' == input:
        data_one_A = very_small_A_probability
        data_one_B = very_small_B_probability
        data_one_C = very_small_C_probability
        data_one_D = very_small_D_probability
        data_one_E = very_small_E_probability

    elif 'small' == input:
        data_one_A = small_A_probability
        data_one_B = small_B_probability
        data_one_C = small_C_probability
        data_one_D = small_D_probability
        data_one_E = small_E_probability


    elif 'medium' == input:
        data_one_A = medium_A_probability
        data_one_B = medium_B_probability
        data_one_C = medium_C_probability
        data_one_D = medium_D_probability
        data_one_E = medium_E_probability
        

    elif 'large' == input:
        data_one_A = large_A_probability
        data_one_B = large_B_probability
        data_one_C = large_C_probability
        data_one_D = large_D_probability
        data_one_E = large_E_probability

    elif 'very large' == input:
        data_one_A = very_large_A_probability
        data_one_B = very_large_B_probability
        data_one_C = very_large_C_probability
        data_one_D = very_large_D_probability
        data_one_E = very_large_E_probability

#------------------------------------------------------->

    elif 'reforestion' == input:
        data_two_A = reforestation_A_probability
        data_two_B = reforestation_B_probability  
        data_two_C = reforestation_C_probability  
        data_two_D = reforestation_D_probability  
        data_two_E = reforestation_E_probability  

    elif 'urban planting' == input:
        data_two_A = urban_planting_A_probability
        data_two_B = urban_planting_B_probability
        data_two_C = urban_planting_C_probability
        data_two_D = urban_planting_D_probability
        data_two_E = urban_planting_E_probability

    elif 'agroforestry' == input:
        data_two_A = urban_planting_A_probability
        data_two_B = urban_planting_B_probability
        data_two_C = urban_planting_C_probability
        data_two_D = urban_planting_D_probability
        data_two_E = urban_planting_E_probability

#------------------------------------------------------->

    elif 'good' == input:
        data_three_A = good_A_probability
        data_three_B = good_B_probability
        data_three_C = good_C_probability
        data_three_D = good_D_probability
        data_three_E = good_E_probability
    
    elif 'fair' == input:
        data_three_A = fair_A_probability
        data_three_B = fair_B_probability
        data_three_C = fair_C_probability
        data_three_D = fair_D_probability
        data_three_E = fair_E_probability
    
    elif 'poor' == input:
        data_three_A = poor_A_probability
        data_three_B = poor_B_probability
        data_three_C = poor_C_probability
        data_three_D = poor_D_probability
        data_three_E = poor_E_probability

#------------------------------------------------------->

    elif 'sunny' == input:
        data_four_A = sunny_A_probability
        data_four_B = sunny_B_probability
        data_four_C = sunny_C_probability
        data_four_D = sunny_D_probability
        data_four_E = sunny_E_probability
    
    elif 'rainy' == input:
        data_four_A = rainy_A_probability
        data_four_B = sunny_B_probability
        data_four_C = sunny_C_probability
        data_four_D = sunny_D_probability
        data_four_E = sunny_E_probability

    elif 'cloudy' == input:
        data_four_A = cloudy_A_probability
        data_four_B = cloudy_B_probability
        data_four_C = cloudy_C_probability
        data_four_D = cloudy_D_probability
        data_four_E = cloudy_E_probability

#------------------------------------------------------->   
#   
    elif 'very_small' == input:
        data_five_A = participant_very_small_A_probability
        data_five_B = participant_very_small_B_probability
        data_five_C = participant_very_small_C_probability
        data_five_D = participant_very_small_D_probability
        data_five_E = participant_very_small_E_probability

    
    elif '_small' == input:
        data_five_A = participant_small_A_probability
        data_five_B = participant_small_B_probability
        data_five_C = participant_small_C_probability
        data_five_D = participant_small_D_probability
        data_five_E = participant_small_E_probability

    elif '_medium' == input:
        data_five_A = participant_medium_A_probability
        data_five_B = participant_medium_B_probability
        data_five_C = participant_medium_C_probability
        data_five_D = participant_medium_D_probability
        data_five_E = participant_medium_E_probability
    
    elif '_large' == input:
        data_five_A = participant_large_A_probability
        data_five_B = participant_large_B_probability
        data_five_C = participant_large_C_probability
        data_five_D = participant_large_D_probability
        data_five_E = participant_large_E_probability
    
    elif 'very_large' == input:
        data_five_A = participant_verylarge_A_probability
        data_five_B = participant_verylarge_B_probability
        data_five_C = participant_verylarge_C_probability
        data_five_D = participant_verylarge_D_probability
        data_five_E = participant_verylarge_E_probability

final_A_probablity = (data_one_A * data_two_A * data_three_A * data_four_A * data_five_A )* A_probability
final_B_probablity = (data_one_B * data_two_B * data_three_B * data_four_B * data_five_B )* B_probability
final_C_probablity = (data_one_C * data_two_C * data_three_C * data_four_C * data_five_C )* C_probability
final_D_probablity = (data_one_D * data_two_D * data_three_D * data_four_D * data_five_D )* D_probability
final_E_probablity = (data_one_E * data_two_E * data_three_E * data_four_E * data_five_E )* E_probability

print("Final Probability:",final_A_probablity)
print("Final Probability:",final_B_probablity)
print("Final Probability:",final_C_probablity)
print("Final Probability:",final_D_probablity)
print("Final Probability:",final_E_probablity)

print("--------------------------------------------\n")


# Create a list of data variables
data_list_A = [data_one_A, data_two_A, data_three_A, data_four_A, data_five_A]
data_list_B = [data_one_B, data_two_B, data_three_B, data_four_B, data_five_B]
data_list_C = [data_one_C, data_two_C, data_three_C, data_four_C, data_five_C]
data_list_D = [data_one_D, data_two_D, data_three_D, data_four_D, data_five_D]
data_list_E = [data_one_E, data_two_E, data_three_E, data_four_E, data_five_E]

# Filter out variables with zero value
filtered_data_list_A = [data for data in data_list_A if data != 0.0]
filtered_data_list_B = [data for data in data_list_B if data != 0.0]
filtered_data_list_C = [data for data in data_list_C if data != 0.0]
filtered_data_list_D = [data for data in data_list_D if data != 0.0]
filtered_data_list_E = [data for data in data_list_E if data != 0.0]

# Calculate the final probability of A
final_A_probability = 1.0
for data in filtered_data_list_A:
    final_A_probability *= data
    Final_A = final_A_probability * A_probability 
print("Final Probability of A:", Final_A)

# Calculate the final probability of B
final_B_probability = 1.0
for data in filtered_data_list_B:
    final_B_probability *= data
    Final_B = final_B_probability * B_probability 
print("Final Probability of B:", Final_B)

# Calculate the final probability of C
final_C_probability = 1.0
for data in filtered_data_list_C:
    final_C_probability *= data
    Final_C = final_C_probability * C_probability 
print("Final Probability of C:", Final_C)

# Calculate the final probability of D
final_D_probability = 1.0
for data in filtered_data_list_D:
    final_D_probability *= data
    Final_D = final_D_probability * D_probability 
print("Final Probability of D:", Final_D)

# Calculate the final probability of E
final_E_probability = 1.0
for data in filtered_data_list_E:
    final_E_probability *= data
    Final_E = final_E_probability * E_probability 
print("Final Probability of E:", Final_E)


        







