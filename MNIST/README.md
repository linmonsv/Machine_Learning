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

python /home/d/Documents/caffe/tools/extra/plot_training_log.py.example 0 accuracy_iters.png caffe.ubuntu.d.log

python /home/d/Documents/caffe/tools/extra/plot_training_log.py.example 2 loss_iters.png caffe.ubuntu.d.log

python /home/d/Documents/caffe/python/draw_net.py lenet_train_val.prototxt mlp_train.png --rankdir BT

/home/d/Documents/caffe/build/tools/caffe test -model lenet_test.prototxt -weights mnist_lenet_iter_36000.caffemodel -iterations 100

/home/d/Documents/caffe/build/tools/caffe time -model lenet.prototxt

python recognize_digit.py test.txt

python run_augmentation.py mnist/train/ mnist/augmented 250000 --rotate_angle_vari=15 --p_mirror=0 --p_hsv=0 --p_gamma=0

python gen_caffe_imglist.py mnist/augmented augmented.txt

cat train.txt augmented.txt > train_aug.txt

/home/d/Documents/caffe/build/tools/convert_imageset ./ train_aug.txt train_aug_lmdb --resize_width=28 --resize_height=28 --gray --shuffle

/home/d/Documents/caffe/build/tools/caffe train -solver lenet_solver_aug.prototxt -log_dir ./

python /home/d/Documents/caffe/tools/extra/plot_training_log.py.example 0 accuracy_iters_aug.png mnist_train.log mnist_train_with_augmentation.log

python /home/d/Documents/caffe/tools/extra/plot_training_log.py.example 2 loss_iters_aug.png mnist_train.log mnist_train_with_augmentation.log

/home/d/Documents/caffe/build/tools/caffe train -solver lenet_solver_aug.prototxt -snapshot mnist_aug_lenet_iter_36000.solverstate -log_dir ./

```

```bash

python gen_mxnet_imglist.py mnist/train train.lst

python gen_mxnet_imglist.py mnist/val val.lst

python gen_mxnet_imglist.py mnist/test test.lst

/home/d/mxnet/bin/im2rec train.lst ./ train.rec color=0

/home/d/mxnet/bin/im2rec val.lst ./ val.rec color=0

/home/d/mxnet/bin/im2rec test.lst ./ test.rec color=0

python train_lenet5.py

python /home/d/mxnet/example/kaggle-ndsb1/training_curves.py --log-file=train_mnist_lenet.log

python test_time_mxnet.py 


```
