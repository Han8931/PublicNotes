def test(i):
    if i<3:
        print(f"{i}")
        test(i+1)
        print(f"Done: {i}") 

test(0)
