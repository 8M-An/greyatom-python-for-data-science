# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Creating a new variable to store the value counts
loan_status=data['Loan_Status'].value_counts()
#Plotting bar plot
loan_status.plot(kind='bar')
plt.show()
# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status'])
property_and_loan=property_and_loan.size().unstack()
property_and_loan.plot(kind='bar',stacked=False)
#Changing the x-axis label
plt.xlabel('Property Area')
#Changing the y-axis label
plt.ylabel('Loan Status')
#Rotating the ticks of X-axis
plt.xticks(rotation=45)
# Step 3
#Plotting a stacked bar plot
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)
#Changing the x-axis label
plt.xlabel('Education Status')
#Changing the y-axis label
plt.ylabel('Loan Status')
#Rotating the ticks of X-axis
plt.xticks(rotation=45)
plt.show()
# Step 4 
#Subsetting the dataframe based on 'Education' column
graduate=data[data['Education']=='Graduate']
#Subsetting the dataframe based on 'Education' column
not_graduate=data[data['Education']=='Not Graduate']
#Plotting density plot for 'Graduate'
graduate['LoanAmount'].plot(kind='density',label='Graduate')
#Plotting density plot for 'Not Graduate'
not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')
#For automatic legend display

# Step 5
#Setting up the subplots
fig,(ax_1,ax_2,ax_3)=plt.subplots(3,1,figsize=(20,10))
#Plotting scatter plot
data['TotalIncome'] = data['CoapplicantIncome'] + data['ApplicantIncome']
ax_1.scatter(data['ApplicantIncome'],data['LoanAmount'])
ax_2.scatter(data['CoapplicantIncome'],data['LoanAmount'])
ax_3.scatter(data['TotalIncome'],data['LoanAmount'])
#Setting the subplot axis title
ax_1.set_title('Applicant Income')
ax_2.set_title('Coapplicant Income')
ax_3.set_title('Total Income')
#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title


