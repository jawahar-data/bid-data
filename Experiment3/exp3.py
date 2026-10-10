import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "crime.csv")
crime = pd.read_csv(csv_path)  

plt.plot(crime.Murder, crime.Assault)
plt.title('Murder Vs Assault')
plt.show()

plt.figure(figsize=(12,6))
sns.scatterplot(x=crime.Murder, y=crime.Assault, hue=crime.Murder, s=100)
plt.title('Murder Vs Assault')
plt.show()

plt.hist(crime.Robbery)
plt.title('Histogram for Robbery')
plt.show()

sns.barplot(x='Robbery', y='Year', data=crime)
plt.title('Robbery vs Year')
plt.show()

x = crime.Population
y = crime.CarTheft
plt.scatter(x, y)
plt.xlabel('Population')
plt.ylabel('CarTheft')
plt.title('Population Vs CarTheft') 
plt.show()
