from pixellib.instance import instance_segmentation

def objectt_detection_image():
    segment_image= instance_segmentation( )
    segment_image.load_model("mask_rcnn_coco.h5")

    segment_image.segmentImage(
        image_path="caption.jpg",
        output_image_name="output.jpg"
    )
    
def main():
    objectt_detection_image()
    
    
if __name__ == "__main__":
    main()