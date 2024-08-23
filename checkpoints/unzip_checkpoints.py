import os
import zipfile

def unzip_folder(zip_path, output_folder):
    # Open the zip file in read mode
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        # Extract all the contents into the specified output folder
        zip_ref.extractall(output_folder)

if __name__ == "__main__":
    zip_paths = ["checkpoints_cifar10.zip", "checkpoints_cifar100.zip", "checkpoints_cifar10_pretrained_imagenet.zip", "checkpoints_cifar100_pretrained_imagenet.zip"]
    output_folders = ["checkpoints_cifar10", "checkpoints_cifar100", "checkpoints_cifar10_pretrained_imagenet", "checkpoints_cifar100_pretrained_imagenet"]

    for zip_path, output_folder in zip(zip_paths, output_folders):
        # Create the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)
        
        unzip_folder(zip_path, output_folder)
        print(f"All files from '{zip_path}' have been unzipped into '{output_folder}'")
