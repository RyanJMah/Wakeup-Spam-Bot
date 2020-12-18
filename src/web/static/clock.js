// display current time by the second
var currentTime = setInterval(function() {
	var h2 = document.getElementById('clock');
	var date = new Date();

	var hours = date.getHours();
	var minutes = date.getMinutes();
	var seconds = date.getSeconds();
	var am_pm = "AM";
	
	if (hours > 12) {
		am_pm = "PM"
		hours -= 12;
	}


	h2.textContent = addZero(hours) + ":" + addZero(minutes) + ":" + addZero(seconds) + " " + am_pm;

},1000);
function addZero(time) { return (time < 10) ? "0" + time : time; }
