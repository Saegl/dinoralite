from collections import namedtuple

Bhm = namedtuple('Bhm', 'msg answers')


class ParserError(Exception):
    pass


def parse_answer(answer: str):
    pos = 0
    currword = ''
    while pos < len(answer):
        if answer[pos] == '@':
            if answer[pos + 1] == '{':
                while answer[pos] != '}':
                    currword += answer[pos]
                    pos += 1
                currword += answer[pos]
                yield currword
                currword = ''
        else:
            pos += 1


def parse_msg(msg: str) -> Bhm:
    blocks = msg.split('---')
    msg = blocks[0].strip()
    try:
        answers = [s.strip() for s in blocks[1:]]
    except IndexError:
        raise ParserError(
            f'На вопрос "{msg}" не найдено ни одного ответа'
        )
    return Bhm(msg, answers)


def parse(s: str):
    for msg in s.split('msg:'):
        if msg:
            yield parse_msg(msg)


if __name__ == '__main__':
    print(parse_answer('Oh no @{ dffdf } hi  @{ pfff }'))
