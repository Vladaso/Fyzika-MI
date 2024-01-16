def calcMagSila(i, x1, y1, x2, y2, bx, by):
    #vektor usecky mag ciar
    l = [x2-x1,y2-y1,0]
    #vektor magnet indukcie
    b = [bx,by,0]
    
    # https://en.wikipedia.org/wiki/Cross_product#Computing
    # https://www.khanacademy.org/math/precalculus/x9e81a4f98389efdf:matrices/x9e81a4f98389efdf:multiplying-matrices-by-scalars/a/multiplying-matrices-by-scalars
    
    f = [i*(l[1]*b[2]-l[2]*b[1]), # x zlozka
         i*(l[2]*b[0]-l[0]*b[2]), # y zlozka
         i*(l[0]*b[1]-l[1]*b[0])] # z zlozka
    
    return f
    
    
    