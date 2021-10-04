import random
import string
import os
from threading import Thread
from tempfile import TemporaryDirectory


class GenericInputData(object):
    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))


class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)

    return first.result


def map_reduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


def write_test_files(tmp_dir):
    letters = string.ascii_lowercase
    for i in range(10):
        with open(os.path.join(tmp_dir, "{:02d}.txt".format(i)), 'w') as wf:
            for j in range(random.randint(10, 20)):
                wf.write("".join(random.choice(letters) for k in range(random.randint(8, 16))) + "\n")


with TemporaryDirectory() as tmp_dir:
    write_test_files(tmp_dir)
    config = {'data_dir': tmp_dir}
    result = map_reduce(LineCountWorker, PathInputData, config)

print(f'There are {result} lines')
