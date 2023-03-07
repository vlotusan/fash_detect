import os
import fiftyone as fo



direct = r'deepfashion2.json'
direct_abs = os.path.abspath(direct)
# print(direct_abs)

coco_dataset = fo.Dataset.from_dir(
    dataset_type = fo.types.COCODetectionDataset,
    data_path = r'D:\TA\fashion\validation\image',
    labels_path = direct_abs,
    include_id=True
)

session = fo.launch_app(coco_dataset)