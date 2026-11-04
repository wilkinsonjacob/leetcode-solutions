class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        str_sizes: list[int] = []
        result: list[str] = []

        for s in strs:
            str_sizes.append(len(s))

        for size in str_sizes:
            result.append(str(size))
            result.append(',')
        result.append('#')
        result.extend(strs)
        return ''.join(result)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        str_sizes: list[int] = []
        result: list[str] = []
        i: int = 0

        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            str_sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for size in str_sizes:
            result.append(s[i:i + size])
            i += size
        return result