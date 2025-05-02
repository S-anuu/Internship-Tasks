import matplotlib.pyplot as plt

def show_segmentation_overlay(data, mask, index=None):
    if index is None:
        # Use center slice along each axis by default
        index = [data.shape[0] //2,
                 data.shape[1] // 2,
                 data.shape[2] // 2]

    # Prepare the slices for all three axes
    img_slices = [
        (data[index[0], :, :], mask[index[0], :, :], 'Axial (axis=0)'),
        (data[:, index[1], :], mask[:, index[1], :], 'Coronal (axis=1)'),
        (data[:, :, index[2]], mask[:, :, index[2]], 'Sagittal (axis=2)')
    ]

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    for i, (img_slice, mask_slice, title) in enumerate(img_slices):
        axes[i].imshow(img_slice.T, cmap='gray', origin='lower')
        axes[i].imshow(mask_slice.T, cmap='Reds', alpha=0.4, origin='lower')
        axes[i].set_title(f"{title} - Overlay")
        axes[i].axis('off')

    plt.tight_layout()
    plt.show()