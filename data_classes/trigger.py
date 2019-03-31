import script1
import script2
import singleton

obj_main = singleton.OnlyOne('main')
print(obj_main)

script1.main()
script2.main()
