class Solution:
    def countBits(self, n: int) -> List[int]:
        counts = []

        # get counts
        for i in range(n+1):
            
            if i == 0:
                counts.append(i)
            elif i == 1:
                counts.append(i)
            else:
                size = i
                count = 0
                while size > 0:
                    if size & 1 == 1:
                        count += 1
                        size = size >> 1
                    else:
                        size = size >> 1
                counts.append(count)
        return counts




            
            



            
        