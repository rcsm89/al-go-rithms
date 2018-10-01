def gaussian(img):
    kernel = np.matrix('1 2 1; 2 4 2; 1 2 1')/16
    k = kernel.shape[0]
    rows, cols = img.shape
    result = np.zeros((rows, cols), np.float32)
    edge = (k-1)//2
    for i in range(edge, rows-edge):
        for j in range(edge, cols-edge):
            for x in range(k):
                for y in range(k):
                    result[i,j]+=img[i+x-edge, j+y-edge]*kernel[x,y]
    return result
