P = 10 ** 9 + 7


def main():
    outdata = []
    for testcase in range(int(input())):
        n, k, moves, x, y = read_data()
        solve(moves, k, x, y, outdata)
    print('\n'.join(outdata))


def read_data():
    n, k, x, y = input().split()
    n, k = int(n), int(k)
    moves = []
    for _ in range(n):
        opcode, *ops = input().split()
        moves.append((opcode, ops))
    return n, k, moves, x, y


def convFp(s):
    a, b = map(int, s.split('/'))
    return a * pow(b, -1, P) % P



def solve(moves, k, zr, zi, outdata):
    zr = convFp(zr)
    zi = convFp(zi)
    finalop = (1, 0, 0, 0, 0, 0, 1, 0, False)
    for opcode, ops in moves:
        if opcode == 'T':
            (ur, ui) = map(convFp, ops)
            mop = (1, 0, ur, ui, 0, 0, 1, 0, False)
        elif opcode == 'R':
            (ur, ui) = map(convFp, ops)
            mop = (ur, -ui, 0, 0, 0, 0, 1, 0, False)
        elif opcode == 'S':
            c = convFp(ops[0])
            mop = (c, 0, 0, 0, 0, 0, 1, 0, False)
        elif opcode == 'F' and ops[0] == 'X':
            mop = (1, 0, 0, 0, 0, 0, 1, 0, True)
        elif opcode == 'F' and ops[0] == 'Y':
            mop = (-1, 0, 0, 0, 0, 0, 1, 0, True)
        elif opcode == 'I':
            mop = (0, 0, 1, 0, 1, 0, 0, 0, True)
        else:
            raise ValueError('unknown opcode')
        finalop = opmul(mop, finalop)

    finalop = oppow(finalop, k)
    outdata.append(opapply(finalop, (zr, zi)))


def opmul(mop1, mop2):
    sar, sai, sbr, sbi, scr, sci, sdr, sdi, sconj = mop1
    oar, oai, obr, obi, ocr, oci, odr, odi, oconj = mop2
    conj = sconj ^ oconj
    if sconj:
        oai = -oai
        obi = -obi
        oci = -oci
        odi = -odi
    ar = (sar * oar - sai * oai + sbr * ocr - sbi * oci) % P
    ai = (sar * oai + sai * oar + sbr * oci + sbi * ocr) % P
    br = (sar * obr - sai * obi + sbr * odr - sbi * odi) % P
    bi = (sar * obi + sai * obr + sbr * odi + sbi * odr) % P
    cr = (scr * oar - sci * oai + sdr * ocr - sdi * oci) % P
    ci = (scr * oai + sci * oar + sdr * oci + sdi * ocr) % P
    dr = (scr * obr - sci * obi + sdr * odr - sdi * odi) % P
    di = (scr * obi + sci * obr + sdr * odi + sdi * odr) % P
    return (ar, ai, br, bi, cr, ci, dr, di, conj)


def oppow(mop, exp):
    if exp < 0: raise RuntimeError('no exp<0')
    oppow2, ret = mop, (1, 0, 0, 0, 0, 0, 1, 0, False)
    for bit in range(exp.bit_length()):
        if 1 << bit & exp:
            ret = opmul(ret, oppow2)
        oppow2 = opmul(oppow2, oppow2)
    return ret


def opapply(mop, z):
    ar, ai, br, bi, cr, ci, dr, di, conj = mop
    zr, zi = z
    if conj: zi = -zi
    divdr = (ar * zr - ai * zi + br) % P
    divdi = (ar * zi + ai * zr + bi) % P
    divrr = (cr * zr - ci * zi + dr) % P
    divri = (cr * zi + ci * zr + di) % P
    if divrr == 0 and divri == 0:
        return 'WONDERLAND'
    else:
        divrabs = pow(divrr * divrr + divri * divri, -1, P)
        retr = (divdr * divrr + divdi * divri) * divrabs % P
        reti = (-divdr * divri + divdi * divrr) * divrabs % P
        return f'{retr} {reti}'


main()

