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

/home/d/Documents/caffe/build/tools/convert_imageset ./ train.txt train_lmdb -resize_width 224 -resize_height 224 --shuffle

/home/d/Documents/caffe/build/tools/convert_imageset ./ val.txt val_lmdb -resize_width 224 -resize_height 224 --shuffle

```

# Train

```bash

python /home/d/Documents/caffe/python/draw_net.py food_resnet_10_cvgj_finetune.prototxt train.png --rankdir BT

/home/d/Documents/caffe/build/tools/caffe train -solver solver.prototxt -weights resnet10_cvgj_iter_320000.caffemodel -log_dir ./

python /home/d/Documents/caffe/tools/extra/plot_training_log.py.example 2 tlft_test_loss_iters.png caffe.ubuntu.d.log
python /home/d/Documents/caffe/tools/extra/plot_training_log.py.example 0 tlft_test_accuracy_iters.png caffe.ubuntu.d.log
python /home/d/Documents/caffe/tools/extra/plot_training_log.py.example 6 tlft_train_loss_iters.png caffe.ubuntu.d.log

python recognize_food.py val.txt

sudo apt-get install python-sklearn
sudo pip install sklearn

python make_confusion_matrix.py

python kaoya_PR_curve.py

python kaoya_Receiver_Operating_Characteristic_curve.py

python visualize_activation.py val_visualize_activation.txt

```
