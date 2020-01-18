# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Code starts here
data = np.genfromtxt(path, delimiter=",", skip_header=1)

census = np.concatenate((data, np.asarray(new_record)))

print(data)
print(census)


# --------------
#Code starts here
age = np.array(census[:, 0])
print(age)

max_age = np.max(age)
min_age = np.min(age)
age_mean = np.mean(age)
age_std = np.std(age)

print("max_age:",max_age,"min_age:",min_age,"age_mean:",age_mean,"age_std:",age_std)

if age_mean > 15:
    print("Young country")
else:
    print("Old country")

# --------------
#Code starts here
race_0 = census[census[:,2] == 0]
race_1 = census[census[:,2] == 1]
race_2 = census[census[:,2] == 2]
race_3 = census[census[:,2] == 3]
race_4 = census[census[:,2] == 4]
#print(race_0)
#print(race_1)
#print(race_2)
#print(race_3)
#print(race_4)

len_0 = race_0.shape[0]
len_1 = race_1.shape[0]
len_2 = race_2.shape[0]
len_3 = race_3.shape[0]
len_4 = race_4.shape[0]
#print(len_0)
#print(len_1)
#print(len_2)
#print(len_3)
#print(len_4)

len_race = np.array([len_0, len_1, len_2, len_3, len_4])
minority_race = list(len_race).index(np.min(len_race))
print(minority_race)


# --------------
#Code starts here
senior_citizens = census[census[:,0] > 60]

working_hours_sum = np.sum(senior_citizens[:,6])

senior_citizens_len = senior_citizens.shape[0]

avg_working_hours = working_hours_sum / senior_citizens_len

print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1] > 10 ]
low = census[census[:,1] <= 10 ]

avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])

if avg_pay_high > avg_pay_low:
    print("It proves that better education leads to better pay")
else:
    print("It does not prove that always better education leads to better pay")


