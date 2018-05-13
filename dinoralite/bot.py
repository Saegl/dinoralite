import os
import os.path
import random
from typing import List

from .parser import parse, parse_answer, Bhm


class BotError(Exception):
    pass


class Bot:
    def __init__(self, name: str):
        self.name = name
        self.bhms: List[Bhm] = []
        self.answer_fn = {}

    def learn_from_dir(self, modelsdir):
        for basedir, _, files in os.walk(modelsdir):
            for filename in files:
                if filename.endswith('.bhm'):
                    self.learn_from_file(
                        os.path.join(basedir, filename))

    def learn_from_file(self, filename: str):
        with open(filename, encoding='utf-8') as f:
            self.learn_from_data(f.read())

    def learn_from_data(self, data: str):
        self.bhms.extend(parse(data))

    def add_answer_fn(self, name, fn):
        self.answer_fn[name] = fn

    def eval(self, code: str) -> str:
        code = code[2:-1]  # Удалить "@{" вначале и "}" в конце
        code_blocks = code.split()
        fn = self.answer_fn[code_blocks[0]]
        return fn(*code_blocks[1:])

    def build_message(self, bhm: Bhm) -> str:
        answer: str = random.choice(bhm.answers)
        for code in parse_answer(answer):
            answer = answer.replace(code, self.eval(code))
        return answer

    def response(self, s: str) -> str:
        for bhm in self.bhms:
            if bhm.msg.lower() == s.lower():
                return self.build_message(bhm)
        return "Я тебя не понимаю"


if __name__ == '__main__':
    pass
