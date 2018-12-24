import threading
import time
import requests

# 获取毫秒级时间
def get_time_ms():
    ct = time.time()    # 时间戳
    local_time = time.localtime(ct) # 本地化时间
    cart_time_strftime = time.strftime("%Y-%m-%d %H:%M:%S", local_time)  # 格式化时间
    cart_time_strftime_ms = (ct - int(ct)) * 1000
    ms = "%s.%03d" % (cart_time_strftime, cart_time_strftime_ms) # 拼接，获取毫秒级时间
    return ms

# 定义请求函数
def test():
    # session = requests.session()
    # url = "https://www.cnblogs.com/xuxiongbing/p/9475772.html"
    # try:
    #     jmt_request = session.get(url)
    #     status_code = jmt_request.status_code
    #     return status_code
    # except Exception as e:
    #     return str(e)   
    print('11')


if __name__ == '__main__':
    threads = []
    for jk in range(1,100000):
        s = threading.Thread(target=test,args=())    # 把请求函数加入多线程中去
        threads.append(s)    

    for t in threads:
        t.setDaemon(True)           # 把多线程设置为守护线程
        t.start()             # 开始执行多线程
        print (('%s 执行时间为 %s') % (t,get_time_ms()))     # 输出执行时间
    t.join()       # 阻塞主线程执行
    print("all over %s" % get_time_ms())
    exit()