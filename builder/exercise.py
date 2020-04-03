class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.attributes = []

    def add_field(self, type, name):
        self.attributes.append({'type': type, 'name': name})
        return self

    def __str__(self):
        lines = ['class {}:'.format(self.root_name)]
        lines.append('  def __init__(self):') if self.attributes else lines.append('  pass')
        for attribute in self.attributes:
            lines.append('    self.{} = {}'.format(attribute["type"], attribute["name"]))
        return '\n'.join(lines)


if __name__ == '__main__':
    cb = CodeBuilder('Person')
    print(cb)