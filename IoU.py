def area(box):
    """
    计算box的面积，box的坐标形式为xyxy
    """
    x1, y1, x2, y2 = box
    return (max(x1, x2)-min(x1, x2)) * (max(y1, y2)-min(y1, y2))


def IoU(box1, box2):
    """
    计算两个box的IoU,box的坐标形式为xyxy
    """
    s1 = area(box1)
    s2 = area(box2)
    x1, y1 = max(box1[0], box2[0]), max(box1[1], box2[1])
    x2, y2 = min(box1[2], box2[2]), min(box1[3], box2[3])
    intersection = max(x2-x1, 0) * max(y2-y1, 0)
    union = s1 + s2 -intersection
    return intersection / union


bbox1 = [100, 100, 200, 200]
bbox2 = [120, 120, 200, 200]
print(IoU(bbox1, bbox2))
