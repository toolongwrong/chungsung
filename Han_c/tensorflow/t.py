import tensorflow as tf
import os


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


x_data = [[1,7],[1,8],[1,10],[1,2],[1,5],[1,12],[1,23],[1,24],[1,52]]
y_data = [[0],[0],[0],[0],[0],[1],[1],[1],[1]]

W=tf.Variable( tf.random_normal([2,1]))
b=tf.Variable( tf.random_normal([1]))

X= tf.placeholder(tf.float32, shape=[None, 2], name="manjok")
Y=tf.placeholder(tf.float32, shape=[None, 1], name="thatcnt")

hypothesis= tf.sigmoid(tf.matmul(X,W)+b)

cost = tf.reduce_mean(tf.square(hypothesis-Y))

optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.1)
train = optimizer.minimize(cost)

predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)

accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())

    for step in range(100):
        
        cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})


    print("\n TEST")
    print("X: 5, Y:", sess.run(predicted, feed_dict={X:[[1,10]]}))
    print("X: 2.5, Y:", sess.run(predicted, feed_dict={X:[[1,20]]}))
