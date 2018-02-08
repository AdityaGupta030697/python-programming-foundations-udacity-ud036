import os

def renamefiles():

    # 1 get file names from aa folder
    file_list = os.listdir(r"C:\Users\aditya\Desktop\Apps\py\udacitypy\prank")
    
    # to get current working directory
    saved_path = os.getcwd()
    
    # to change the present directory
    os.chdir(r"C:\Users\aditya\Desktop\Apps\py\udacitypy\prank")
    
    # 2 to renaming a file
    """
    str.maketrans() is being called with three arguments, both first and second arguments are empty strings ('' or "") and the third argument
    is a string whose characters will be removed from the resulting string.

    """
    
    for file_name in file_list:
        # here translate function removes all instances of chars/digits in right

        map = str.maketrans('', '', '0123456789')
        os.rename(file_name, file_name.translate(map))
        
        
    # restoring changes to directory
    os.chdir(saved_path)
    
    
renamefiles()   
