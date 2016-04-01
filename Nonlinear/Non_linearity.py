# program returns array specifying nonlinearity of each component function
# takes input as a 1-D array as S-Box.
###########################################################################
# finds Walsh Transform of truth table(f)

S = [239, 78, 47, 165, 205, 178, 9, 175, 233, 123, 251, 216, 58, 26, 96, 199, 220, 15, 206, 83, 154, 235, 143, 245, 64, 79, 210, 63, 42, 82, 69, 134, 111, 50, 227, 229, 159, 156, 160, 145, 197, 124, 72, 228, 55, 77, 2, 189, 10, 18, 209, 122, 100, 20, 226, 129, 34, 37, 137, 200, 31, 240, 242, 62, 87, 136, 91, 59, 7, 106, 90, 135, 198, 27, 179, 158, 139, 241, 138, 144, 104, 211, 97, 148, 19, 108, 125, 192, 118, 46, 230, 12, 109, 161, 195, 221, 93, 246, 248, 196, 99, 225, 52, 120, 49, 188, 73, 67, 238, 207, 119, 163, 232, 43, 35, 254, 215, 21, 126, 127, 113, 41, 61, 75, 94, 172, 141, 89, 71, 219, 110, 45, 150, 234, 36, 112, 171, 131, 11, 237, 102, 32, 250, 54, 208, 4, 213, 29, 180, 243, 168, 60, 169, 201, 214, 13, 114, 116, 223, 23, 244, 185, 181, 84, 190, 247, 53, 28, 255, 6, 193, 253, 149, 167, 202, 17, 66, 22, 57, 191, 186, 44, 130, 14, 170, 1, 81, 105, 48, 88, 236, 155, 95, 25, 152, 166, 252, 38, 217, 5, 0, 157, 65, 176, 16, 140, 103, 76, 40, 121, 249, 173, 218, 24, 115, 183, 147, 68, 153, 231, 142, 3, 224, 187, 107, 177, 86, 51, 146, 132, 74, 133, 212, 56, 164, 174, 98, 203, 182, 30, 70, 39, 117, 80, 128, 33, 184, 8, 85, 222, 162, 194, 204, 151, 101, 92]


def fwt(f):  # f is a Boolean function represented as a TT(0/1) of length 2^n
    import math
    wf = []
    for x in f:
        if x == 0:
            wf.append(1)
        else:
            wf.append(-1)
    order = len(f)  # order = 2^n
    n = int(math.log(order, 2))
    size = int(math.floor(order / 2))
    while size >= 1:
        left = 0
        while left < order - 1:
            for p in range(int(size)):
                right = left + int(size)
                a = wf[left]
                b = wf[right]
                wf[left] = a + b
                wf[right] = a - b
                left = left + 1
            left = right + 1
        size = int(math.floor(size / 2))
    # print"\tWalsh transform of function's truth table is",
    # print wf
    return wf

############################################################################
# finds non-linearity of an n-variable boolean function 'f'


def bf_nonlinearity(f, n):
    import math
    fw = fwt(f)
    # find modulus of each element in Walsh transform
    for i in range(len(fw)):
        fw[i] = abs(fw[i])
    # nonlinearity from the Walsh transform
    x = ((2 ** (n - 1)) - (max(fw) / 2))
    # print"\tNL of function is",
    # print x
    return x

##############################################################################
# converts num to binary form (no of bits in binary representation = length)


def binary(num, length):
    binary_string_list = list(format(num, '0{}b'.format(length)))
    return [int(digit) for digit in binary_string_list]

##############################################################################
# returns array of NL of each component function for sbox S


def nonlinearity(S):
    import math
    order = len(S)
    n = int(math.log(order, 2))
    nl_array = []  # nl_array[] stores calculated NL for each function yi
    for bitno in range(n):
        f = []
        for index in range(order):  # for each element in Sbox
            binary_value = binary(S[index], n)
            bit = binary_value[bitno]
            f.append(bit)
        # print"***********************************************"
        # print "Funct no %d" % bitno,
        # print(f)
        bfnl = bf_nonlinearity(f, n)
        nl_array.append(bfnl)
    return nl_array


def value_nonl(S):
    """
    Returns nonlinearity for the sbox
    """
    nl_array = nonlinearity(S)
    return (nl_array)

print (value_nonl(S))

