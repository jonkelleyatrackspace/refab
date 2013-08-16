from base import BaseHandler
from base import *

class Worker(threading.Thread):
   def __init__(self, callback=None, *args, **kwargs):
        super(Worker, self).__init__(*args, **kwargs)
        self.callback = callback

   def run(self):
        import time
        time.sleep(3)
        self.callback('DONE')

class ThreadHandler(tornado.web.RequestHandler):
    @asynchronous
    def get(self):
        Worker(self.worker_done).start()

    def worker_done(self, value):
        self.finish(value)
