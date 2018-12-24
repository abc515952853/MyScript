#encoding=utf-8
import multiprocessing
import time
import os
#测试多进程创建空文件夹性能
def test():
    print('111')

if __name__=='__main__':
    #打印开始时间
    print (time.ctime())
    #进程个数，目前设置4
    pool=multiprocessing.Pool(processes=1000)
    for i in range(1000):
        pool.apply_async(test,())
    pool.close()
    pool.join()
    #打印结束时间
    print (time.ctime())