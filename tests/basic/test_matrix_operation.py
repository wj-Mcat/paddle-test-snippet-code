import paddle


def test_paddle_reshape():
    a = paddle.randn((2,3, 4))
    b = paddle.reshape_(a, (2,4, 3))

    assert id(b) == id(a)

    assert b.shape == [2, 4, 3]