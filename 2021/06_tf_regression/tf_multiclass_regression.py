import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

x_data = [
    [25, 10, 3], [29, 6, 4], [0, 1, 1], [28, 2, 0], [12, 14, 1], [5, 13, 3], [28, 1, 4], [20, 0, 3], [5, 2, 0], [3, 0, 1],
    [2, 6, 3], [20, 2, 2], [7, 15, 4], [27, 14, 2], [18, 8, 0], [1, 12, 3], [21, 5, 4], [19, 12, 2], [2, 5, 3], [17, 0, 4],
    [5, 5, 0], [15, 3, 3], [25, 7, 4], [26, 3, 3], [14, 12, 1], [0, 11, 0], [9, 13, 2], [6, 6, 3], [17, 15, 2], [19, 13, 0],
]
y_data = [
    [0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 1, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1],
    [0, 0, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 0, 1], [0, 0, 1], [0, 0, 1], [1, 0, 0], [0, 0, 1], [0, 0, 1],
    [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 1, 0],
]

nb_classes = 3

X = tf.placeholder(tf.float32, [None, nb_classes])
Y = tf.placeholder(tf.float32, [None, nb_classes])

W = tf.Variable(tf.random_normal([3, nb_classes]), name="weight")
b = tf.Variable(tf.random_normal([nb_classes]), name="bias")

logits = tf.matmul(X, W) + b
# 활성함수를 Softmax function을 사용
hypothesis = tf.nn.softmax(logits)

# 텐서플로우는 Softmax 활성함수와 cross-entropy Cost function을 한 번에 정의 가능. 대신 logits인자에 활성함수 적용 '전'을 넣어야 함!
cost_i = tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=Y)

cost = tf.reduce_mean(cost_i)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1).minimize(cost)

# -----------------------------------------------------------------------#

xdata_new = [[1, 11, 7], [1, 3, 4], [1, 1, 0], [1, 1, 0], [25, 10, 3], [17, 15, 2]]

with tf.Session() as sess:
    # sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    for step in range(8001):
        _, cost_val = sess.run([optimizer, cost], feed_dict={X: x_data, Y: y_data})

        if step % 100 == 0:
            print(step, cost_val)
        sess.run(hypothesis, feed_dict={X: x_data})

        a = sess.run(hypothesis, feed_dict={X: xdata_new})
    print(a, sess.run(tf.arg_max(a, 1)))
