import os
#os.system('ls')

import time  
def performance(f):                                                 #定义装饰器函数，功能是传进来的函数进行包装并返回包装后的函数  
    def fn(*args, **kw):                                            #对传进来的函数进行包装的函数  
        t_start = time.time()                                       #记录函数开始时间   
        r = f(*args, **kw)                                          #调用函数  
        t_end = time.time()                                         #记录函数结束时间   
        print('call %s() in %fs' % (f.__name__, (t_end - t_start)))  #打印调用函数的属性信息，并打印调用函数所用的时间  
        return r                                                    #返回包装后的函数      
    return fn

@performance
def test(n):
    print('test')
    num = 1
    for i in (1,n):
        for j in (1,n):
            num = num*i*j*i*j
    return num
if __name__ == "__main__":
    print(test(10000000000000000000000000000))
