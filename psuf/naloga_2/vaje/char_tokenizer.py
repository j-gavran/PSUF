class SimpleTokenizer:
    """Enostaven tokenizer za nize po znakih."""
    def __init__(self, chars: str) -> None:
        self._ch_to_int = {}
        self._int_to_ch = {}

        for i, ch in enumerate(chars):
            self._ch_to_int[ch] = i
            self._int_to_ch[i] = ch

        self.vocab_size = len(chars)

    def encode(self, s: str) -> list[int]:
        """Niz v seznam celih števil."""
        int_lst = []
        for ch in s:
            int_lst.append(self._ch_to_int[ch])
        return int_lst

    def __call__(self, s: str) -> list[str]:
        return self.encode(s)

    def decode(self, int_lst: list[int]) -> str:
        "Seznam celih števil v niz."
        str_lst = []
        for i in int_lst:
            str_lst.append(self._int_to_ch[i])
        return "".join(str_lst)
