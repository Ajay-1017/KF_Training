import sys
import math
import practice

# 1) version of compelte python Version
print(sys.version)  

# 2) version as tuple-like object
print(sys.version_info)

print(sys.version_info.major)
print(sys.version_info.minor)

if sys.version_info >=(3,10):
    print("python version supported")
else:
    print("python upgrade")

# 3) shows the operating system
print(sys.platform)

# 4) shows where the python is installed
print(sys.executable)

# 5) Python needs to know where to search for modules.
print(sys.path)

# 6) Standard output stream.
sys.stderr.write("Hello")
sys.stdout.write("World")

# 7) Dictionary of already imported modules.
print(sys.modules)

if len(sys.argv)>1:
    print(sys.argv[1])
    print(int(sys.argv[1])+5)