def medianFilter(img, k):
    rows, cols = img.shape
    result = np.zeros((rows, cols), np.float32)
    edge = (k-1)//2
    for i in range(edge, rows-edge):
        for j in range(edge, cols-edge):
        	#obtendo a mediana dos valores dos pixels correspondentes ao frame
            tempV = []
            for x in range(k):
                for y in range(k):
                    tempV.append(img[i+x-edge, j+y-edge])
            tempV.sort()
            result[i,j] = tempV[len(tempV)//2]   
    return result
