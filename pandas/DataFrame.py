import pandas as pd
import numpy as np

employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp00'],
    'Name': ['John Doe', 'William Spark'],
    'Occupation': ['Chemist', 'Statistician'],
    'Date Of Join': ['2018-01-25', '2018-01-26'],
    'Age': [23, 24]},
    index=['Emp001', 'Emp002'],
    columns=['Name', 'Occupation', 'Date Of Join', 'Age'])

print(employees)
employees = pd.DataFrame({
    'EmpCode': ['Emp001', 'Emp002', 'Emp003', 'Emp004', 'Emp005'],
    'Name': ['John', 'Doe', 'William', 'Spark', 'Mark'],
    'Occupation': ['Chemist', 'Statistician', 'Statistician',
                   'Statistician', 'Programmer'],
    'Date Of Join': ['2018-01-25', '2018-01-26', '2018-01-26', '2018-02-26',
                     '2018-03-16'],
    'Age': [23, 24, 34, 29, 40]})

# Adding column to dataframe
employees['City'] = ['London', 'Tokyo', 'Sydney', 'London', 'Toronto']
# employees.loc[len(employees)]=[45,....]

print("\nUse < operator\n")
print(employees.loc[employees['Age'] < 30])

print("\nUse isin operator\n")
print(employees.loc[employees['Occupation'].isin(['Chemist','Programmer'])])

print("\nMultiple Conditions\n")
print(employees.loc[(employees['Occupation'] == 'Chemist') |
                    (employees['Name'] == 'John') &
                    (employees['Age'] < 30)])

# Iterate over rows 
print("\n Example ittertuples \n")
for row in employees.itertuples(index=True,name="Pandas"):
    #note that index=True and "Pandas" are default
    print(row)
    print(getattr(row,"Name"),"--->",getattr(row,"Age"))
print("The row type is {}".format(type(row)))
# -> pandas.core.frame.Pandas'
print("The employees type is {}".format(type(employees)))
# -> pandas.core.frame.DataFrame'
print("\n Drop Column by Name \n")
employees.drop('Age', axis=1, inplace=True)
print(employees)

print("\n Drop Column by Index \n")
employees.drop(employees.columns[[0,1]], axis=1, inplace=True)
print(employees)

print("\n Selecting multiple columns from dataframe \n")
df = employees[['Occupation', 'City']]
print(df)

df_random=pd.DataFrame(np.random.randint(100,size=(10,6)),columns=list('ABCDEF'),index=['Row--{}'.format(i) for i in range(10)])
print(df_random)

######  loc selects data only by labels       #########

df = pd.DataFrame({'Age': [30, 20, 22, 40, 32, 28, 39],
                   'Color': ['Blue', 'Green', 'Red', 'White', 'Gray', 'Black',
                             'Red'],
                   'Food': ['Steak', 'Lamb', 'Mango', 'Apple', 'Cheese',
                            'Melon', 'Beans'],
                   'Height': [165, 70, 120, 80, 180, 172, 150],
                   'Score': [4.6, 8.3, 9.0, 3.3, 1.8, 9.5, 2.2],
                   'State': ['NY', 'TX', 'FL', 'AL', 'AK', 'TX', 'TX']
                   },
                  index=['Jane', 'Nick', 'Aaron', 'Penelope', 'Dean',
                         'Christina', 'Cornelia'])

print(df)
print("\n -- Selecting a single row with .loc with a string -- \n")
print(df.loc['Penelope'])

print("\n -- Selecting multiple rows with .loc with a list of strings -- \n")
print(df.loc[['Cornelia', 'Jane', 'Dean']])

print("\n -- Selecting multiple rows with .loc with slice notation -- \n")
print(df.loc['Aaron':'Dean'])

print("\n -- Selecting a single row with .iloc with an integer -- \n")
print(df.iloc[4])

print("\n -- Selecting multiple rows with .iloc with a list of integers -- \n")
print(df.iloc[[2, -2]])

print("\n -- Selecting multiple rows with .iloc with slice notation -- \n")
print(df.iloc[:5:3])
###### .iloc selects data only by integer location ######

##### loc can also do boolean but iloc cannot #####

print("\n -- loc -- \n")
print(df.loc[df['Age'] < 30, ['Color', 'Height']])

print("\n -- iloc -- \n")
print(df.iloc[(df['Age'] < 30).values, [1, 3]])

print("\n -- getting the index of the dataframe -- \n")
print(df.index)

print("\n -- getting the columns of the dataframe -- \n")
print(df.columns)

print("\n -- getting the values of the dataframe --\n")
print(df.values)
