class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs is None:
            return []
        full = " ".join(strs)
        
        return full


    def decode(self, s: str) -> List[str]:
        if s is None:
            return ""
        return s.split(" ")