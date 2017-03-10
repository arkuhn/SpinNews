#Run this to validate your Tensorflow install
import tensorflow as tf

hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello)) #"Hello, Tensorflow!"