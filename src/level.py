
def level(x):
    if x == 1:
        cannon = [[12,30], [12,50]]
        hut = [[16,40], [16,30],[16,50],[7,30],[7,50]]
        wizard = [[12,25], [7,40]]
        return [cannon,hut,wizard]
    elif x == 2:
        cannon = [[12,35], [12,50],[7,42]]
        hut = [[16,40], [16,30],[16,50],[7,30],[7,50]]
        wizard = [[12,30],[7,36],[16,36]]
        return [cannon,hut,wizard]
    else :
        cannon = [[12,35], [12,50],[7,42],[16,45]]
        hut = [[16,40], [16,30],[16,50],[7,30],[7,50]]
        wizard = [[12,30],[7,36],[16,36],[12,45]]
        return [cannon,hut,wizard]
