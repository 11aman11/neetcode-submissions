class Solution:

    def encode(self, strs: List[str]) -> str:
        full = " ".join(strs)
        
        return full


    def decode(self, s: str) -> List[str]:
        return s.split(" ")