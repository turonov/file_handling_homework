def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    b=[]
    for i in f:
        b.append(i)
    return b

# Read data from file
f = open("txt_file/data01.txt").read().split(",")
print(main(f))