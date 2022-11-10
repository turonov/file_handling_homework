def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    a=[]
    for i in f:
        a.append(len(i))
    return a
            
    
# Read data from file
f = open("txt_file/data06.txt").read().split("\n")
print(main(f))