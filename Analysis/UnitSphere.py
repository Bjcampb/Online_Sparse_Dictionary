import numpy as np
import nibabel as nib
from sklearn.preprocessing import normalize

def unitsphere(file):
	points = [[244,168,253],
		  [280,192,243],
		  [316,184,266]]

	data = np.nib('file').get_data()
	x,y,z = data.nonzero()
	intensity = np.zeros((len(x))
	vectors = np.zeros((len(x),len(y),len(z),3)
	
	for j in range(3):
		for i in range(len(x)):
			intensity[i] = data[x[i],y[i],z[i]]
			vectors[i,i,i] = [x[i]-points[j][0],
				          y[i]-points[j][1],
					  z[i]=points[j][2]]
		vectors = normalize(vectors[:,:,:,j])
	return intensity, vectors
			
