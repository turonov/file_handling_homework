def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a = 0
    for i in f:
        if i.isdigit():
            if a<int(i):
                a=int(i)
    return a
# Read data from file
f = open("txt_file/data08.txt").read()
print(main(f))