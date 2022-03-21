import datetime
import platform
import sys

print("Platform.system : %s"%(platform.system()))
print("Platform.release: %s"%(platform.release()))

try:
    print(f"Hello from an F-String at {datetime.datetime.now().isoformat()}")
except Exception as e:
    print("There was an error using F-Strings, they are not supported in Python2.7.")
    sys.exit(1)

sys.exit(0)
