import numpy as np

# 绘制矩形框
boxes = np.array([[100, 100, 210, 210, 0.72],
                  [250, 250, 420, 420, 0.8],
                  [220, 220, 320, 330, 0.92],
                  [100, 100, 210, 210, 0.72],
                  [230, 240, 325, 330, 0.81],
                  [220, 230, 315, 340, 0.9]])


# 设置形参,dets为绘制的矩形框，thresh为置信度
def py_cpu_nms(dets, thresh):
    # 分别为各个矩形框两个点的坐标值
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]
    # 计算各个矩形框的面积
    areas = (y2 - y1) * (x2 - x1)
    # 每个矩形框的置信度
    scores = dets[:, 4]
    # 用来保存最后留下来的矩形框
    keep = []
    # argsort()用法，表示对数据进行从小到大进行排序，返回数据的索引值
    # argsort()[::-1]对置信度进行从大到小排序，返回索引值
    index = scores.argsort()[::-1]
    while index.size > 0:
        # 置信度最高的矩形框的索引
        i = index[0]
        # 将本次置信度最高的矩形框的索引添加到keep列表中
        keep.append(i)

        # 当前矩形框和剩下矩形框之间的交叉区域
        # 求交集的两个点的坐标值
        x11 = np.maximum(x1[i], x1[index[1:]])  # 交叉区域左上角的横坐标
        y11 = np.maximum(y1[i], y1[index[1:]])  # 交叉区域左上角的纵坐标
        x22 = np.minimum(x2[i], x2[index[1:]])  # 交叉区域右上角的横坐标
        y22 = np.minimum(y2[i], y2[index[1:]])  # 交叉区域右上角的纵坐标

        # 考虑不相交的情况，取最大值
        w = np.maximum(0, x22 - x11)  # the weights of overlap
        h = np.maximum(0, y22 - y11)  # the height of overlap

        # 计算交集
        overlaps = w * h
        # 计算IoU,index[1:]表示从第一个框到最后
        # IoU = 交叉区域面积/(矩形框面积 + 另一个矩形框面积 - 交叉区域面积)
        ious = overlaps / (areas[i] + areas[index[1:]] - overlaps)

        # 保留IoU值比较小的矩形框，因为有可能检测到的不是同一个物体
        idx = np.where(ious <= thresh)[0]
        print(idx)
        #
        index = index[idx + 1]

    return keep


import matplotlib.pyplot as plt


def plot_bbox(dets, c='k'):
    x1 = dets[:, 0]
    y1 = dets[:, 1]
    x2 = dets[:, 2]
    y2 = dets[:, 3]

    plt.plot([x1, x2], [y1, y1], c)
    plt.plot([x1, x1], [y1, y2], c)
    plt.plot([x1, x2], [y2, y2], c)
    plt.plot([x2, x2], [y1, y2], c)
    plt.title("nms")


plt.figure(1)
ax1 = plt.subplot(1, 2, 1)
ax2 = plt.subplot(1, 2, 2)

plt.sca(ax1)
plot_bbox(boxes, 'k')  # before nms

keep = py_cpu_nms(boxes, thresh=0.7)
plt.sca(ax2)
plot_bbox(boxes[keep], 'r')  # after nms
plt.show()
