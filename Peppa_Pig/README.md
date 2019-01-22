# Peppa_Pig

```bash

mkdir VOC2018
...
...

python voc_label.py

./darknet detector train cfg/peppa.data cfg/yolov3-voc-peppa.cfg darknet53.conv.74

./darknet detector test cfg/peppa.data cfg/yolov3-voc-peppa-test.cfg backup/yolov3-voc-peppa_final.weights ~/Machine_Learning/Peppa_Pig/000000.jpg

```

## Reference

	@article{yolov3,
		title={YOLOv3: An Incremental Improvement},
		author={Redmon, Joseph and Farhadi, Ali},
		journal = {arXiv},
		year={2018}
	}
