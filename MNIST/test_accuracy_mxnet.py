import mxnet as mx

test_dataiter = mx.io.ImageRecordIter(
    path_imgrec="test.rec",
    data_shape=(1, 28, 28),
    batch_size=100,
    mean_r=128,
    scale=0.00390625,
)

mod = mx.mod.Module.load('mnist_lenet', 35, context=mx.gpu(0))

mod.bind(
    data_shapes=test_dataiter.provide_data,
    label_shapes=test_dataiter.provide_label,
    for_training=False)

metric = mx.metric.create('acc')

mod.score(test_dataiter, metric)

for name, val in metric.get_name_value():
    print('{} = {:.2f}%'.format(name, val * 100))
