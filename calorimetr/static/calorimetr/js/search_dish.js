var Dishes = new Bloodhound({
    datumTokenizer: Bloodhound.tokenizers.obj.whitespace('q'),
    queryTokenizer: Bloodhound.tokenizers.whitespace,
    prefetch: '^/dish.json?q=%QUERY',
    remote: {
    url:'^/dish.json?q=%QUERY',
    wildcard: '%QUERY'
    }
});

$('.search-dish-query').typeahead({
    hint:true,
    highlight: true,
    // autoselect: true,
    minLength:1,
    limit: 10,
},
    {
    name: 'dishes',
    display: 'q',
    // displayKey: 'count',
    source: Dishes.ttAdapter(),
    templates: {
        empty: 'No results...',
        suggestion: function (data) {
            return '<p><span>' + data.q +'</span></p>';
        }
    }
});
