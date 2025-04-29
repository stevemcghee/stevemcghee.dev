def b(x,y):
   return [(a, b) for a in x for b in y if a < b]

def test_b(x, y):
    out = b([77], [1,2])
    assert out == [(1,77), (2, 77)]

    out = b([1,2,3,4,5], [77,67,57,47,37,27])
    assert out == [1]

    print ("ok")
