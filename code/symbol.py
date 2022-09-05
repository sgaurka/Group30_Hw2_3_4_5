import math

class Sym:
    n = 0
    at = 0
    name = ""
    _has = {}

    def __init__(self, c: int, s: str):
        if c:
            self.at = c
        if s:
            self.name = s

    def add(self, v: str):
        if v != "?":
            self.n += 1
            self._has[v] = self._has.get(v, 0) + 1

    def mid(self) -> int:
        mode = None
        most = -1
        for k, v in self._has.items():
            if v > most:
                mode, most = k, v
        return mode

    def div(self) -> int:
        def fun(p):
            return p * math.log(p, 2)
        e = 0
        for _, n in self._has.items():
            if n > 0:
                e = e - fun(n / self.n)
        return e


if __name__ == '__main__':
    sym = Sym(c=1, s="Waol")

    sym.add(v="&")
    sym.add(v="*")
    sym.add(v="@")
    sym.add(v="$")

    print(sym.div())
    print(sym.mid())
