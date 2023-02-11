"""
module
@project_python
ⒸCopyright cone
"""
#1
"""
import matematika as tk

# sintaks
    # module_name.function_name 


# basic
tk.greating("hola")

a = tk.person1["age"]
print(a)


# mengganti nama module
    #  import matematika as tk


"""
#2

"""
import platform
import matematika as tk

x = platform.python_branch()
print(x) 



# dir()
x = dir(platform)
print(x)
"""

#3

from matematika import person1


a = person1["age"]
print(a)
print(person1["country"])


"""
note:
   Saat mengimpor menggunakan from kata kunci,
   jangan gunakan nama modul saat merujuk ke elemen dalam modul.
   Contoh: person1["age"], tidak mymodule.person1["age"]
"""
