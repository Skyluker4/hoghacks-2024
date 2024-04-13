import pandas as pd
import numpy as np
import tensorflow as tf
from sklearn.model_selection import KFold, train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import mean_absolute_error
from keras.models import Sequential
from keras.layers import Dense, Dropout
from keras import regularizers
from keras.optimizers import schedules, SGD, RMSprop
from keras.callbacks import EarlyStopping, TensorBoard
from keras.utils import to_categorical
from scipy import stats

# Load the data
data = pd.read_csv('bwdata.tsv', sep='\t')

data = data.drop(['Team', 'Opposing Team', 'Defensive Front', 'Defensive Coverage', 'Defensive Play'], axis=1)

# Preprocess the data into floats
le = LabelEncoder()
for col in data.columns:
    if data[col].dtype == 'object' and col != 'Offensive Play':
        data[col] = le.fit_transform(data[col])

le_y = LabelEncoder()
data['Offensive Play'] = le_y.fit_transform(data['Offensive Play'])

data = data.astype(float)

# Set any NaN values to the mean of the column and any infinite values to NaN
data = data.fillna(data.mean())
data = data.replace([np.inf, -np.inf], np.nan)
data = data.fillna(data.max())

z_scores = stats.zscore(data)
abs_z_scores = np.abs(z_scores)
filtered_entries = (abs_z_scores < 3).all(axis=1)
data = data[filtered_entries]

# Split the data into features and labels
X = data.drop('Offensive Play', axis=1)
y = data['Offensive Play']

# Encode the labels
print("Shape of y before encoding:", y.shape)
y_encoded = le.fit_transform(y)
y_encoded = to_categorical(y_encoded)
print("Shape of y after encoding:", y_encoded.shape)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2)

#kf = KFold(n_splits=5)
#for train_index, test_index in kf.split(X):
#    X_train, X_test = X.iloc[train_index], X.iloc[test_index]
#    y_train, y_test = y.iloc[train_index], y.iloc[test_index]

# Normalize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create the model
model = Sequential([
    Dense(64, activation='elu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.5),
    Dense(32, activation='elu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.5),
    Dense(16, activation='elu', kernel_regularizer=regularizers.l2(0.01)),
    Dropout(0.5),
    Dense(len(le.classes_), activation='softmax')
])

# Learning rate scheduler
lr_schedule = schedules.ExponentialDecay(
    initial_learning_rate=1e-2,
    decay_steps=10000,
    decay_rate=0.9
)
optimizer = RMSprop(learning_rate=lr_schedule)

# Compile the model
model.compile(optimizer=optimizer, loss='categorical_crossentropy', metrics=['accuracy'])

# Early stopping
early_stop = EarlyStopping(monitor='loss', patience=20, restore_best_weights=True)

# Fit the model
model.fit(X_train_scaled, y_train, epochs=200, validation_split=0.2, callbacks=[early_stop])

# Show the model's output compare to the actual values
y_pred = model.predict(X_test_scaled)
y_pred_labels = np.argmax(y_pred, axis=1)
y_test_labels = np.argmax(y_test, axis=1)

df = pd.DataFrame({'Actual': y_test_labels, 'Predicted': y_pred_labels})
print(df)
_, accuracy = model.evaluate(X_test_scaled, y_test, verbose=0)
print('Accuracy:', accuracy*100)

# Convert predictions back to categorical values
y_test_original = le_y.inverse_transform(y_test_labels)
y_pred_original = le_y.inverse_transform(y_pred_labels)
print(pd.DataFrame({'Actual': y_test_original, 'Predicted': y_pred_original}))

# Save the model
#model.save('NN-Model.keras')
