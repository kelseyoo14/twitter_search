// Get data from search form and send post request to server with search terms


// function getTweetData(evt) {
//     evt.preventDefault();
//     console.log('getTweetData called');


//     formInputs = {
//         'search_terms': $(this).find('#search-terms').val(),
//         'number-of-tweets':$(this).find('#number-of-tweets-select').val(),
//         'filter':$(this).find('#filter-select').val(),
//         'language':$(this).find('#language-select').val()
//     };

//     $.post('/results.json',
//             formInputs,
//             addLinks);

//     console.log('post made');

//     function addLinks(result) {
//         console.log(result);
//     }
// }

// $('#search-form').on('submit', getTweetData);


// $('p').linkify();
