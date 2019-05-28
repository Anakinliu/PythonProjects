
    let p = 1;
    let e_p = 1;
    let is_error = false;
    let temp;
     function getReview() {
         console.log("getreview()");
         // console.log($('select#brand').get(0).selectedIndex);
         // console.log($('select#score').get(0).selectedIndex);
         console.log(p);
         // 显示第几页
         $('b#current_page').html(p);

          $.getJSON('/_get_reviews', {
              // 发送的数据
              start_p: p++,
              end_p: e_p,
              brand: $('select#brand').get(0).selectedIndex,
              score: $('select#score').get(0).selectedIndex,
              // 结束
          }, function(data) {// data是从服务器接收的数据
              temp = data;
              // 接受的数据出错
              if (data.result.length < 10 || data === undefined){
                  is_error = true;
                  // 显示警告框
                  $('div#crawler_warning').removeClass('hidden');
                  // 停止进度条
                  window.clearInterval(cool_down);
                  // 禁用按钮
                  $("button#resume").attr('disabled',false);
                  $("button#pause").attr('disabled',true);
                  return;
              }

              for (let i = 0; i< data.result.length; i++){
                  for(let j=0; j<2; j++){
                      let id = String("#" + (i+1) + (j+1));
                      // 不显示数字，显示表情
                      if (j === 0) {
                          $(id).text(data.result[i][0]);
                      } else {
                           let s = data.result[i][1];
                            switch (s) {
                              case 1: $(id).text('😒' + s + '星');
                              //$(id).addClass('danger');
                                  break;
                              case 2:
                              case 3: $(id).text('😐' + s + '星');
                              //$(id).addClass('warning');
                                  break;
                              case 4:
                              case 5: $(id).text('😃' + s + '星');
                              //$(id).addClass('success');
                                  break;
                            }
                      }
                  }
              }
          });
          // 启动进度条
          timer(intDiff);
          return false;
    }
     function start(){
         p =  $('input#start_p').val();
         e_p = $('input#end_p').val();
         if (p === "" || e_p === "") {
             $('<div>').appendTo('.page-header')
                             .addClass('alert alert-danger')
                             .html('😂你还没输入起始范围啊😂')
                             .show().delay(1000).fadeOut();
             return;
         }
         console.log("start()");
         getReview();
         $("button#start").attr('disabled',true);
         $("button#pause").attr('disabled',false);
         window.onbeforeunload=function(){
        return "你确定要离开吗?";
        };
     }
     function resume(){
         is_error = false;
         p = $('input#start_p').val();
         // if (p < new_p){
         //     p = new_p;
         // }
         e_p = $('input#end_p').val();
         if (parseInt(e_p) <= parseInt(p)) {
             return;
         } else {
             // 隐藏警告框
             $('div#task_end').addClass('hidden');
         }
         getReview();
         // timer(intDiff);
         $("button#pause").attr('disabled',false);
         $("button#resume").attr('disabled',true);
          window.onbeforeunload=function(){
        return "你确定要离开吗?";
        };
     }
     function pause(){
         cool_down = window.clearInterval(cool_down);
         $("button#pause").attr('disabled',true);
         $("button#resume").attr('disabled',false);
         window.onbeforeunload = null;
     }
     //开始爬取按钮事件
      $(function() {
        $('button#start').bind('click', start);
      });
     //倒计时
     let cool_down;
     let t_wait = 14;      // 获取从1到10的随机整数 ，取0的概率极小。;
     let intDiff = t_wait;
     function timer(last_time) {
         intDiff = last_time;
         if (intDiff <= 1){
             // t_wait = 20;
             intDiff = t_wait;
         }
         // 将前一个计时清除以避免叠加
         if (cool_down != null)
            clearInterval(cool_down);
         cool_down = window.setInterval(function () {
                 //与setInterval外不是不是同一线程，所以不能 在碗面times--
                 if (intDiff <= 0){
                     getReview();
                     if(p > e_p && !is_error){
                         console.log("p > e_p");
                         pause();
                         // 显示警告框
                         $('div#task_end').removeClass('hidden');
                          // 停止进度条
                         window.clearInterval(cool_down);
                     }
                 }
                 $('div#cool_down_progress').css("width", (100 - intDiff / t_wait * 100) + "%");
                 intDiff--;
             }, 1000
         );
     }