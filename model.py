import tensorflow as tf
import random

starters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','@']

one_step_reloaded = tf.saved_model.load('one_step')

states = None
next_char = tf.constant([random.choice(starters)])
result = [next_char]

for n in range(100):
  next_char, states = one_step_reloaded.generate_one_step(next_char, states=states)
  result.append(next_char)

print(tf.strings.join(result)[0].numpy().decode("utf-8"))