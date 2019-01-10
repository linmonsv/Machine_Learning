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

```


