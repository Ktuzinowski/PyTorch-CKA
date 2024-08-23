import gdown, sys

checkpoint_urls = ['https://drive.google.com/file/d/1g2FxUg1iK6oyCMSjQLIUnnsVtPYsV_K3/view?usp=sharing', 'https://drive.google.com/file/d/1v2ZielJCr1Bq7iAe6_nfbSpYZWmsrlsY/view?usp=sharing', 'https://drive.google.com/file/d/1ANuo4nwGBPSdR4KmjCfPtdP_h_l9R4ZX/view?usp=sharing', 'https://drive.google.com/file/d/1d6gggBTl-6W2DcrJI4CmQRR9RVYdzFNd/view?usp=sharing']

prefix = 'https://drive.google.com/uc?/export=download&id='

for checkpoint_url in checkpoint_urls:
    file_id = checkpoint_url.split('/')[-2]
    gdown.download(prefix+file_id)