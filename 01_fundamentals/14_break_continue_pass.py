# ------------------------------------------------------------------------
# break, continue, pass
# ------------------------------------------------------------------------

for i in range(10):
    if i == 5:
        break
    print(i)

print('---')

for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

print('---')

for i in range(3):
    pass  # placeholder when a statement is required but you have nothing to run yet

print('done')
