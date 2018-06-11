$(document).ready(function() {
  
  $(".tab li").click( function() { // html의 tab 클래스 밑의 li가 클릭되면
    $(this).addClass('selectColor').siblings().removeClass('selectColor');
    var idx = $(this).index();

    if (idx == 0) { // tab1클릭시
      $(".commonContents").hide(0, function() {
        $("#contents1").show();
      });
    }

    else if (idx == 1) { // tab2클릭시
      $(".commonContents").hide(0, function() {
        $("#contents2").show();
      });
    }

    else if(idx == 2) {//tab3클릭시
      $(".commonContents").hide(0, function() {
        $("#contents3").show();
      });
    }

    else if(idx == 3) {//tab4클릭시
      $(".commonContents").hide(0, function() {
        $("#contents4").show();
      });
    }
  });//click
});//jQuery
