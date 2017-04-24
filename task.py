#!/usr/bin/env python

import sys

import tensorflow as tf
import cv2

import pagan

if len(sys.argv) != 2:
    print('Usage: {} <id>'.format(argv[0]))
    exit(1)

img_data = cv2.imread('cit.jpg')

image = tf.constant(img_data)

result = tf.reduce_mean(tf.log(image))

with tf.Session() as sess:
    value = sess.run(result)

avatar = pagan.Avatar(str(value), pagan.SHA512)
avatar.save('/data_cifs/bnavetta', 'test-' + sys.argv[1])
