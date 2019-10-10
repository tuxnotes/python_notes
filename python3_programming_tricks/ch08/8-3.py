import tarfile
import os

def tar_xml(tfname):
    tf = tarfile.open(tfname, 'w:gz') # 以写的方式打开，压缩算法是gz
    for fname in os.listdir('.'):
        if fname.endswith('.xml'):
            tf.add(fname)
            os.remove(fname)
    tf.close()

    if not tf.members:
        os.remove(tfname)

tar_xml('test.tgz')
