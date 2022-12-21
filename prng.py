from functools import reduce


MODULUS = int('1'*607, 2) # M607 - a large prime number.
GENERATOR = 7


def one_way_function(x: int) -> int:
        return pow(GENERATOR, x, MODULUS)


def hard_core_predicate(state: int, seed: int) -> int:
        
        bits = (int(bit) for bit in '{:b}'.format(state * seed))
        return reduce(lambda x, y: x ^ y, bits)


def prng(seed: int, state: int) -> int:

        while True:
                bit = hard_core_predicate(state, seed)
                yield bit


                # Shift next bit into state.

                state = one_way_function(int('{:b}{}'.format(state, bit), 2))
