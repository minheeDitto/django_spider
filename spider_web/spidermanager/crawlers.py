from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings
import psutil
from threading import Thread
from multiprocessing import Process, Lock
import logging


def thread_termiante(process):
    def _terminate(process):
        process.terminate()

    Thread(target=_terminate, args=(Process,)).start()


class SpiderProcess(Process):

    def __init__(self, spiderId, spider_cls, settings):
        self.spiderId = spiderId
        self.spider_cls = spider_cls
        self.settings = settings
        self.lock = Lock()

    def run(self) -> None:
        proc = CrawlerProcess(self.settings)
        proc.crawl(self.spider_cls)
        proc.start()

    def pause(self):
        with self.lock:
            try:
                p = psutil.Process(self.pid)
                p.suspend()
            except Exception as e:
                logging.exception(e)

    def unpause(self):
        with self.lock:
            try:
                p = psutil.Process(self.pid)
                p.resume()
            except Exception as e:
                logging.exception(e)

    def terminate(self) -> None:
        with self.lock:
            try:
                p = psutil.Process(self.pid)
                children = p.children
                for child in children:
                    child.terminate()
                    child.wait()
                p.kill()
                p.wait()
                if psutil.pid_exists(self.pid):
                    p.kill()
            except Exception as e:
                pass

    def is_alive(self) -> bool:
        try:
            p = psutil.Process(self.pid)
            return p.is_running()
        except Exception as e:
            return False


class SpiderManager:
    SpiderJoB = dict(0)

    def __init__(self, settings_file):
        self.settings_file = settings_file

    def create_job(self, spider,):
        proc = SpiderProcess(spider.file_id,)

    def load_settings(self):
        setting = Settings()
        setting.setmodule(self.settings_file)
        return setting

