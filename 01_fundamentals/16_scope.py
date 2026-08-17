# ------------------------------------------------------------------------
# Scope
# ------------------------------------------------------------------------

works_at = 'Regnology'

def show_workplace():
    print(works_at)  # reads the global name

show_workplace()

def change_local():
    works_at = 'elsewhere'
    print(works_at)

change_local()
print(works_at)  # global value is unchanged

def change_global():
    global works_at
    works_at = 'elsewhere'

change_global()
print(works_at)
