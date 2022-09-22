import os
import shutil
from this import s

path = "E:\\OneDrive\\Desktop\\Python"

print("Before Copying: ")
print(os.listdir(path))

source = "E:\\OneDrive\\Desktop\\Python\\sample.txt"
destination = "E:\\OneDrive\\Desktop\\Python\\sample(copy).txt"

shutil.copy(source, destination)

print("After Copying: ")
print(os.listdir(path))