def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
              if(len(a[0])!=len(b)):
                return -1

              mat1=[]
              for i in range(len(a)):
                mat2=[]
                for j in range(len(b[0])):
                    val=0
                    for k in range(len(b)):
                        val+=a[i][k]*b[k][j]
                    mat2.append(val)
                mat1.append(mat2)
              return mat1