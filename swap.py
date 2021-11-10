def swap_case(s):
    return s.swapcase()
def reverse(s):
    return s[::-1]
if __name__ == "__main__":
    s=input()
    result = swap_case(s)
    reve = reverse(result)
    print(result)
    print(reve)


