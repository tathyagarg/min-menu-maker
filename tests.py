import bullets

rad = iter(bullets.Radix('turtle'))

for i in range(11196): # Prints turtle at this weird index!
    print(next(rad))
