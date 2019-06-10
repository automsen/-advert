# -*- coding: UTF-8 -*- 

from psd_tools2 import PSDImage
from builtins import enumerate
class PSD2LayImage:
    
    psd = None;
    
    floder = "examp"
    
    def __init__(self):
        
        #获取文件
        self.psd = PSDImage.open('my_image.psd');

        #保存图片
        self.psd.compose().save(self.floder + '/main.png')
        
    def do(self):
        
        print("-----", self.psd.header);
        psdData = {};
        psdData['height'] = 5315;
        psdData['width'] = 3543;
        imageData = [];
        psdArr = self.psd.descendants();
        
        print(psdArr)
        
        for index, layer in enumerate(psdArr):
            #获取坐标
            bbox = layer.bbox;
            
            #如果坐标小于0,暂时先过滤掉，尽量过滤些超出画布范围的一些图层
#             if bbox[0] < 0:
#                 continue;
            
            #先放在这里，试验了番还不确定这是干什么用的
#             if layer.has_vector_mask() :
#                 continue;
            #如果是文本
            if layer.kind == 'type':
                textVal = " ".join(layer.text.split());
                
                print(index, layer.engine_dict['StyleRun']) 
                text = layer.engine_dict['Editor']['Text'].value
                fontset = layer.resource_dict['FontSet']
                runlength = layer.engine_dict['StyleRun']['RunLengthArray']
                rundata = layer.engine_dict['StyleRun']['RunArray']
                _index = 0
                layerTextStyleArr = [];
                for length, style in zip(runlength, rundata):
                    #print("#####", _index, length)
                    substring = text[_index:_index + length]
                    StyleSheetData = style['StyleSheet']['StyleSheetData']
                    font = fontset[StyleSheetData['Font']]
                    font['fontName'] = " ".join(substring.split());
                    layerTextStyle = {"font":font, "fontSize":str(StyleSheetData['FontSize']),"fillColor":list(map(str, StyleSheetData['FillColor']['Values'])),"StrokeColor":list(map(str, StyleSheetData['StrokeColor']['Values'])) if 'StrokeColor' in StyleSheetData else []};
                    layerTextStyleArr.append(layerTextStyle);
                    #print('%r gets %s' % (substring, font))
                    _index += length 
                
                layerInfo = {"type": "text", "name":index, "val":textVal, "coordinate":list(layer.offset), "size":list(layer.size), "textStyle":layerTextStyleArr};
                imageData.append(layerInfo);
                continue;
            if layer.has_pixels():
                layer_image = layer.topil();
                layer_image_path = self.floder + "/img_" + str(index) + ".png";
                layer_image.save(layer_image_path);
                layerInfo = {"type": "image", "name":index, "url":layer_image_path, "coordinate":list(layer.offset), "size":list(layer.size)};
                imageData.append(layerInfo);
                
#                 styleRun = layer.engine_dict['StyleRun'];
#                 fontset = layer.resource_dict['FontSet']
#                 
#                 runStyle = styleRun["RunArray"][0];
#                 StyleSheetData = runStyle['StyleSheet']['StyleSheetData']
#                 layerTextStyleArr = [];
#                 layerTextStyle = {"font":str(StyleSheetData['Font']), "fontSize":str(StyleSheetData['FontSize']),"fillColor":list(map(str, StyleSheetData['FillColor']['Values'])),"StrokeColor":list(map(str, StyleSheetData['StrokeColor']['Values'])) if 'StrokeColor' in StyleSheetData else []};
#                 layerInfo = {"type": "text", "name":index, "val":textVal, "bbox":list(bbox), "textStyle":layerTextStyle};
#                 imageData.append(layerInfo);
        psdData['imageDatas'] = imageData;
        return psdData;
tools = PSD2LayImage();
psdData = tools.do();
print(psdData)
# print("=======准备上传图片========")
# for img in imageData:
#     if img['type'] == 'image':
#         imageFile = {"imageFile":("xxx.png", open("d:\\xxx.png", "rb"), "image/jpeg")};
#         r = requests.post("http://图片地址", files=imageFile);
#         print(r.text)
# print("已上传所有图片，正在同步数据到平台")


