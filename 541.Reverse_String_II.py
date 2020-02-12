class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chunks = []
        for i in range(len(s)//k + 1):
            chunk = s[k*i: k*i+k]
            if not i % 2:
                chunks.append(chunk[::-1])
            else:
                chunks.append(chunk)
        return ''.join(chunks)
                