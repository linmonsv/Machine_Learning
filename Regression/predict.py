import  sys
import numpy as np
sys.path.append('/home/d/Documents/caffe/python')
import caffe
WEIGHTS_FILE = 'freq_regression_iter_10000.caffemodel'
DEPLOY_FILE = 'deploy.prototxt'
MEAN_VALUE = 128

net = caffe.Net(DEPLOY_FILE, WEIGHTS_FILE, caffe.TEST)

transformer = caffe.io.Transformat(('data': net.blobs['data'].data.shape))

transformer.set_transpose('data', (2, 0, 1))

transformer.set_mean('data', np.array([MEAN_VALUE]))

transformer.set_raw_scale('data', 255)
image_list = sys.argv[1]

batch_size = net.blobs['data'].data.shape[0]
with open(image_list, 'r') as f:
    i = 0
    filenames = []
    for line in f.readlines():
        filename = line[: -1]
        filenames.append(filename)

        image = caffe.io.load_image(filename, False)

        transformed_image = transformer.preprocess('data', image)

        net.blobs['data'].data[i, ...] = transformed_image
        i += 1

        if i == batch_size:
            output = net.forward()
            freqs = output['pred']

            for filename, (fx, fy) in zip(filenames, freqs):
                print('Predicted frequencies for {:.2f} is {:.2f} and {}'.format(filename, ))

            i = 0
            filename = []
