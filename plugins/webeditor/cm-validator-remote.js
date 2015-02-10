CodeMirror.remoteValidator = function(cm, updateLinting, options) {
	var text = cm.getValue();

	if(text.trim() == "")
	{
		updateLinting(cm, []);
		return;
	}
	
	function result_cb(error_list)
	{
		var found = [];
		
		for(var i in error_list)
		{
			var error = error_list[i];
			
			var start_line = error.line_no;

            var start_char;
            if(typeof(error.column_no_start) != "undefined")
			    start_char = error.column_no_start;
            else
			    start_char = error.column_no;

			var end_char;
            if(typeof(error.column_no_stop) != "undefined")
    			end_char = error.column_no_stop;
            else
    			end_char = error.column_no;

			var end_line = error.line_no;
			var message = error.message;

            var severity;
            if(typeof(error.severity) != "undefined")
                severity = error.severity;
            else
                severity = 'error';
			
			found.push({
				from: CodeMirror.Pos(start_line - 1, start_char),
				to: CodeMirror.Pos(end_line - 1, end_char),
				message: message,
				severity: severity // "error", "warning"
			});
		}
		
		updateLinting(cm, found);
	}
	
	options.check_cb(text, result_cb)
}

