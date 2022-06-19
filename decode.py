# Автор: Василь Онуфрійчук
# Розкодувальник.
# https://github.com/8a7l/py_text_encode_decode-Caesar-s-method-
vocabulary='''your vocabulary characters'''
encode_list=str(input('code list:'))
step=int(input('step(integer):'))
def decode(vocabulary,encode_list,step):
    encode_list=encode_list.split(',')
    text_list=list()
    for i in encode_list:
        try:
            text_list.append(str(vocabulary[int(i)-step]))
        except:
            pass
    text_list=''.join(text_list)
    return text_list
print(decode(vocabulary,encode_list,step))
