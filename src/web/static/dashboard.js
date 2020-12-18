init = {
	text: function(text) {
		var text_cell = document.createElement("td");
		text_cell.className = "text-left";
		text_cell.contentEditable = true;

		var text_node = document.createTextNode(text);
		text_cell.appendChild(text_node);

		return text_cell;
	},
	dropdown: function() {
		var option1 = document.createElement("option");
		option1.value = "sms";
		option1.text = "sms";
		var option2 = document.createElement("option")
		option2.value = "call";
		option2.text = "call";

		var dropdown = document.createElement("select");
		dropdown.appendChild(option1);
		dropdown.appendChild(option2);
		return dropdown;		
	},
	checkbox: function() {
		var checkbox = document.createElement("input");
		checkbox.type = "checkbox";
		return checkbox;
	},
	add_button: function(id) {
		var button = document.createElement("button");
		button.className = "add-button";
		button.onclick = function() { add_row(button); };
		button.textContent = "+";
		// button.id = "add_button_" + String(id);
		return button;
	},
	del_button: function(id) {
		var button = document.createElement("button");
		button.className = "delete-button";
		button.onclick = function() { del_row(button); };
		button.textContent = "-";
		// button.id = "del_button_" + String(id);
		return button;
	}
}

window.onload = function WindowLoad(event) {
	// alert("Page is loaded");
	add_row();
}

function add_row(element) {
	field_dummies = [
		"[click to add name]",
		'[click to add message]',
		"[click to add time]",
		"[click to add phone number]"
	]	
	var table = document.getElementById("alarm-table");
	var row = table.insertRow(-1);
	for (var i = 0; i < field_dummies.length; i++) {
		var text = init.text(field_dummies[i]);
		row.appendChild(text);
	}
	var dropdown_cell = row.insertCell(4);
	dropdown_cell.appendChild(init.dropdown());

	var checkbox_cell = row.insertCell(5);
	checkbox_cell.appendChild(init.checkbox());

	var buttons_cell = row.insertCell(6);
	buttons_cell.appendChild(init.add_button(id = table.length));
	buttons_cell.appendChild(init.del_button(id = table.length))
}
function del_row(element) {
	var row = element.parentNode.parentNode.rowIndex;
	// var col = element.parentNode.cellIndex;
	// console.log(row);
	// console.log(col);
	// console.log();
	document.getElementById("alarm-table").deleteRow(row);
}

function get_all_checkboxes() {
	var checkboxes = [];
	$('input[type=checkbox]').each(function () {		
		checkboxes.push(this.checked);
	});
	return checkboxes;
}
function get_all_dropdowns() {
	var dropdowns = [];
	$('select').each(function () {
		// dList += $(this).attr("value");
		dropdowns.push( $(this).attr("value") );
	});
	return dropdowns;
}
function send_form() {
	var table = document.getElementById('alarm-table');
	table_rows = [];
    for (var r = 1, n = table.rows.length; r < n; r++) {
		row = {
			"name": table.rows[r].cells[0].innerHTML,
			"message": table.rows[r].cells[1].innerHTML,
			"time": table.rows[r].cells[2].innerHTML,
			"phone_number": table.rows[r].cells[2].innerHTML
		};
		table_rows.push(row);
	}
	checkboxes = get_all_checkboxes();
	dropdowns = get_all_dropdowns();
	for (var i = 0; i < table_rows.length; i++) {
		table_rows[i]["type"] = dropdowns[i];
		table_rows[i]["repeat"] = checkboxes[i];
	}
	console.log(table_rows);

	var xhr = new XMLHttpRequest();
	xhr.open("POST", "http://localhost:5000/dashboard", true);
	xhr.setRequestHeader("Content-type","application/json");
	xhr.send(JSON.stringify(table_rows));

}

