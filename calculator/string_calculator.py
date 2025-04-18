class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0
        numbers = numbers.replace("\n", ",")
        parts = numbers.split(",")
        return sum(int(n) for n in parts)