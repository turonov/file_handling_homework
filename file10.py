def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = []
    for i in f:
        a.append(len(i))
    return max(a)
# Read data from file
f = open("txt_file/data10.txt").read().split("\n")
print(main(f))