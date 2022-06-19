# Автор: Василь Онуфрійчук
# Генератор словника.
# https://github.com/8a7l/py_text_encode_decode-Caesar-s-method-
import random
vocabulary='''your vocabulary characters'''
vocabulary=list(vocabulary)
random.shuffle(vocabulary)
new_vocabulary=''.join(vocabulary)
print(new_vocabulary)
pause=input()
