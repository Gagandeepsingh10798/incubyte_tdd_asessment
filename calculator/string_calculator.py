import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiters = [","]
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)
            if delimiter_line.startswith("//["):
                delimiters = re.findall(r"\[(.*?)\]", delimiter_line)
            else:
                delimiters = [delimiter_line[2:]]

        for delim in delimiters:
            numbers = numbers.replace(delim, ",")

        numbers = numbers.replace("\n", ",")
        parts = numbers.split(",")

        nums = []
        for n in parts:
            if not n:
                continue
            num = int(n)
            if num < 0:
                nums.append(num)
            elif num <= 1000:
                nums.append(num)

        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

        return sum(n for n in nums if n >= 0)