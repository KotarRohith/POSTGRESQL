import pandas as pd

# Read the CSV data into a DataFrame
data = pd.read_csv('C:/Users/diksh/OneDrive/Desktop/Projects/customer_data.csv')
# Data transformation: Convert Age to a categorical column
data['Age Group'] = pd.cut(data['Age'],bins=[0, 30, 40, 50, float('inf')], labels=['<30', '30-40', '40-50', '50+'])

data = data.drop_duplicates()


from sqlalchemy import create_engine

# Create a database connection
engine = create_engine('postgresql://postgres:Sonia123!@localhost:5432/TEST-DB')

data.to_sql('customer_data', engine, if_exists='replace', index=False)
# Example: Calculate the average age
average_age = data['Age'].mean()
print(f"Average A: {average_age}")
import matplotlib.pyplot as plt

# Example: Plot age distribution
plt.hist(data['Age'], bins=10)
plt.xlabel('Age')
plt.ylabel('Count')
plt.title('Age Distribution')
plt.show()
