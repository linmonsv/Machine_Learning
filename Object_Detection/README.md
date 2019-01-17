# Object Detection

```bash

cd /home/water/mxnet/example/ssd

wget https://github.com/zhreshold/mxnet-ssd/releases/download/v0.6/resnet50_ssd_512_voc0712_trainval.zi

unzip resnet50_ssd_512_voc0712_trainval.zip

python data/demo/download_demo_images.py

python demo.py --gpu 0

python demo.py --epoch 0 --images ./data/demo/dog.jpg --thresh 0.5

python demo.py --cpu --network resnet50 --data-shape 512

python demo.py --images ./data/demo/person.jpg --thresh 0.3

```
