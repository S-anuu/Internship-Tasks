### A program that automatically detects and segments bones in 3D medical images (usually in NIfTI or DICOM format).

# Install requirements from terminal
# pip install -r requirements.txt

import nibabel as nib
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Load the NIfTI image
nii_path = '/home/anuuu/Documents/Internship/Tasks/bone_segmentation/ankle_image.nii.gz'
img = nib.load(nii_path)
img_data = img.get_fdata()

print(f'Image Shape: {img_data.shape}')
print(f'Data type: {img_data.dtype}')

# Visualize middle slices
def show_slice(data, axis=0, index=None):
    if index is None:
        index = data.shape[axis] // 2

    if axis == 0:
        slice_ = data[index, :, :]
    elif axis == 1:
        slice_ = data[:, index, :]
    else:
        slice_ = data[:, :, index]

    plt.imshow(slice_.T, cmap='gray', origin='lower')
    plt.title(f'Slice {index} on axis {axis}')
    plt.axis('off')
    plt.show()

#show_slice(img_data, axis=0)

# Apply Threshold for Bone Segmentation

# Set thresholds
lower_thres = 565
upper_thres = 1500

# Apply thresholding
bone_mask = np.logical_and(img_data >= lower_thres, img_data <=upper_thres).astype(np.uint8)

print(f'Number of bone voxels: {np.sum(bone_mask)}')

# Visualize the segmentation mask
def show_segmentation(data, mask, axis=2, index=None):
    if index is None:
        index = data.shape[axis] //2

    if axis == 0:
        img_slice = data[index, :, :]
        mask_slice = mask[index, :, :]
    elif axis == 1:
        img_slice = data[:, index, :]
        mask_slice = mask[:, index, :]
    else:
        img_slice = data[:, :, index]
        mask_slice = mask[:, :, index]
    
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img_slice.T, cmap='gray', origin='lower')
    plt.title('Original Slice')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(img_slice.T, cmap='gray', origin='lower')
    plt.title('Bone Segmentation')
    plt.axis('off')
    plt.show()

# show_segmentation(img_data, bone_mask, axis=2)

# Save the mask with the same affine and header
seg_img = nib.Nifti1Image(bone_mask, affine=img.affine, header=img.header)
nib.save(seg_img, 'bone_segmentation_mask.nii.gz')