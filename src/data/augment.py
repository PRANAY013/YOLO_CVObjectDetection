import os
import cv2
import numpy as np
from tqdm import tqdm

def augment_image(image):
    aug_imgs = []
    aug_imgs.append(cv2.flip(image, 1))  
    rows, cols = image.shape[:2]
    M = cv2.getRotationMatrix2D((cols/2, rows/2), 15, 1)
    aug_imgs.append(cv2.warpAffine(image, M, (cols, rows)))
    noise = np.random.normal(0, 10, image.shape).astype(np.uint8)
    aug_imgs.append(cv2.add(image, noise))
    return aug_imgs

def augment_dataset(input_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for fname in tqdm(os.listdir(input_dir)):
        if fname.endswith('.jpg') or fname.endswith('.png'):
            img_path = os.path.join(input_dir, fname)
            img = cv2.imread(img_path)
            aug_imgs = augment_image(img)
            for i, aug in enumerate(aug_imgs):
                out_name = fname.replace('.', f'_aug{i}.')
                cv2.imwrite(os.path.join(output_dir, out_name), aug)

if __name__ == "__main__":
    augment_dataset('data/raw', 'data/augmented')
