import html


def make_element(name, value, **attrs):
    keyvals = [' %s="%s"' % item for item in attrs.items()]
    attr_str = ''.join(keyvals)
    element = '<{name}{attrs}>{value}</{name}>'.format(
        name=name,
        attrs=attr_str,
        value=html.escape(value))
    return element


# Example
# Creates '<item size="large" quantity="6">Albatross</item>'
print(make_element('item', 'Albatross', size='large', quantity=6))

# Creates '<p>&lt;spam&gt;</p>'
print(make_element('p', '<spam>'))


class A:
    def __init__(*args, **kwargs):
        print(args[0])

    @classmethod
    def a(*args, **kwargs):
        print(*args)

    @staticmethod
    def hh(a, b):
        print(a + b)


a = A(1, 2, 3)
a.a(1, 2)
a.hh(1, 3)
