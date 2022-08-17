import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler

df = pd.read_csv(r"C:\Users\KSpicer\Desktop\neural_networks\diabetes.csv")
#print(df.head())

# Investigating our Data Distributions and Normalizing our Histograms:
for i in range(len(df.columns[:-1])):
    label = df.columns[i]
    plt.hist(df[df['Outcome'] == 1][label], color='blue', label="Diabetes", alpha=0.7, density=True, bins=15)
    plt.hist(df[df['Outcome'] == 0][label], color='mediumorchid', label='No diabetes', alpha=0.7, density=True, bins=15)
    plt.title(label)
    plt.ylabel("Probability")
    plt.xlabel(label)
    plt.legend()
    #plt.show()
    plt.clf()

#print(len(df[df['Outcome']==1]), len(df[df['Outcome']==0]))

X = df[df.columns[:-1]].values
#print(X)

y = df[df.columns[-1]].values
#print(y)

# Applying StandardScaler
scaler = StandardScaler()
X = scaler.fit_transform(X)
print(X)

data = np.hstack((X, np.reshape(y, (-1, 1))))
transformed_df = pd.DataFrame(data, columns=df.columns)
print(X.shape)

#for i in range(len(df.columns[:-1])):
    #label = df.columns[i]
    #plt.hist(transformed_df[transformed_df['Outcome'] == 1][label], color='red', label="Diabetes", alpha=0.7, density=True, bins=15)
    #plt.hist(transformed_df[transformed_df['Outcome'] == 0][label], color='mediumorchid', label='No diabetes', alpha=0.7, density=True, bins=15)
    #plt.title(label)
    #plt.ylabel("Probability")
    #plt.xlabel(label)
    #plt.legend()
    #plt.show()

print(len(transformed_df[transformed_df['Outcome'] ==1]), len(transformed_df[transformed_df['Outcome']==0]))

over = RandomOverSampler()
X, y = over.fit_resample(X, y)
print(X.shape, y.shape)

X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.4, random_state=0)
X_valid, X_test, y_valid, y_test = train_test_split(X_temp, y_temp, test_size=0.5, random_state=0)

model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu'), # 'relu means x<=0 --> 0, x>0 --> x
    tf.keras.layers.Dense(16, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), 
             loss=tf.keras.losses.BinaryCrossentropy(),
             metrics=['accuracy'])

model.evaluate(X_train, y_train)
model.evaluate(X_valid, y_valid)

model.fit(X_train, y_train, batch_size=16, epochs=20, validation_data=(X_valid, y_valid))

model.evaluate(X_test, y_test)




