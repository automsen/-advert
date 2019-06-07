/*
* author tanglongsen
* modify by 20190606
* */
var tcanvas = {
	_objects : [],
	contextContainer : "",
	//h5， wx-app， pay-app
	platType:"h5",
	initContext: function (obj, type) {
		tcanvas.contextContainer = obj || {};
		if (type != "h5" &&  type != "wx-app" && type != "pay-app"){
			tcanvas.platType = "h5"
			return tcanvas;
		}
		if (type){
			tcanvas.platType = type
			return tcanvas;
		}
		
		tcanvas.platType = "h5"
		
		return tcanvas;
	},
	getContext : function(){
		return tcanvas.contextContainer;
	},
	CanvasObj : function (){
		this.id = "object1",
		this.type = "object",
		this.top = 0;
		this.left = 0;
		this.width = 0;
		this.height = 0;
		this.scaleX = 200;
		this.scaleY = 200;
		this.changeCount = 0;
		this.renderFunction = false;
		this.isEdit = false;
		this.rotateCircle = {
			radius:1
		};
		this.onMouseDown = function(){
			
		
		};
		this.onEdit = function(flag){
			if (!flag){
				tcanvas.utils._obj2OffEdit();
			}
			this.isEdit = true;
			this.changeCount++;
		},
		this.offEdit = function(flag){
			if (!flag){
				tcanvas.utils._obj2OffEdit();
			}
			this.isEdit = false;
			this.changeCount--;
		},
		this.renderControlRect = function(ctx, x, y, width, height){
			//添加对象边框
			if (this.isEdit) {
				ctx.setLineDash([5,5]);
				ctx.strokeStyle='red';
				ctx.lineWidth='2';
				ctx.strokeRect(x, y, width, height);
				ctx.stroke();
				
				//添加边框操作对象可以是图形，图片
				
			}
			
		}
		
		
	},
	utils : {
		add : function(_object) {
			
			//这个地方判断下数组中是否已经添加，后面再加上
			tcanvas._objects.push(_object);
			Object.defineProperty(_object,'changeCount', {
				get: function () {
					return "";
				},
				set: function (newValue) {
					console.log(newValue);//成功触发方法打印出设置的值
					tcanvas.utils.renderAll();
				}
			});
			tcanvas.utils.renderAll();
		},
		get : function(id){
			var _objectArr = tcanvas._objects;
			for (var _object in _objectArr) {
				if (_objectArr[_object].id == id) {
					return _objectArr[_object];
				}
			}
		},
		_obj2Prop : function(_this, obj) {
			for (var oj in obj) {
				_this[oj] = obj[oj];
			}
		},
		_obj2OffEdit : function() {
			var renderAllObj = tcanvas._objects;
			for (var _object in renderAllObj) {
			  renderAllObj[_object].isEdit = false;
			}
		},
		_obj2onEdit : function() {
			var renderAllObj = tcanvas._objects;
			for (var _object in renderAllObj) {
			  renderAllObj[_object].isEdit = true;
			}
		},
		renderAll : function (){
			var renderAllObj = tcanvas._objects;
			for (var _object in renderAllObj) {
			  renderAllObj[_object].renderFunction();
			}
			
			if (tcanvas.platType == "wx-app") {
				tcanvas.getContext().draw();
			}
			//tcanvas.getContext().draw();
		}
	
	},
	Image : function(image, imageObj) {
		//继承父类
		tcanvas.CanvasObj.call(this);
		//this.offEdit();
		imageObj.type = "image";
		imageObj.renderFunction = function(){
			var context = tcanvas.getContext();
			context.drawImage(image, this.left, this.top, this.scaleX, this.scaleY);
			this.renderControlRect(context, this.left, this.top, this.scaleX, this.scaleY);
		}
		tcanvas.utils._obj2Prop(this, imageObj);
	},
	NetImage : function(imageObj) {
		imageObj = Object.assign(tcanvas.canvasObj, imageObj);
		imageObj.type = "image";
		var image = new Image();
		image.src = imageObj.src;
		image.onload = function () {
			var contextContainer = tcanvas.getContext();
			contextContainer.drawImage(image, imageObj.left, imageObj.top, imageObj.scaleX, imageObj.scaleY)
		
		}
		imageObj.renderFunction = function(imageObj){
			var contextContainer = tcanvas.getContext();
			contextContainer.drawImage(image, imageObj.left, imageObj.top, imageObj.scaleX, imageObj.scaleY)
		}
		
	},
	Text : function(textStr, textObj){
		var context = tcanvas.getContext();
		//继承父类
		tcanvas.CanvasObj.call(this);
		textObj.type = "text";
		textObj.textValue = textStr || "请输入文字";
		textObj.fontSize = textObj.fontSize || 40;
		textObj.maxWidth = textObj.maxWidth || 2048;
		textObj.renderFunction = function(){
			
			//设置样式
			setTextStyle(context, textObj);
			
			//获取最大定义宽度
			var maxWidth = getWidth(context, textObj);
			
			//写文字
			context.fillText(this.textValue, this.left, this.top, this.maxWidth);
			//(line-height - font-size) * 2 + font-size;
			var fontHeight = textObj.fontSize * 1.0
			this.renderControlRect(context, this.left - this.maxWidth/2, this.top - (fontHeight/2 * 1.7), this.maxWidth, fontHeight);
		}
		textObj.setTextValue = function(val) {
			this.textValue = val;
			this.onEdit();
		}
		tcanvas.utils._obj2Prop(this, textObj);
		
		//设置样式
		function setTextStyle(context, textObj){
			//context.fillStyle = "blue";
			context.font = "bold " + textObj.fontSize + "px sans-serif";
			context.textAlign = "center";
		}
		
		//根据字体实际长度获取最大宽度
		function getWidth(context, textObj) {
			var textMeasu = context.measureText(textObj.textValue);
			var width = textMeasu.width;
			if (textObj.maxWidth < width) {
				return width;
			}
			return textObj.maxWidth;
		}
		
	}

}
	
module.exports = tcanvas;
