import pandas as pd
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tensorflow as tf
import tensorflow_hub as hub

df = pd.read_csv(r'C:\Users\KSpicer\Desktop\neural_networks\wine-reviews.csv', usecols = ['country', 'description', 'points', 'price', 'variety', 'winery'])

df = df.dropna(subset=['description', 'points'])

#plt.hist(df['points'], bins=20)
#plt.show()

df['label'] = (df.points >= 90).astype(int)

df = df[['description', 'label']]

train, val, test = np.split(df.sample(frac=1), [int(0.8*len(df)), int(0.9*len(df))])
len(train), len(val), len(test)

def df_to_dataset(dataframe, shuffle=True, batch_size=1024):
  df = dataframe.copy()
  labels = df.pop('label')
  df = df["description"]
  ds = tf.data.Dataset.from_tensor_slices((df, labels))
  if shuffle:
    ds = ds.shuffle(buffer_size=len(dataframe))
  ds = ds.batch(batch_size)
  ds = ds.prefetch(tf.data.experimental.AUTOTUNE) # original tutorial had tf.data.AUTOTUNE, raised an error, checked Tensorflow 2.3 documentation (https://www.tensorflow.org/versions/r2.3/api_docs/python/tf/data/experimental#other_members) which specifies tf.data.experimental.AUTOTUN instead.
  return ds

train_data = df_to_dataset(train)
valid_data = df_to_dataset(val)
test_data = df_to_dataset(test)

print(list(train_data)[0])

embedding = "https://tfhub.dev/google/nnlm-en-dim50/2"
hub_layer = hub.KerasLayer(embedding, dtype=tf.string, trainable=True)

print(hub_layer(list(train_data)[0][0]))

model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dropout(0.4))
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dropout(0.4))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss=tf.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])

model.evaluate(train_data)
model.evaluate(valid_data)

history = model.fit(train_data, epochs=10, validation_data=valid_data)



