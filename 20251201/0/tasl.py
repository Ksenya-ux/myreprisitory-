C = type(
    'C',
    (),
    {
        'var': 100500,
        '__init__': lambda self, value: setattr(self, 'var', value)
    }
)
