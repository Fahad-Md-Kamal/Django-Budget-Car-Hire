$(function () {
    $("input[name='{{ widget.name }}']").datetimepicker({
      format: 'd/m/Y H:i',
    });
  });