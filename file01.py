def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    b=[]
    for i in a:
        b.append(int(i))
    return data

# Read data from file
f = open("txt_file/data01.txt").read()
a=f.split(",")
print(main(a))