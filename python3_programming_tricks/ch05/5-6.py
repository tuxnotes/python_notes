from tempfile import TemporaryFile, NamedTemporaryFile

# 通常来讲，临时文件都是二进制文件

tf = TemporaryFile() # 是一个操作系统级别的临时文件，支持系统调用

tf.write(b'*' * 1024 * 1024)
tf.seek()
tf.read(512)

# 此临时文件在文件系统找不到，但是创建是可以指定目录

tf.close() # 此临时文件自动删除

# 2 NamedTemporaryFile 这不是操作系统级别的临时文件，是python库完成的

ntf = NamedTemporaryFile()
ntf.name
tempfile.gettempdir()
tempfile.gettempprefix()
ntf.close()

ntf2 = NamedTemporaryFile(delete=False)


