let show_all_btn;
let jump_to_btn;
let pre_btn;
let next_btn;
let good_btn;
let normal_btn;
let bad_btn;
let page_count = 0;
let current_page_num = 1;
let cla_page_count;
// 页面加载完执行
$(document).ready(function(){
        show_all_btn = $('button#show_all');
        jump_to_btn = $('button#jump_to');
        pre_btn = $('button#pre_btn');
        next_btn = $('button#next_btn');
        good_btn = $('button#show_good');
        normal_btn = $('button#show_normal');
        bad_btn = $('button#show_bad');
        set_btn(true)
});
function set_btn(flag){
    show_all_btn.attr('disabled', !flag);
    jump_to_btn.attr('disabled', flag);
    pre_btn.attr('disabled', flag);
    next_btn.attr('disabled', flag);
    good_btn.attr('disabled', flag);
    normal_btn.attr('disabled', flag);
    bad_btn.attr('disabled', flag);
}

function set_table_pn(data, pn) {
    for (let i = 0; i< data.length; i++){
            for(let j=0; j<2; j++){
                let id = "#" + (i+1) + (j+1);
                // 不显示数字，显示表情
                if (j === 0) {
                    $(id).text(data[i][0]);
                } else {
                    let s = data[i][1];
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
    let s = '目前共爬取了 ' + page_count + ' 页，其中，';
    for (let i in cla_page_count) {
        if (cla_page_count.hasOwnProperty(i))
            s = s + i + '&nbsp' + cla_page_count[i] + '&nbsp页 |';
    }
    $('b#page_count').html(s);
    // 设置当前页
    $('b#current_page_num').html(pn);
}

function first(cla_para) {
    page_count = 0;
    $.getJSON('/_get_first_csv', {
        cla: cla_para
    }, function (data) {
        // console.log(data.result);
        // js获取页数（csv文件数）并保存到全局变量
        cla_page_count = data.count;
        for (let k in cla_page_count){
            if (cla_page_count.hasOwnProperty(k))
                page_count += cla_page_count[k];
        }
        //page_count = data.count;

        set_table_pn(data.result, 1);

        //$('div#loader_div').removeClass('hidden');
    });
}

function start(){
    first(0);
    set_btn(false);
}
function good(){
    first(3);
}
function normal(){
    first(2);
}
function bad(){
    first(1);
}

function jump(){
    let user_input = $('input#jump_num').val();
    if (user_input < 1 || user_input > page_count) {
        // 输入页码不合法
        return;
    }
    $.getJSON('/_get_want_csv', {
        want_index: user_input,
        },
        function (data) {
        // console.log(data.result);
        // 根据得到的数据设置表格内容
        set_table_pn(data.result, user_input);
        current_page_num = user_input;
        //$('div#loader_div').removeClass('hidden');
    });
}

function pre_p() {
    if (current_page_num === 1) {
        // 下面会减一，导致下标错误，所以设成循环的
        current_page_num = page_count + 1;
    }
    $.getJSON('/_get_want_csv', {
        want_index: current_page_num - 1,
        },
        function (data) {
        console.log(data.result);
        // 根据得到的数据设置表格内容
        set_table_pn(data.result, current_page_num - 1);
        current_page_num--;
        //$('div#loader_div').removeClass('hidden');
    });
}

function next_p() {
     if (current_page_num === page_count) {
        // 下面会减一，导致下标错误，所以设成循环的
        current_page_num = 1;
        } else {
            current_page_num++;
        }
    $.getJSON('/_get_want_csv', {
        want_index: current_page_num,
        },
        function (data) {
        // console.log(data.result);
        // 根据得到的数据设置表格内容
        set_table_pn(data.result, current_page_num);

        //$('div#loader_div').removeClass('hidden');
    });
}

$(function() {
    show_all_btn.bind('click', start);
});

$(function() {
    jump_to_btn.bind('click', jump);
});

$(function () {
    good_btn.bind('click', good);
});

$(function () {
    normal_btn.bind('click', normal);
});

$(function () {
    bad_btn.bind('click', bad);
});

$(function() {
pre_btn.bind('click', pre_p);
});

$(function() {
next_btn.bind('click', next_p);
});

