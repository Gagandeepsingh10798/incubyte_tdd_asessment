class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)
            delimiter = delimiter_line[2:]

        numbers = numbers.replace("\n", delimiter)
        parts = numbers.split(delimiter)
        nums = [int(n) for n in parts if n]

        negatives = [n for n in nums if n < 0]
        if negatives:
            raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")
        
        return sum(nums)