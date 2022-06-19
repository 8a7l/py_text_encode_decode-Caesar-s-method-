# Автор: Василь Онуфрійчук
# Кодувальник.
# https://github.com/8a7l/py_text_encode_decode-Caesar-s-method-
vocabulary='''your vocabulary characters'''
input_text=input('input text:')
step=int(input('step(integer):'))
def encode(vocabulary,input_text,step):
    input_text=list(input_text)
    encode_list=list()
    for i in input_text:
        index_number=0+step
        vocabulary=list(vocabulary)
        for j in vocabulary:
            if i==j:
                encode_list.append(str(index_number))
            index_number+=1
    encode_list=','.join(encode_list)
    return encode_list
print(encode(vocabulary,input_text,step))
