# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)

#Code starts here

census=np.concatenate((data,new_record))


age=census[:,0]
print(age)
max_age,min_age=age.max(),age.min()
print(max_age)
print(min_age)
age_mean=age.mean()
age_std=np.std(age)
print(age_mean)
print(age_std)


race_0=census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3=census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0,len_1,len_2,len_3,len_4=len(race_0),len(race_1),len(race_2),len(race_3),len(race_4)
print(len_0,len_1,len_2,len_3,len_4)
lenlist=[len_0,len_1,len_2,len_3,len_4]
minority_race=min(lenlist)
for i in range(len(lenlist)):
    if minority_race==lenlist[i]:
        minority_race=i
        break
print(minority_race)        


senior_citizens=census[census[:,0]>60]
working_hours_sum=senior_citizens[:,6].sum()
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(working_hours_sum,avg_working_hours)


high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=high[:,7].mean()
avg_pay_low=low[:,7].mean()
print(avg_pay_high,avg_pay_low)


