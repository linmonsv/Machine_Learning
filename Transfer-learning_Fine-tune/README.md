# Collect Data

```bash

python collect_data.py

python remove_invalid_images.py ./

sudo apt-get install fdupes

fdupes -rdN ./

sudo apt-get install findimagedupes

mkdir train
mv 00? train

python downscale.py train 256

findimagedupes -R train > dup_list

python remove_dups_from_list.py dup_list

python gen_val.py

python gen_aug.py

python gen_label_list.py train
python gen_label_list.py val

/home/d/Documents/caffe/build/tools/conver_imageset ./ train.txt train_lmdb -resize_width 224 -resize_height 224 --shuffle

/home/d/Documents/caffe/build/tools/conver_imageset ./ val.txt val_lmdb -resize_width 224 -resize_height 224 --shuffle

```
