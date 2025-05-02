import nibabel as nib

def load_nifti_image(nii_path):
    
    img = nib.load(nii_path)
    img_data = img.get_fdata()

    return img, img_data