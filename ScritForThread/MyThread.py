import requests
import threading
import sys, io
# 解决console显示乱码的编码问题
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Mythread(threading.Thread):
	"""This class customizes the output thu overriding the run() method"""
	def __init__(self, obj):
		super(Mythread, self).__init__()
		self.obj = obj

	def run(self):
		self.obj.test()
		
class test(object):
    def __init__(self):
        self.a=1

    def test(self):
        print(self.a)
        self.a=self.a+1
	
if __name__ == '__main__':
	ThreadApi = test()
	thds = []
	for i in range(100000):
		thd = Mythread(ThreadApi)
		thd.start()
		thds.append(thd)

	for thd in thds:
		thd.join()