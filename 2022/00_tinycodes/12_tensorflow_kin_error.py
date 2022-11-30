import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split

x_train = np.array(
    [
        [105.06, 99.83],
        [101.88, 99.40],
        [98.28, 99.71],
        [96.06, 100.02],
        [97.63, 99.84],
        [99.62, 100.23],
        [99.83, 100.69],
        [99.40, 100.03],
        [99.05, 100.33],
        [98.59, 99.92],
        [99.51, 99.89],
        [101.82, 100.13],
        [102.55, 100.03],
        [103.97, 99.82],
        [104.71, 100.40],
        [104.66, 100.53],
        [105.53, 99.89],
        [107.07, 100.72],
        [107.90, 101.21],
        [107.59, 100.63],
        [109.31, 100.65],
        [111.48, 100.38],
        [109.41, 100.81],
        [109.11, 101.74],
        [111.04, 101.53],
        [117.16, 102.07],
        [119.20, 102.56],
        [119.79, 102.68],
        [123.31, 103.24],
        [123.43, 103.89],
        [117.40, 104.60],
        [115.77, 104.03],
        [115.18, 104.10],
    ]
)
y_train = np.array([1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])

x_train, x_test, y_train, y_test = train_test_split(x_train, y_train, test_size=0.2)

model = Sequential()
model.add(Dense(1, input_dim=2, activation="sigmoid"))

model.compile(optimizer="sgd", loss="binary_crossentropy", metrics=["binary_accuracy"])
hist = model.fit(x_train, y_train, epochs=5000)

# 모델 손실 함수 시각화
plt.plot(hist.history["loss"], "b-", label="loss")
plt.title("Model loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.legend()
plt.show()

# 모델 정확도 시각화
plt.plot(hist.history["binary_accuracy"], "g-", label="accuracy")
plt.title("Model Accuracy")
plt.xlabel("Epoch")
plt.ylabel("Accuracy")
plt.legend()
plt.show()

# 손실 함수 계산
model.evaluate(x_test, y_test, batch_size=1, verbose=2)

# 모델 시각화
print(x_test)
print(min(x_test), max(x_test), 0.01)
line_x = np.arange(min(x_test), max(x_test), 0.01)
line_y = model.predict(line_x)

plt.plot(line_x, line_y, "r-")
plt.plot(x_test, y_test, "bo")
plt.title("Model")
plt.xlabel("test")
plt.ylabel("predict")
plt.legend(["predict", "test"], loc="upper left")
plt.show()