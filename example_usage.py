from client import DGIMCounter

def main():
    print("=== Testing DGIM Sliding Window Bit Counter ===")
    dgim = DGIMCounter(window_size=50)
    bits = [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1]
    for b in bits:
        dgim.update(b)

    est = dgim.estimate_count(10)
    print("Estimated count in last 10 elements:", est)
    assert est >= 4
    print("DGIM Counter verified successfully!")

if __name__ == '__main__':
    main()
