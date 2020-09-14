import numpy as np
import scipy.io as scio

person_color = np.asarray([[0, 0, 0], [250, 0, 0]], dtype=np.uint8)

scio.savemat("./data/Person/person_color.mat", {'colors': person_color})
