import numpy as np
import matplotlib.pyplot as pt 

#---------------------- histograph----------------------
random_number = np.random.randn(1000)
pt.hist(random_number,bins=30,color='yellow' )
pt.show()