import nibabel as nib
from load_nifti_image import load_nifti_image
# from show_slices import show_slices
# from show_segmentation_overlay import show_segmentation_overlay
# from show_segmentation import show_segmentation
from apply_threshold import apply_threshold

# Load the NIfTI images
nii_path_1 = '/home/anuuu/Documents/Internship/Tasks/threshold_segmentation/ankle_image.nii.gz'
img_1, img_data_1 = load_nifti_image(nii_path_1)

nii_path_2 = '/home/anuuu/Documents/Internship/Tasks/threshold_segmentation/ankle_image_2.nii.gz'
img_2, img_data_2 = load_nifti_image(nii_path_2)

# Thresholds
bone_thres = [500, 2100]
air_sac_thres = [-1000, -700]
fat_thres = [-100, -30]
hard_tissue_thres = [90, 300]
soft_tissue_thres = [30, 90]

thresholds = {'bone': bone_thres,
              'air_sac': air_sac_thres,
              'fat': fat_thres,
              'hard_tissue': hard_tissue_thres,
              'soft_tissue': soft_tissue_thres}

masks_1 = {}

# Apply thresholds in image_1
for name, thres in thresholds.items():
    mask = apply_threshold(img_data_1, lower_thres=thres[0], upper_thres=thres[1])
    masks_1[name] = mask

# Save Masks
for (name, mask) in masks_1.items():
    seg_img = nib.Nifti1Image(mask, affine=img_1.affine, header=img_1.header)
    postfix = '_segmentation_mask.nii.gz'
    print(f'Saving {name} mask....')
    nib.save(seg_img, name+postfix)

masks_2 = {}

# Apply thresholds in image_2
for name, thres in thresholds.items():
    mask = apply_threshold(img_data_2, lower_thres=thres[0], upper_thres=thres[1])
    masks_2[name] = mask

# Save Masks
for (name, mask) in masks_2.items():
    seg_img = nib.Nifti1Image(mask, affine=img_2.affine, header=img_2.header)
    postfix = '_segmentation_mask_2.nii.gz'
    print(f'Saving {name} mask....')
    nib.save(seg_img, name+postfix)

# sitk.GetArrayFromImage(image).max()
