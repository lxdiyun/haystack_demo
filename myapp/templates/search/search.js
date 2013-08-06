var source = [
"Option 1",
"Option 2"
];
$('input').typeahead({
    source: function (query, typeahead) {
	    Dajaxice.myapp.autocomplete(function(data){
		    typeahead(data.results)
	    },
	    {'inputs': query})
	    typeahead(source)
	    
    }
});

