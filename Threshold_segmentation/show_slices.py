import matplotlib.pyplot as plt

def show_slices(data, index=None):
    if index is None:
        # Use center slice along each axis by default
        index = (data.shape[0] // 2,
                 data.shape[1] // 2,
                 data.shape[2] // 2)

    # Prepare the slices for all thress axis
    slices = [(data[index[0], :, :], 'Axial(axis=0)'),
              (data[:, index[1], :], 'Coronal(axis=1)'),
              (data[:, :, index[2]], 'Sagittal(axis=2)')]

    # Create a figure with 3 subplots
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    for ax, (slice_, title) in zip(axes, slices):
        ax.imshow(slice_.T, cmap='gray', origin='lower')
        ax.set_title(title)
        ax.axis('off')

    plt.tight_layout()
    plt.show()