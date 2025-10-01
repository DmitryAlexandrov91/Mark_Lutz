class ReverseIter:

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


def test_reverse_iter():
    """Тестирование перевёрнутого итератора."""

    text = "Перевёртыш"
    revers_text = text[::-1]

    assert text != revers_text
    assert revers_text == "".join([_ for _ in ReverseIter(text)])
