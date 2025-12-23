class Vowel:
    __slots__ = ("a", "e", "i", "o", "u", "y")

    def __init__(self, **kw):
        for k, v in kw.items():
            if k in "aeiouy":
                setattr(self, k, v)

    def __str__(self):
        parts = []
        for ch in "aeiouy":
            if hasattr(self, ch):
                parts.append(f"{ch}: {getattr(self, ch)}")
        return ", ".join(parts)

    @property
    def answer(self):
        return 42

    @answer.setter
    def answer(self, v):
        raise AttributeError("answer is read-only")

    @property
    def full(self):
        for ch in "aeiouy":
            if not hasattr(self, ch):
                return False
        return True

    @full.setter
    def full(self, v):
        pass

import sys
exec(sys.stdin.read())
