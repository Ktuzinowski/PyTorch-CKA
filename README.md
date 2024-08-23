<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#environment-setup">Dependencies for Conda Environment</a>
    </li>
    <li>
      <a href="#checkpoints">Checkpoints</a>
    </li>
    <li>
      <a href="#cka">Centered Kernel Alignment (CKA)</a>
    </li>
  </ol>
</details>

<!-- Dependencies for Conda Environment -->
## Environment Setup

* Pytorch. Find command for your GPU at link [here.](https://pytorch.org/get-started/locally/)
  ```sh
  pip3 install torch torchvision
  ```
* Gdown
  ```sh
  pip3 install gdown
  ```
* Six
  ```
  pip3 install six
  ```
* Einops
  ```
  pip3 install einops
  ```

<!-- Checkpoints -->
## Checkpoints

1. Download checkpoints from Google Drive using **download_for_checkpoints.py**, downloads all zip files for CIFAR10 and CIFAR100 trained models.
  ```sh
  cd checkpoints
  python download_for_checkpoints.py
  ```
2. Unzip all checkpoint zip files using **unzip_checkpoints.py**, Unzips all checkpoints into corresponding folders. Feel free to delete zip files afterwards.
  ```sh
  python unzip_checkpoints.py
  ```

<!-- Centered Kernel Alignment (CKA) -->
## CKA

1. 





