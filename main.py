import config as cfg


def get_target_plane(size = '1/3'):
    '''
    根据靶面大小返回感光元件的宽和高

    :param size:
    :return:
    '''
    if size not in cfg.target_plane_size.keys():
        raise Exception('size should in {}'.format(cfg.target_plane_size.keys()))

    return cfg.target_plane_size[size]


def main(focus,distance,target_size='1/3',dpi=(1920,1080)):
    '''

    :param dpi: (1920,1080) w*h
    :param focus: 12(mm)
    :param distance: 5(m)
    :param target_size: '1/3'
    :return:
    '''

    # 拿到默认的人脸宽，高
    face_w,face_h = cfg.face_size
    print('default face size:,width {}m,height {}m'.format(face_w,face_h))

    # 拿到分辨率，宽*高
    dpi_w,dpi_h = dpi

    # 拿到感光元件的宽和高
    target_w,target_h = get_target_plane(target_size)

    # 根据小孔成像，利用焦距和物距来计算人脸的宽在图像上占几个像素
    pic_w = focus*face_w/(distance*target_w/dpi_w)

    # 根据小孔成像，利用焦距和物距来计算人脸的高在图像上占几个像素
    pic_h = focus*face_h/(distance*target_h/dpi_h)

    return pic_w,pic_h

if __name__ == '__main__':
    print(main(6,5,dpi=(1280,720)))
