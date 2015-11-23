var platForm = getPlatForm();

var slideShow = false;
var tagsShow = false;

$(function(){
		onAction();
		showBody();
		});

function islogin() {
	var loged = $("#loged").attr("loged");
	return loged != "False";
}

function showBody() {
	$("body").animate(
			{opacity: 1}, 
			1000, 
			function() {
			});
}

function onAction() {
	$(".play").on("click", slidePlay);
	$(".cover").on("click", hideSlide);
	$(".tags-column").on("click", tagsPlay)
	if (platForm === "pc") {
		onMouseFocusAction();
	} else {
	/*
	 * todo 手机端的自适应
		$(".left-box").css({
				"display": "none",
				});
		$(".right-box").css({
				"display": "none",
				})
		$(".paper").css({
				"width": "100%",
				"margin-top": "100px",
				});
		$(".section").css({
				"width": "100%",
				})
	*/
	}
}

function tagsPlay() {
}

function onMouseFocusAction() {
	var mouseOnList = {
		"logo": "logo",
		"play": "play",
		"home-column": "home",
		"tags-column": "tags",
		"blog-column": "blog",
		"about-column": "about",
		"contact-column": "contact",
	};
	for (var item in mouseOnList) {
		var href = mouseOnList[item];
		$("." + item).on("mouseenter", {"msg":{
				"item": item,
				"href": href,
				}}, mouseEnter);
		$("." + item).on("mouseleave", {"msg":{
				"item": item,
				"href": href,
				}}, mouseLeave);
	}
}

function mouseEnter(event) {
	var element = $(this);
	var href = event.data.msg.href;
	var item = event.data.msg.item;
	//var element = $("."+ event.data.msg);
	element.css({
			"background-color": "#734444",
			});
}

function mouseLeave(event) {
	var element = $(this);
	var href = event.data.msg.href;
	var item = event.data.msg.item;
	//var element = $("." + event.data.msg);
	element.removeAttr("style");
}

function slidePlay() {
	if (slideShow === false) {
		showSlide();
	} else {
		hideSlide();
	}
}

function showSlide() {
	var slide = $(".slide");
	var cover = $(".cover");
	var content = $("#content");
	slide.animate({
		left: "0px",
	}, 500, function() {
	});
	content.animate({
		left: "200px",
	}, 500, function(){
	});
	cover.removeAttr("hidden");
	slideShow = true;
}

function hideSlide() {
	var slide = $(".slide");
	var cover = $(".cover");
	var content = $("#content");
	slide.animate({
		left: "-200px",
	}, 500);
	content.animate({
		left: "0",
	}, 500)
	cover.attr("hidden", "");
	slideShow = false;
}
function getPlatForm() {
	var ua = navigator.userAgent;
	var ipad = ua.match(/(iPad).*OS\s([\d_]+)/),
		isIphone = !ipad && ua.match(/(iPhone\sOS)\s([\d_]+)/),
		isAndroid = ua.match(/(Android)\s+([\d.]+)/),
		isMobile = isIphone || isAndroid;
	if (isMobile) {
		return "mobile";
	} else {
		return "pc";
	}
}

function checkMobile(mobile){
	var pattern = /^0?1[3|4|5|8][0-9]\d{8}$/;
	mobile = mobile.replace(new RegExp(" ","gm"),"");
	mobile = mobile.replace("+86","");
	if(!pattern.test(mobile)){
		return false;
	}
	return mobile;
}

function checkPassword(password) {
	var pattern = /^[a-zA-Z]([a-zA-Z0-9]{5,14})/;
	if (!pattern.test(password)) {
		return false;
	}
	return true;
}
