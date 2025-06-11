import matplotlib.pyplot as plt
import numpy as np

def show_segmentation(data, mask, index=None):
    if index is None:
        # Use center slice along each axis by default
        index = [
            data.shape[0] // 2,
            data.shape[1] // 2,
            data.shape[2] // 2
        ]

    # Prepare the slices for all three axes
    img_slices = [
        (data[index[0], :, :], mask[index[0], :, :], 'Axial (axis=0)'),
        (data[:, index[1], :], mask[:, index[1], :], 'Coronal (axis=1)'),
        (data[:, :, index[2]], mask[:, :, index[2]], 'Sagittal (axis=2)')
    ]

    fig, axes = plt.subplots(2, 3, figsize=(15, 10))

    for i, (img_slice, mask_slice, title) in enumerate(img_slices):
        # Normalize image slice
        img_norm = (img_slice - np.min(img_slice)) / (np.max(img_slice) - np.min(img_slice) + 1e-8)

        # Plot original image
        axes[0, i].imshow(img_norm.T, cmap='gray', origin='lower')
        axes[0, i].set_title(f"{title} - Image")
        axes[0, i].axis('off')

        # Plot segmentation mask
        axes[1, i].imshow(mask_slice.T, cmap='Reds', origin='lower')
        axes[1, i].set_title(f"{title} - Segmentation")
        axes[1, i].axis('off')

    plt.tight_layout()
    plt.show()
