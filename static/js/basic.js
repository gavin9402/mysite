var platForm = getPlatForm();

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
