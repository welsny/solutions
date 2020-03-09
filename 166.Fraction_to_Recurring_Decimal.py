class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        whole = str(abs(numerator) // abs(denominator))
        if numerator and (numerator < 0) != (denominator < 0):
            whole = '-' + whole
        rem = abs(numerator) % abs(denominator)

        denominator = abs(denominator)

        seen = {}
        frac = '.'
        rem *= 10
        while rem:
            if rem in seen:
                i = seen[rem]
                frac = frac[:i] + '(' + frac[i:] + ')'
                break
            else:
                seen[rem] = len(frac)

            frac += str(rem // denominator)
            rem %= denominator
            rem *= 10

        return whole + frac if len(frac) > 1 else whole
