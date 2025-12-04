import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('cardio_train.csv', sep=';')
df.drop('id', axis=1, inplace=True)
df['age'] = (df['age'] / 365).astype(int)

# Histogram of age
plt.figure(figsize=(8,5))
df['age'].hist(bins=20)
plt.title("Age Distribution")
plt.xlabel("Age (Years)")
plt.ylabel("Count")
plt.show()

# Heart disease count
sns.countplot(x='cardio', data=df)
plt.title("Heart Disease Distribution (0 = No, 1 = Yes)")
plt.show()

# Plot features vs target
features = ['age', 'gender', 'cholesterol', 'gluc', 'smoke', 'alco', 'active']
for feature in features:
    sns.countplot(x=feature, hue='cardio', data=df)
    plt.title(f"{feature} vs Heart Disease")
    plt.show()
