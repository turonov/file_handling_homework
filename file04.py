def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    for i in data:
        if i.isalpha():
            a.append('\n')
    return i
    
# Read data from file
f=open("txt_file/data04.txt").read()
print(main(f))
