$('.toast').toast('show');
$(document).ready(function(){
    $(".sidenav").sidenav();
    $('select').formSelect();
    $('#copyright').text(new Date().getFullYear());
});
