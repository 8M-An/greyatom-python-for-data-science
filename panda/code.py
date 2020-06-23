# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank_data = pd.read_csv(path)
categorical_var=bank_data.select_dtypes(include='object')

numerical_var=bank_data.select_dtypes(include='number')

bank_data.drop(['Loan_ID'],inplace=True,axis=1)
banks=bank_data

n=banks.isnull().sum()

bank_mode=banks.mode()

banks.fillna(bank_mode,inplace=True)

avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount',aggfunc=np.mean)

loan_approved_se=banks.loc[(banks['Self_Employed']== 'Yes') & (banks['Loan_Status']== 'Y'),['Loan_Status']].count()
loan_approved_nse=banks.loc[(banks['Self_Employed']== 'No') & (banks['Loan_Status']== 'Y'),['Loan_Status']].count()
percentage_se=loan_approved_se*(100/614)
percentage_nse=loan_approved_nse*(100/614)


loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=len(loan_term[loan_term>=25])

loan_groupby=banks.groupby('Loan_Status')
loan_groupby=loan_groupby['ApplicantIncome','Credit_History']
mean_values=loan_groupby.mean()
print(mean_values)



