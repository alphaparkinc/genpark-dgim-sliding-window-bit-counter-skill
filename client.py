class DGIMBucket:
    def __init__(self, size, timestamp):
        self.size = size
        self.timestamp = timestamp

class DGIMCounter:
    """DGIM streaming bit counter with logarithmic space."""
    def __init__(self, window_size):
        self.window_size = window_size
        self.buckets = []
        self.current_time = 0

    def update(self, bit):
        self.current_time += 1
        cutoff = self.current_time - self.window_size
        self.buckets = [b for b in self.buckets if b.timestamp > cutoff]

        if bit == 1:
            self.buckets.insert(0, DGIMBucket(1, self.current_time))
            self._compress()

    def _compress(self):
        idx = 0
        while idx < len(self.buckets) - 2:
            b1 = self.buckets[idx]
            b2 = self.buckets[idx + 1]
            b3 = self.buckets[idx + 2]
            if b1.size == b2.size == b3.size:
                new_bucket = DGIMBucket(b2.size * 2, b2.timestamp)
                self.buckets.pop(idx + 2)
                self.buckets.pop(idx + 1)
                self.buckets.insert(idx + 1, new_bucket)
            else:
                idx += 1

    def estimate_count(self, k):
        cutoff = self.current_time - k
        total = 0
        for b in self.buckets:
            if b.timestamp > cutoff:
                total += b.size
            else:
                total += b.size // 2
                break
        return total
