def main(data:str) -> list():
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    return data

# Read data from file
f = open("txt_file/data01.txt").read()
a=f.split(",")
b = [a]
print(main(a))