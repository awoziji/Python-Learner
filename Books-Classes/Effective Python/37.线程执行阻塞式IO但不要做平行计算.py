 # -*- coding:utf-8 -*-


'''
因为受到全局解释器锁（GIL）的限制，所以多条python线程不能再多个cpu核心上面平行地执行字节码

尽管受制于GIL，但是python的多线程功能依然很有用，它可以轻松地模拟出同一时刻执行多项任务的效果

通过python线程，我们可以平行地执行多个系统调用，这使得程序能够在执行阻塞式I/O操作的同时，执行一些运算操作
'''
