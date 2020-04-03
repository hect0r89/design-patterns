class CodeBuilder:
    def __init__(self, root_name):
        self.root_name = root_name
        self.attributes = []

    def add_field(self, type, name):
        self.attributes.append({'type': type, 'name': name})
        return self

    def __str__(self):
        lines = []
        lines.append('class {}:'.format(self.root_name))
        lines.append('  def __init__(self):')
        for attribute in self.attributes:
            lines.append('    self.{} = {}'.format(attribute["type"], attribute["name"]))
        return '\n'.join(lines)


if __name__ == '__main__':
    cb = CodeBuilder('Person').add_field('name', '""').add_field('age', '0')
    print(cb)