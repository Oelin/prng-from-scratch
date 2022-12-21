from functools import reduce


MODULUS = int('1'*607, 2) # M607 - a large prime number.
GENERATOR = 7


def one_way_function(x): # The discrete logarithm problem.
        return pow(GENERATOR, x, MODULUS)


def hard_core_predicate(state, seed): # XOR-reduction on x * y.
        bits = (int(bit) for bit in '{:b}'.format(x * y))

        return reduce(lambda x, y: x ^ y, bits)
    

def prng(seed: int, state: int) -> int:

        while True:
                bit = hard_core_predicate(state, seed)
                yield bit


                # Shift next bit into state.

                state = one_way_function(int('{:b}{}'.format(state, bit), 2))
