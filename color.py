import struct

'''
color basic manipulation
'''


class Color:
    def color2arbg(col: int) -> list:  # list of a,r,g,b
        return list(struct.pack('=i', int(col)))

    def arbg2color(a: int, r: int, g: int, b: int) -> int:
        return Color.arbgflist2color([a, r, g, b])

    def arbgflist2color(l: list) -> int:  # float list to arbg
        return int.from_bytes(struct.pack('=4B', *list(map(int, l))), byteorder='big')

    def interpolate(org: int, dest: int, ratio: float) -> int:  # org, dest in RRGGBB ratio 0..1 -> return list[r,g,b]
        return Color.arbgflist2color(
            [c[0] + (c[1] - c[0]) * ratio + 0.5 for c in zip(Color.color2arbg(org), Color.color2arbg(dest))])

    def colIndex(col: int, ix: int) -> float: return struct.pack('=i', int(col))[ix % 4] / 255.

    def alphaF(col: int) -> float: return Color.colIndex(col, 0)

    def redF(col: int) -> float: return Color.colIndex(col, 1)

    def greenF(col: int) -> float: return Color.colIndex(col, 2)

    def blueF(col: int) -> float: return Color.colIndex(col, 3)

    def brightness(col: int) -> float:
        return sum([f * Color.colIndex(col, ix) for ix, f in enumerate([0.299, 0.587, 0.114])])

    def CCS(col: int) -> str:
        return "#{0:06x}".format(col & 0xffffff)
