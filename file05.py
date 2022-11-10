def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a = []
    for i in f:
        if i.isdigit():
            a.append(i)
    return a
    
# Read data from file
f=open("txt_file/data05.txt").read().split("\n")
print(main(f))