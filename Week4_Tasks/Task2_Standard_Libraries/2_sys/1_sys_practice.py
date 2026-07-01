import sys

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


sys.stderr.write("test\n")
sys.stderr.flush()
sys.stdout.write("hello\n")

if len(sys.argv)>1:
    print(sys.argv[1])
    print(int(sys.argv[1])+5)