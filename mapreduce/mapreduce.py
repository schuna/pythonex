import random
import string
import os
from threading import Thread
from tempfile import TemporaryDirectory


class InputData(object):
    def read(self):
        raise NotImplementedError


class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()


class Worker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError


class LineCountWorker(Worker):
    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def generate_inputs(data_dir):
    for name in os.listdir(data_dir):
        yield PathInputData(os.path.join(data_dir, name))


def create_workers(input_list):
    workers = []
    for input_data in input_list:
        workers.append(LineCountWorker(input_data))
    return workers


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


def map_reduce(data_dir):
    inputs = generate_inputs(data_dir)
    workers = create_workers(inputs)
    return execute(workers)


def write_test_files(tmp_dir):
    letters = string.ascii_lowercase
    for i in range(10):
        with open(os.path.join(tmp_dir, "{:02d}.txt".format(i)), 'w') as wf:
            for j in range(random.randint(10, 20)):
                wf.write("".join(random.choice(letters) for k in range(random.randint(8, 16))) + "\n")


with TemporaryDirectory() as tmpdir:
    write_test_files(tmpdir)
    result = map_reduce(tmpdir)

print(f'There are {result} lines')