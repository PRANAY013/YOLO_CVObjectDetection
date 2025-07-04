import os
import shutil
from sklearn.model_selection import train_test_split

def split_dataset(images_dir, labels_dir, output_dir, test_size=0.2, val_size=0.1):
    images = [f for f in os.listdir(images_dir) if f.endswith('.jpg') or f.endswith('.png')]
    train_imgs, test_imgs = train_test_split(images, test_size=test_size, random_state=42)
    train_imgs, val_imgs = train_test_split(train_imgs, test_size=val_size, random_state=42)

    splits = {'train': train_imgs, 'val': val_imgs, 'test': test_imgs}
    for split, imgs in splits.items():
        img_out = os.path.join(output_dir, split, 'images')
        lbl_out = os.path.join(output_dir, split, 'labels')
        os.makedirs(img_out, exist_ok=True)
        os.makedirs(lbl_out, exist_ok=True)
        for img in imgs:
            shutil.copy(os.path.join(images_dir, img), img_out)
            label = img.replace('.jpg', '.txt').replace('.png', '.txt')
            shutil.copy(os.path.join(labels_dir, label), lbl_out)
    print('Dataset split complete.')

if __name__ == "__main__":
    split_dataset('data/raw', 'data/annotated', 'data/augmented')
