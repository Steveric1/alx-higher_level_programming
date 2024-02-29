$('DIV#add_item').click(function () {
  const newElement = $('<li>').text('Item');
  $('UL.my_list').append(newElement);
});
