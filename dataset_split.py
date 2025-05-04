import os
import random
import shutil

# Copy function
def copy_data(img_src, lbl_src, img_list, img_dst, lbl_dst):
    for img in img_list:
        name = os.path.splitext(img)[0]
        shutil.copy(os.path.join(img_src, img), os.path.join(img_dst, img))
        shutil.copy(os.path.join(lbl_src, name + ".txt"), os.path.join(lbl_dst, name + ".txt"))


def split_dataset(img_src, lbl_src, img_train, img_val, lbl_train, lbl_val, train_ratio=0.8):

    for d in [img_train, img_val, lbl_train, lbl_val]:
        os.makedirs(d, exist_ok=True)

    # List all image files
    images = [f for f in os.listdir(img_src) if f.endswith(('.jpg'))]
    random.shuffle(images)

    # Split the dataset
    split_idx = int(train_ratio * len(images))
    train_imgs = images[:split_idx]
    val_imgs = images[split_idx:]

    # Copy to train and val folders
    copy_data(img_src, lbl_src, train_imgs, img_train, lbl_train)
    copy_data(img_src, lbl_src, val_imgs, img_val, lbl_val)

    print("Dataset split and copied successfully!")


if __name__ == "__main__":
    split_dataset(
        img_src="original_dataset/images",
        lbl_src="original_dataset/labels",
        img_train="dataset_after_splitting/images/train",
        img_val="dataset_after_splitting/images/val",
        lbl_train="dataset_after_splitting/labels/train",
        lbl_val="dataset_after_splitting/labels/val",
        train_ratio=0.8    # 80% train set 20% validation set
    )

    # create YAML file for the dataset 
    data_yaml = """
    path: C:/Users/rwkos/Desktop/asd/Smart_License_Detect/dataset_after_splitting
    train: images/train
    val: images/val
    nc: 1
    names: ['driving license']
    """

    with open("custom.yaml", "w") as f:
        f.write(data_yaml)