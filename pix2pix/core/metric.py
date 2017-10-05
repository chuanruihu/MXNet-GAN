import mxnet as mx
import numpy as np

class AccMetric(mx.metric.EvalMetric):
    def __init__(self):
        super(AccMetric, self).__init__('Accuracy')

    def update(self, labels, preds):
        pred = preds[0].asnumpy().ravel()
        label = labels[0].asnumpy().ravel()

        self.sum_metric += np.sum((pred > 0.5) == label)
        self.num_inst += len(pred)

class CrossEntropyMetric(mx.metric.EvalMetric):
    def __init__(self):
        super(CrossEntropyMetric, self).__init__('CrossEntropy')

    def update(self, labels, preds):
        pred = preds[0].asnumpy().ravel()
        label = labels[0].asnumpy().ravel()

        ce = -(label * np.log(pred + 1e-12) + (1. - label) * np.log(1. - pred + 1e-12))

        self.sum_metric += np.sum(ce)
        self.num_inst += len(pred)

class L1LossMetric(mx.metric.EvalMetric):
    def __init__(self):
        super(L1LossMetric, self).__init__('L1Loss')

    def update(self, labels, preds):
        l1loss = preds[0].asnumpy()

        self.sum_metric += np.sum(l1loss)
        self.num_inst += l1loss.shape[0]