import mxnet as mx

# Imperative

a = mx.nd.array([1])
b = mx.nd.array([2])
c = mx.nd.array([3])

d = (a + b) * c
print(d.asnumpy())
print(d.asscalar())

# Symbolic

a = mx.sym.Variable('a')
b = mx.sym.Variable('b')
c = mx.sym.Variable('c')

d = (a + b) * c

input_args = {
    'a': mx.nd.array([1]),
    'b': mx.nd.array([2]),
    'c': mx.nd.array([3])
}

executor = d.bind(ctx=mx.cpu(), args=input_args)
executor.forward()
print(executor.output[0].asnumpy())

#

grad_a = mx.nd.empty(1)
executor = d.bind(
    ctx=mx.cpu(),
    args=input_args,
    args_grad=('a': grad_a)
)
executor.backward(out_grads=mx.nd.ones(1))
print(grad_a.asscalar())
