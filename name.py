import sys
if len(sys.argv)!=2:
print("usage: python name.py <name>")
sys.exit(1)
script_name = sys.argv[0]
name = sys.argv[1]
print("script name:",script_name)
print("student name:",name)
