# MNIST

```bash
wget http://deeplearning.net/data/mnist/mnist.pkl.gz

python gen_caffe_imglist.py mnist/train train.txt

python gen_caffe_imglist.py mnist/val val.txt

python gen_caffe_imglist.py mnist/test test.txt

/home/d/Documents/caffe/build/tools/convert_imageset ./ train.txt train_lmdb --gray --shuffle

/home/d/Documents/caffe/build/tools/convert_imageset ./ val.txt val_lmdb --gray --shuffle

/home/d/Documents/caffe/build/tools/convert_imageset ./ test.txt test_lmdb --gray --shuffle

/home/d/Documents/caffe/build/tools/caffe train -solver lenet_solver.prototxt -log_dir ./

```
