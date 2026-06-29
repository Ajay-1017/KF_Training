import sys

sys.stderr.write("test\n")
sys.stderr.flush()
sys.stdout.write("hello\n")

if len(sys.argv)>1:
    print(sys.argv[1])
    print(int(sys.argv[1])+5)