import tensorflow as tf

from onnx_tf_prenatal.handlers.backend_handler import BackendHandler
from onnx_tf_prenatal.handlers.handler import onnx_op
from onnx_tf_prenatal.handlers.handler import tf_func


@onnx_op("Size")
@tf_func(tf.size)
class Size(BackendHandler):

  @classmethod
  def get_attrs_processor_param(cls):
    return {"default": {"out_type": tf.int64}}

  @classmethod
  def version_1(cls, node, **kwargs):
    return [cls.make_tensor_from_onnx_node(node, **kwargs)]

  @classmethod
  def version_13(cls, node, **kwargs):
    return [cls.make_tensor_from_onnx_node(node, **kwargs)]
