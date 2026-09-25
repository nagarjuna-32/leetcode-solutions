class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        n = len(expression)

        def parse(i):
            # Parse a union: product (',' product)*
            res = set()
            cur, i = parse_product(i)
            res |= cur

            while i < n and expression[i] == ',':
                cur, i = parse_product(i + 1)
                res |= cur

            return res, i

        def parse_product(i):
            # Parse concatenation of factors
            res = {""}

            while i < n and expression[i] not in "},":
                if expression[i] == '{':
                    part, i = parse(i + 1)
                    i += 1  # skip '}'
                else:
                    part = {expression[i]}
                    i += 1

                # Cartesian product / concatenation
                res = {a + b for a in res for b in part}

            return res, i

        result, _ = parse(0)
        return sorted(result)
