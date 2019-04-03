
(function() {

	// output information
	function Output(msg) {
		var m = document.getElementById("messages");
		m.innerHTML = msg + m.innerHTML;
	}


	// file drag hover
	function FileDragHover(e) {
		e.stopPropagation();
		e.preventDefault();
		//e.target.className = (e.type == "dragover" ? "hover" : "");
	}


	// file selection
	function FileSelectHandler(e) {

		// cancel event and hover styling
		FileDragHover(e);

		// fetch FileList object
		var files = e.target.files || e.dataTransfer.files;

		// process all File objects
		var k="";
		for (var i = 0, f; f = files[i]; i++) {
			k+= '<tr width="100%">';
			k+= '<td><strong>' + f.name +'</strong></td>';
			k+= '<td><strong>' + f.type +'</strong></td>';
			k+= '<td><strong>' + f.size +'</strong></td>';
			k+= '</tr>';

		}

		document.getElementById('files').innerHTML = k;

	}

	// initialize
	function Init() {

		var filedrag = document.getElementById("dropzone");
		var file = document.getElementById("file");

		// is XHR2 available?
		var xhr = new XMLHttpRequest();
		if (xhr.upload) {

			// file drop
			filedrag.addEventListener("dragover", FileDragHover, false);
			filedrag.addEventListener("dragleave", FileDragHover, false);
			filedrag.addEventListener("drop", FileSelectHandler, false);
			filedrag.style.display = "block";
			file.addEventListener("change", FileSelectHandler, false);


		}

	}

	// call initialization file
	if (window.File && window.FileList && window.FileReader) {
		Init();
	}


})();