#!/usr/bin/env python
#!coding:utf-8
from threading import  Thread
import  requests
import  matplotlib.pyplot as plt
import  datetime
import  time
import  numpy as np
import  json
class ThreadTest(Thread):
   def __init__(self,func,args=()):
      '''
:param func: 被测试的函数
:param args: 被测试的函数的返回值
      '''
super(ThreadTest,self).__init__()
      self.func=func
      self.args=args
   def run(self) -> None:
      self.result=self.func(*self.args)
   def getResult(self):
      try:
         return self.result
      except BaseException as e:
         return e.args[0]
def baiDu(code,seconds):
   '''
:param code: 状态码
:param seconds: 请求响应时间
:return:
   '''
r=requests.get(url='http://www.baidu.com/')
   code=r.status_code
   seconds=r.elapsed.total_seconds()
   return code,seconds
def calculationTime(startTime,endTime):
   '''计算两个时间之差，单位是秒'''
return (endTime-startTime).seconds
def getResult(seconds):
   '''获取服务端的响应时间信息'''
data={
      'Max':sorted(seconds)[-1],
      'Min':sorted(seconds)[0],
      'Median':np.median(seconds),
      '99%Line':np.percentile(seconds,99),
      '95%Line':np.percentile(seconds,95),
      '90%Line':np.percentile(seconds,90)
   }
   return data
def highConcurrent(count):
   '''
   对服务端发送高并发的请求
:param cout: 并发数
:return:
   '''
startTime=datetime.datetime.now()
   sum=0
   list_count=list()
   tasks=list()
   results = list()
   #失败的信息
   fails=[]
   #成功任务数
   success=[]
   codes = list()
   seconds = list()
   for i in range(1,count):
      t=ThreadTest(baiDu,args=(i,i))
      tasks.append(t)
      t.start()
   for t in tasks:
      t.join()
      if t.getResult()[0]!=200:
         fails.append(t.getResult())
      results.append(t.getResult())
   endTime=datetime.datetime.now()
   for item in results:
      codes.append(item[0])
      seconds.append(item[1])
   for i in range(len(codes)):
      list_count.append(i)
   #生成可视化的趋势图
   fig,ax=plt.subplots()
   ax.plot(list_count,seconds)
   ax.set(xlabel='number of times', ylabel='Request time-consuming',
          title='olap continuous request response time (seconds)')
   ax.grid()
   fig.savefig('test.png')
   plt.show()
   for i in seconds:
      sum+=i
   rate=sum/len(list_count)
   # print('n总共持续时间:n',endTime-startTime)
   totalTime=calculationTime(startTime=startTime,endTime=endTime)
   if totalTime<1:
      totalTime=1
   #吞吐量的计算
   try:
      throughput=int(len(list_count)/totalTime)
   except Exception as e:
      print(e.args[0])
   getResult(seconds=seconds)
   errorRate=0
   if len(fails)==0:
      errorRate=0.00
   else:
      errorRate=len(fails)/len(tasks)*100
   throughput=str(throughput)+'/S'
   timeData=getResult(seconds=seconds)
   dict1={
      '吞吐量':throughput,
      '平均响应时间':rate,
      '响应时间':timeData,
      '错误率':errorRate,
      '请求总数':len(list_count),
      '失败数':len(fails)
   }
   return  json.dumps(dict1,indent=True,ensure_ascii=False)
if __name__ == '__main__':
    print(highConcurrent(count=1000))
