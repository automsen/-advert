<template>
	<view>
		<view class="uni-common-mt">
			<canvas class="canvas-element" canvas-id="canvas" id="canvas" :style="'width:' + cvsWidth + 'px; height: ' + cvsHeight + 'px;margin:0 auto;'"></canvas>
			<scroll-view class="canvas-buttons" scroll-y="true">
				<form>
					<view class="cu-form-group margin-top solid-top">
						<view class="title">文字一</view>
						<input id="text1" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
					<view class="padding solid-top">
						<text class="title" style="font-size: 15px;">图片</text>
						<view class="cu-avatar margin-left" @tap="upImage" :style="'background-image:url(' + imageUrl+ ');'"></view>
					</view>
					<view class="cu-form-group solid-top">
						<view class="title">文字e</view>
						<input id="text2" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">文字e</view>
						<input id="text3" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">文字e</view>
						<input id="text4" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">文字e</view>
						<input id="text5" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">文字e</view>
						<input id="text6" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">文字e</view>
						<input id="text7" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">文字e</view>
						<input id="text8" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">文字e</view>
						<input id="text9" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
				</form>
			</scroll-view>
		</view>
		<button class="canvas-button" @click="toTempFilePath">生成</button>
	</view>
</template>
<script>
	import tcvs from "../../common/SDK/tcanvas.js";
	
	let templeteData = {'height': 5315, 'width': 3543, 'imageDatas': [
		{'type': 'image', 'name': 0, 'url': '/static/examp/img_0.png', 'coordinate': [0, 0], 'size': [3543, 5315]}, 
		{'type': 'image', 'name': 2, 'url': '/static/examp/img_2.png', 'coordinate': [-16, 0], 'size': [3599, 5356]}, 
		{'type': 'image', 'name': 3, 'url': '/static/examp/img_3.png', 'coordinate': [-16, 2177], 'size': [3616, 2587]}, 
		{'type': 'image', 'name': 4, 'url': '/static/examp/img_4.png', 'coordinate': [-410, 4204], 'size': [4679, 1594]}, 
		{'type': 'image', 'name': 5, 'url': '/static/examp/img_5.png', 'coordinate': [194, 3709], 'size': [2262, 935]}, 
		{'type': 'image', 'name': 6, 'url': '/static/examp/img_6.png', 'coordinate': [2477, 4263], 'size': [1577, 764]}, 
		{'type': 'image', 'name': 7, 'url': '/static/examp/img_7.png', 'coordinate': [-438, 4394], 'size': [1628, 640]}, 
		{'type': 'image', 'name': 8, 'url': '/static/examp/img_8.png', 'coordinate': [2919, 725], 'size': [736, 465]}, 
		{'type': 'image', 'name': 10, 'url': '/static/examp/img_10.png', 'coordinate': [377, 477], 'size': [409, 456]}, 
		{'type': 'image', 'name': 11, 'url': '/static/examp/img_11.png', 'coordinate': [252, 433], 'size': [3097, 3072]}, 
		{'type': 'image', 'name': 12, 'url': '/static/examp/img_12.png', 'coordinate': [85, 160], 'size': [3397, 3514]}, 
		{'type': 'image', 'name': 13, 'url': '/static/examp/img_13.png', 'coordinate': [252, 522], 'size': [3035, 2802]}, 
		{'type': 'image', 'name': 14, 'url': '/static/examp/img_14.png', 'coordinate': [627, 736], 'size': [2280, 2199]}, 
		{'type': 'image', 'name': 15, 'url': '/static/examp/img_15.png', 'coordinate': [1472, 1738], 'size': [814, 488]}, 
		{'type': 'image', 'name': 16, 'url': '/static/examp/img_16.png', 'coordinate': [-86, 2468], 'size': [757, 478]}, 
		{'type': 'image', 'name': 17, 'url': '/static/examp/img_17.png', 'coordinate': [2853, 2659], 'size': [413, 261]}, 
		{'type': 'image', 'name': 18, 'url': '/static/examp/img_18.png', 'coordinate': [-81, 4448], 'size': [3919, 1605]}, 
		{'type': 'image', 'name': 19, 'url': '/static/examp/img_19.png', 'coordinate': [-88, 4459], 'size': [3907, 1523]}, 
		{'type': 'image', 'name': 20, 'url': '/static/examp/img_20.png', 'coordinate': [474, 1191], 'size': [2585, 1291]}, 
		{'type': 'text', 'name': 21, 'val': '新能源节能汽车', 'coordinate': [1341, 2545], 'size': [851, 91], 'textStyle': [{'font': {'Name': 'minijianyuan', 'Script': 3, 'FontType': 1, 'Synthetic': 0, 'fontName': '新能源节能汽车'}, 'fontSize': '359.12497', 'fillColor': ['1.0', '0.13725', '0.13725', '0.13725'], 'StrokeColor': ['1.0', '1.0', '1.0', '1.0']}]}, 
		{'type': 'text', 'name': 22, 'val': '新能源节能汽车', 'coordinate': [1290, 301], 'size': [1020, 34], 'textStyle': [{'font': {'Name': 'minijianyuan', 'Script': 3, 'FontType': 1, 'Synthetic': 0, 'fontName': '新能源节能汽车'}, 'fontSize': '359.12497', 'fillColor': ['1.0', '0.13725', '0.13725', '0.13725'], 'StrokeColor': ['1.0', '1.0', '1.0', '1.0']}]}, 
		{'type': 'text', 'name': 23, 'val': 'Only till my natural death could I tell which of what I have been doing is right or wrong, so now I have to try to do well in everything, and then wait to die a natural death.', 'coordinate': [1376, 2673], 'size': [797, 56], 'textStyle': [{'font': {'Name': 'X-songti', 'Script': 3, 'FontType': 1, 'Synthetic': 0, 'fontName': 'Only till my natural death could I tell which of what I have been doing is right or wrong, so now I have to try to do well in everything, and then wait to die a natural death.'}, 'fontSize': '29.16667', 'fillColor': ['1.0', '0.0', '0.0', '0.0'], 'StrokeColor': ['1.0', '1.0', '1.0', '1.0']}]}]}


	export default {
		data() {
			return {
				tcanvas:"",
				cvsWidth:0,
				cvsHeight:0,
				cvsScale:1,
				imageUrl:"https://ossweb-img.qq.com/images/lol/web201310/skin/big81005.jpg",
				title: 'createContext',
				names: ["rotate", "scale", "reset", "translate", "save", "restore", "drawImage", "fillText", "fill",
					"stroke", "clearRect", "beginPath", "closePath", "moveTo", "lineTo", "rect", "arc",
					"quadraticCurveTo", "bezierCurveTo", "setFillStyle", "setStrokeStyle", "setGlobalAlpha",
					"setShadow", "setFontSize", "setLineCap", "setLineJoin", "setLineWidth", "setMiterLimit"
				]
			}
		},
		onReady: function() {
			let _this = this;
			uni.getSystemInfo({
				success: function(e) {
					_this.cvsWidth = e.windowWidth;
					_this.cvsHeight = e.windowHeight / 2;
					_this.tcanvas = tcvs.initContext(uni.createCanvasContext('canvas',_this), "wx-app");

					if (templeteData['height'] >= templeteData['width']) {
						if (templeteData['height'] > _this.cvsHeight) {
							//.toFixed(2)
							_this.cvsScale = (_this.cvsHeight / templeteData['height']);
							_this.cvsWidth = _this.cvsScale * templeteData['width'];
						}
					}else {
						if (templeteData['width'] > _this.cvsWidth) {
							//.toFixed(2)
							_this.cvsScale = (_this.cvsWidth / templeteData['width']);
							_this.cvsHeight = _this.cvsScale * templeteData['height']
						}
					}
					_this.tcanvas.setCvsScale(_this.cvsScale);
					_this.initContent();
				}
			})
		},
		onShow: function(){
			if (this.tcanvas) {
				this.initContent();
			}
		},
		methods: {
			initContent() {
				
				let imageDataArr = templeteData.imageDatas;
				
				for (var imageDataIndex in imageDataArr) {
					var imageData = imageDataArr[imageDataIndex];
					var coordinate = imageData['coordinate'];
					var size = imageData['size'];
					var imageType = imageData['type'];
					var imageObj = {}
					if ("image" == imageType) {
						imageObj = new this.tcanvas.Image(imageData['url'],{
							id:imageData['name'],
							left:coordinate[0],
							top:coordinate[1],
							scaleX:size[0],
							scaleY:size[1]
						})
					} else if ("text" == imageType) {
						var textStyle = imageData['textStyle'][0];
						console.log(textStyle['fontSize'] + " == " + Math.round(textStyle['fontSize'] * this.cvsScale))
						console.log(coordinate[0] * this.cvsScale + "--" + coordinate[1] * this.cvsScale)
						var fontFamily = textStyle['font']['Name'];
						console.log(fontFamily);
						imageObj = new this.tcanvas.Text(imageData['val'],{
							id:imageData['name'],
							left:coordinate[0],
							top:coordinate[1],
							fontSize:textStyle['fontSize'] ,
							fontFamily:fontFamily + ",serif",
							maxWidth:size[0]
						})
					}
					this.tcanvas.utils.add(imageObj);
					
				}
				this.tcanvas.utils.renderAll();
				//this.drawRegionImg();
				//this.setFont();
			},
			setFont() {
				var text1 = new this.tcanvas.Text("你好,美女",{
					id:"text1",
					left:100,
					top:100,
					fontSize:12,
					maxWidth:100
				})
				this.tcanvas.utils.add(text1);
			},
			drawRegionImg () {
				var img = new this.tcanvas.Image("/static/img/md.png",{
					id:"image1",
					left:0,
					top:0,
					scaleX:this.cvsWidth,
					scaleY:this.cvsHeight
				})
				this.tcanvas.utils.add(img);
			},
			editWenZi (event) {
				let textObj = this.tcanvas.utils.get(event.target.id)
				textObj ? textObj.setTextValue(event.target.value) : "";
			},
			enterEdit (event) {
				let textObj = this.tcanvas.utils.get(event.target.id)
				textObj ? textObj.onEdit() : "";
			},
			exitEdit (event) {
				let textObj = this.tcanvas.utils.get(event.target.id)
				textObj ? textObj.offEdit() : "";
			},
			upImage (event) {
				uni.chooseImage({
					success: (chooseImageRes) => {
						const tempFilePaths = chooseImageRes.tempFilePaths;
						this.imageUrl = tempFilePaths[0];
						var img = new this.tcanvas.Image(tempFilePaths[0],{
							id:"image2",
							left:20,
							top:30,
							scaleX:50,
							scaleY:60
						})
						//img.onEdit();
						this.tcanvas.utils.add(img);
					}
				});
				
			},
			toTempFilePath: function() {
				uni.canvasToTempFilePath({
					canvasId: 'canvas',
					success: function(res) {
						console.log('to image success');
					},
					fail: function(err) {
						console.error(JSON.stringify(err))
					}
				})
			},
		}
	}
</script>

<style>
	.canvas-element-wrapper {
		display: block;
		margin-bottom: 100upx;
	}

	.canvas-element {
		width: 100%;
		height: 500upx;
		background-color: #ffffff;
	}

	.canvas-buttons {
		padding: 15upx 25upx 5upx;
		width: 100%;
		height: 720upx;
		box-sizing: border-box;
	}

	.canvas-button {
		float: left;
		line-height: 2;
		width: 300upx;
		margin: 15upx 12upx;
	}
	
	.cu-form-group .title {
		min-width: calc(4em + 15px);
	}
	
	.margin-left {
		margin-left: 45px;
	}
</style>
