library("MASS")   
print(str(Cars93))   
# Loading the Mass library.   

# Creating a data frame from the main data set.   
car_data<- data.frame(Cars93$AirBags, Cars93$Type)   
# Creating a table with the needed variables.   
car_data = table(Cars93$AirBags, Cars93$Type)    
print(car_data)   
# Performing the Chi-Square test.   
print(chisq.test(car_data))
