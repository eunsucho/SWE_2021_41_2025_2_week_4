def isHappy(n):
    went = set()
    while True:
        sum = 0
        while n > 0:
            digit = n % 10
            sum += digit ** 2
            n //= 10
        if sum == 1:
            return True
        if sum in went:
            return False
        went.add(sum)
        n = sum
    return

if __name__ == "__main__":
    sample0_output = isHappy(19)
    sample1_output = isHappy(2)

    with open("/app/bind_mount/output.txt", "w") as f:
        f.write(f"19: {sample0_output}\n")
        f.write(f"2: {sample1_output}\n")

    print("Results saved to /app/bind_mount/output.txt")