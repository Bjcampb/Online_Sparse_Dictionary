import numpy as np
import nibabel as nib

#---------------------
# Load mapped atoms
#---------------------
data = np.load('../Data/alpha_map_300_atoms.npy')
print(np.shape(data))

#-----------------------
# Loop through and save
#-----------------------
for i in range(np.shape(data)[3]):
	array_data = data[:,:,:,i]
	affine = np.diag([1,2,3,1])
	array_img = nib.Nifti1Image(array_data, affine)
	nib.save(array_img, 'atom_%d.nii' % (i+1))





