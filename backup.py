 # Given input
      
        data_one_A = 0.0
        data_one_B = 0.0
        data_one_C = 0.0
        data_one_D = 0.0
        data_one_E = 0.0

        data_two_A = 0.0
        data_two_B = 0.0
        data_two_C = 0.0
        data_two_D = 0.0
        data_two_E = 0.0

        data_three_A = 0.0
        data_three_B = 0.0
        data_three_C = 0.0
        data_three_D = 0.0
        data_three_E = 0.0

        data_four_A = 0.0
        data_four_B = 0.0
        data_four_C = 0.0
        data_four_D = 0.0
        data_four_E = 0.0

        data_five_A = 0.0
        data_five_B = 0.0
        data_five_C = 0.0
        data_five_D = 0.0
        data_five_E = 0.0
        



        for input in result:
            
            
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

                print("A:",data_one_A)
                print("B:",data_one_B)
                print("C",data_one_C)
                print("D",data_one_D)
                print("E:",data_one_E)


        
                # Create a list of data variables
                data_list_A = [data_one_A, data_two_A, data_three_A, data_four_A, data_five_A]
                data_list_B = [data_one_B, data_two_B, data_three_B, data_four_B, data_five_B]
                data_list_C = [data_one_C, data_two_C, data_three_C, data_four_C, data_five_C]
                data_list_D = [data_one_D, data_two_D, data_three_D, data_four_D, data_five_D]
                data_list_E = [data_one_E, data_two_E, data_three_E, data_four_E, data_five_E]
                print(data_list_A)
                print(data_list_B)
                print(data_list_C)
                print(data_list_D)
                print(data_list_E)

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


                

                # Filter out variables with zero value
                filtered_data_list_A = [data for data in data_list_A if data != 0.0]
                filtered_data_list_B = [data for data in data_list_B if data != 0.0]
                filtered_data_list_C = [data for data in data_list_C if data != 0.0]
                filtered_data_list_D = [data for data in data_list_D if data != 0.0]
                filtered_data_list_E = [data for data in data_list_E if data != 0.0]

                # Calculate the final probability of A
                final_A_probability = 1.0
                Final_A = 0
                for data in filtered_data_list_A:
                    final_A_probability *= data
                    Final_A = final_A_probability * A_probability 
                print("Final Probability of A:", Final_A)

                # Calculate the final probability of B
                final_B_probability = 1.0
                Final_B = 0
                for data in filtered_data_list_B:
                    final_B_probability *= data
                    Final_B = final_B_probability * B_probability 
                print("Final Probability of B:", Final_B)

                # Calculate the final probability of C
                final_C_probability = 1.0
                Final_C = 0
                for data in filtered_data_list_C:
                    final_C_probability *= data
                    Final_C = final_C_probability * C_probability 
                print("Final Probability of C:", Final_C)

                # Calculate the final probability of D
                final_D_probability = 1.0
                Final_D = 0
                for data in filtered_data_list_D:
                    final_D_probability *= data
                    Final_D = final_D_probability * D_probability 
                print("Final Probability of D:", Final_D)

                # Calculate the final probability of E
                final_E_probability = 1.0
                Final_E = 0
                for data in filtered_data_list_E:
                    final_E_probability *= data
                    Final_E = final_E_probability * E_probability 
                print("Final Probability of E:", Final_E)
                

                variables = [Final_A, Final_B, Final_C, Final_D, Final_E]
                max_value = max(variables)
                max_variable = None

                if max_value == Final_A:
                    max_variable = 'Final_A'
                elif max_value == Final_B:
                    max_variable = 'Final_B'
                elif max_value == Final_C:
                    max_variable = 'Final_C'
                elif max_value == Final_D:
                    max_variable = 'Final_D'
                elif max_value == Final_E:
                    max_variable = 'Final_E'

                print("The variable with the highest value is:", max_variable)
                return Final_A,Final_B,Final_C,Final_D,Final_E