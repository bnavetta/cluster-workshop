#!/usr/bin/env python

import sys

import tensorflow as tf
import cv2

img_data = cv2.imread('cit.jpg')

image = tf.constant(img_data)

result = tf.reduce_mean(tf.log(image))

with tf.Session() as sess:
    value = sess.run(result)

with open('/data_cifs/bnavetta/test-{}.txt'.format(sys.argv[1])) as f:
    f.write(str(value))
