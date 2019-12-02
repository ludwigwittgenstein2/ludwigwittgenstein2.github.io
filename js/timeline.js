$('[data-label]')
.mouseover(function () {
  $('#TimelineLabel').text($(this).attr('data-label'));
  $('#TimelineFlavor').text($(this).attr('data-flavor'));
})
.mouseleave(function () {
  $('#TimelineLabel,#TimelineFlavor').text('');
});
