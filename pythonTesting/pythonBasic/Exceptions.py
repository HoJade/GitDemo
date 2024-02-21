ItemsInCart = 0

if ItemsInCart != 2:
    # raise Exception("Product Cart Count NOT matching")
    pass                # pass --> placeholder for empty code, it will do nothing


# expect the condition should always be true
assert (ItemsInCart == 0)


# "try-except": the code execution won't stop if there's error/failure in "try" block
# use "try-except" block when there's a uncertainty situation
try:        # if "try" block doesn't fail, then won't execute "except" block
    with open("testing.txt", "r") as reader:
        print(reader.read())

except:     # when "try" block failed, then execute "except" block, and won't show error
    print("somehow i reached this block bcuz there's a failure in try block")


try:
    with open("testing.txt", "r") as reader:
        print(reader.read())

except Exception as e:     # show the actual error message Python has thrown
    print(e)

finally:                   # it will execute no matter there's a pass or failure in "try-except" block
    print("end")
