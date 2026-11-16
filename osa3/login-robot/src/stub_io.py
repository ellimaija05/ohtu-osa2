class StubIO:

    def __init__(self, inputs=None):
        self._inputs = inputs or []
        self._outputs = []

    def read(self, prompt):
        if len(self._inputs) > 0:
            return self._inputs.pop(0)
        return ""

    def write(self, value):
        self._outputs.append(value)

    def add_input(self, value):
        self._inputs.append(value)

    @property
    def outputs(self):
        return self._outputs