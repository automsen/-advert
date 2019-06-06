<template>
	<view>
		<view class="uni-common-mt">
			<canvas class="canvas-element" canvas-id="canvas" id="canvas" :style="'width:' + cvsWidth + 'px; height: ' + cvsHeight + 'px;'"></canvas>
			<scroll-view class="canvas-buttons" scroll-y="true">
				<form>
					<view class="cu-form-group margin-top">
						<view class="title">文字一</view>
						<input id="text1" placeholder="两字短标题" name="input" @input="editWenZi"></input>
					</view>
					<view class="cu-form-group">
						<view class="title">图片</view>
						<input placeholder="三字标题" name="input"></input>
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
					src:"",
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
</style>
