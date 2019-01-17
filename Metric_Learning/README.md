# Metric Learning

```bash

python gen_pairwise_imglist.py

/home/water/caffe/build/tools/convert_imageset ./ train.txt train_lmdb --gray
/home/water/caffe/build/tools/convert_imageset ./ train_p.txt train_p_lmdb --gray
/home/water/caffe/build/tools/convert_imageset ./ val.txt val_lmdb --gray
/home/water/caffe/build/tools/convert_imageset ./ val_p.txt val_p_lmdb --gray

python /home/water/caffe/python/draw_net.py mnist_siamese_train_test.prototxt mnist_siamese_train_test.png --rankdir BT

```
