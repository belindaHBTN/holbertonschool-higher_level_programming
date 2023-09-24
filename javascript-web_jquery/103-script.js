const langs = ['ar', 'az', 'be', 'bg', 'bn', 'bs', 'cs', 'da', 'de', 'dz', 'el', 'en', 'en - gb', 'en - us', 'es', 'et', 'fa', 'fi', 'fil', 'fr', 'he', 'hi', 'hr', 'hu', 'hy', 'id', 'is', 'it', 'ja', 'ka', 'kk', 'km', 'ko', 'lb', 'lo', 'lt', 'lv', 'mk', 'mn', 'ms', 'my', 'ne', 'no', 'pl', 'pt', 'ro', 'ru', 'sk', 'sl', 'sq', 'sr', 'sv', 'sw', 'th', 'tk', 'uk', 'vi', 'zh'];

const fetchHello = () => {
  const input = $('#language_code').val();
  if (langs.includes(input)) {
    $.ajax({
      type: 'GET',
      url: `https://hellosalut.stefanbohacek.dev/?lang=${input}`,
      success: function (data) {
        $('#hello').text(data.hello);
      }
    });
  } else {
    $('#hello').text('Please enter a valid lang code.');
  }
};

$(function() {
  $('#btn_translate').click(function () {
    fetchHello();
  });

  $('#language_code').focus(function () {
    $(document).keypress(function (e) {
      if (e.key === 'Enter') {
        fetchHello();
      }
    });
  });
});
