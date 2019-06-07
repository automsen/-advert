<template>
	<view>
		<view class="uni-common-mt">
			<canvas class="canvas-element" canvas-id="canvas" id="canvas" :style="'width:' + cvsWidth + 'px; height: ' + cvsHeight + 'px;'"></canvas>
			<scroll-view class="canvas-buttons" scroll-y="true">
				<form>
					<view class="cu-form-group margin-top">
						<view class="title">文字一</view>
						<input id="text1" placeholder="两字短标题" name="input" @focus="enterEdit" @input="editWenZi" @blur="exitEdit"></input>
					</view>
					<view class="padding">
						<text class="title">图片</text>
						<view class="cu-avatar margin-left" style="background-image:url(https://ossweb-img.qq.com/images/lol/web201310/skin/big81005.jpg);"></view>
					</view>
				</form>
			</scroll-view>
		</view>
	</view>
</template>
<script>
	import tcvs from "../../common/SDK/tcanvas.js";
	export default {
		data() {
			return {
				tcanvas:"",
				cvsWidth:0,
				cvsHeight:0,
				title: 'createContext',
				names: ["rotate", "scale", "reset", "translate", "save", "restore", "drawImage", "fillText", "fill",
					"stroke", "clearRect", "beginPath", "closePath", "moveTo", "lineTo", "rect", "arc",
					"quadraticCurveTo", "bezierCurveTo", "setFillStyle", "setStrokeStyle", "setGlobalAlpha",
					"setShadow", "setFontSize", "setLineCap", "setLineJoin", "setLineWidth", "setMiterLimit"
				]
			}
		},
		onReady: function() {
			console.log(tcvs)
			let _this = this;
			uni.getSystemInfo({
				success: function(e) {
					_this.cvsWidth = e.windowWidth;
					_this.cvsHeight = e.windowHeight / 3;
					_this.tcanvas = tcvs.initContext(uni.createCanvasContext('canvas',_this), "wx-app");
					//context = this.cvsContext = uni.createCanvasContext('canvas',this);
					_this.initContent();
				}
			})
		},
		methods: {
			initContent() {
				this.drawRegionImg();
				this.setFont();
				//this.cvsContext.draw();
				//this.drawRect();
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
				var img = new this.tcanvas.Image("../../static/img/md.png",{
					id:"image1",
					left:0,
					top:0,
					scaleX:this.cvsWidth,
					scaleY:this.cvsHeight
				})
				this.tcanvas.utils.add(img);
			},
			drawRect () {
			  var fcanvas = this.fCanvas;
			  fcanvas.add(new fabric.Circle({ radius: 30, fill: '#f55', top: 100, left: 100 }));
			  fcanvas.item(0).set({
				borderColor: 'red',
				cornerColor: 'green',
				cornerSize: 6,
				transparentCorners: false
			  });
			  fcanvas.setActiveObject(fcanvas.item(0));
			  //canvas.renderAll();
			},
			editWenZi (event) {
				let textObj = this.tcanvas.utils.get(event.target.id)
				textObj.setTextValue(event.target.value)
			},
			enterEdit (event) {
				let textObj = this.tcanvas.utils.get(event.target.id)
				textObj.onEdit();
			},
			exitEdit (event) {
				let textObj = this.tcanvas.utils.get(event.target.id)
				textObj.offEdit();
			}
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
