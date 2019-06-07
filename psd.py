# -*- coding: UTF-8 -*- 

from psd_tools2 import PSDImage
from builtins import enumerate
import requests
class PSD2LayImage:
    
    psd = None;
    
    def __init__(self):
        
        #获取文件
        self.psd = PSDImage.open('my_image.psd');

        #保存图片
        self.psd.compose().save('images/main.png')
        
    def do(self):
        
        imageData = [];
        psdArr = self.psd[1];
        
        for index, layer in enumerate(psdArr):
            #获取坐标
            bbox = layer.bbox;
            
            #如果坐标小于0,暂时先过滤掉，尽量过滤些超出画布范围的一些图层
            if bbox[0] < 0:
                continue;
            
            #先放在这里，试验了番还不确定这是干什么用的
            if layer.has_vector_mask() :
                continue;
            
            if layer.has_pixels():
                layer_image = layer.topil();
                layer_image_path = "images/img_" + str(index) + ".png";
                layer_image.save(layer_image_path);
                layerInfo = {"type": "image", "name":index, "url":layer_image_path, "bbox":list(bbox)};
                imageData.append(layerInfo);
                
            #如果是文本
            if layer.kind == 'type':
                textVal = " ".join(layer.text.split());
                styleRun = layer.engine_dict['StyleRun'];
                runStyle = styleRun["RunArray"][0];
                StyleSheetData = runStyle['StyleSheet']['StyleSheetData']
                layerTextStyle = {"font":str(StyleSheetData['Font']), "fontSize":str(StyleSheetData['FontSize']),"fillColor":list(map(str, StyleSheetData['FillColor']['Values'])),"StrokeColor":list(map(str, StyleSheetData['StrokeColor']['Values']))};
                layerInfo = {"type": "text", "name":index, "val":textVal, "bbox":list(bbox), "textStyle":layerTextStyle};
                imageData.append(layerInfo);
            
        return imageData;
tools = PSD2LayImage();
imageData = tools.do();
print("=======准备上传图片========")
for img in imageData:
    if img['type'] == 'image':
        imageFile = {"imageFile":("xxx.png", open("d:\\xxx.png", "rb"), "image/jpeg")};
        r = requests.post("http://图片地址", files=imageFile);
        print(r.text)
print("已上传所有图片，正在同步数据到平台")


