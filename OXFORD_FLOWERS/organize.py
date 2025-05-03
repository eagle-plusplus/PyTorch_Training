import os
import shutil
import scipy.io
# from tqdm.auto import tqdm
from PIL import Image

# Paths
base_dir = ".\OXFORD_FLOWERS\oxfordflowers102"
img_dir = os.path.join(base_dir, "jpg")
label_mat = scipy.io.loadmat(os.path.join(base_dir, "imagelabels.mat")) 
setid_mat = scipy.io.loadmat(os.path.join(base_dir, "setid.mat"))

# Labels (1-based to 0-based)
labels = label_mat["labels"][0] - 1

# Splits (1-based to 0-based)
train_ids = setid_mat["trnid"][0] - 1
val_ids   = setid_mat["valid"][0] - 1
test_ids  = setid_mat["tstid"][0] - 1

# Output structure
output_root = os.path.join(base_dir, "split")
splits = {"train": train_ids, "val": val_ids, "test": test_ids}

for split, indices in splits.items():
    for i in indices:
        label = labels[i]
        img_filename = f"image_{i+1:05d}.jpg"
        img_path = os.path.join(img_dir, img_filename)

        class_dir = os.path.join(output_root, split, str(label))
        os.makedirs(class_dir, exist_ok=True)

        shutil.copy(img_path, os.path.join(class_dir, img_filename))