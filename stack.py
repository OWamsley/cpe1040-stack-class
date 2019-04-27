class Stack():
    def __init__(self, sample):
        self.stack = []
        self.sample = sample
        print("New Stack object")
        pass

    def pop(self):
        print("Popping...")
        removed = self.stack.pop()
        return removed

    def push(self, value):
        expect_type(value, self.sample)
        print("Pushing...")
        self.stack.append(value)
        pass


def expect_type(given_value, sample):
    if not isinstance(given_value, type(sample)):
        raise ValueError('Expected ' + type(sample) + ' but got {}'.format(type(given_value)))
    else:
        print('Got a ' + type(sample) + ' value {}'.format(given_value))
