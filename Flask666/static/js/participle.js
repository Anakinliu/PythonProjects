 let do_part_btn;
    let load_part_btn;
    let pre_btn;
    let next_btn;
    let loaded = 0;
    let current_page_num = 1;
    let page_count = 0;
    let show;
    $(function(){
        do_part_btn = $('button#do_participle');
        load_part_btn = $('button#load_participle');
        load_part_btn.attr('disabled', true);
        pre_btn = $('button#pre_btn');
        next_btn = $('button#next_btn');
    });

    function set_table(result) {
        let i;
        for (i=1; i <= 10; i++) {
            let id = 'td#' + i;
            $(id).html("");
        }
        for (i = 1; i <= result.length; i++) {
            let id = 'td#' + i;
            $(id).html(result[i-1]);
        }
    }
    function do_part() {
        // 显示加载动画
        $('div#loader_div').removeClass('hidden');
        // 禁用按钮
        do_part_btn.attr('disabled', true);
        $.getJSON('/_do_participle', {
            // 空
        }, function (data) {
            loaded = data.result;
            // 后台执行完分词后隐藏动画,启用按钮
            if (loaded === 1){
                $('div#loader_div').addClass('hidden');
                load_part_btn.attr('disabled', false);
            }
            // 警告框
            $('<div>').appendTo('.page-header').addClass('alert alert-success').html('🎉分词已完成🎉').show().delay(1500).fadeOut();

        });
    }

    function load_part() {
        // 显示加载动画
        //$('div#loader_div').removeClass('hidden'); // 时间短
        // 获取跳转页码
        let jump_num = $('input#jump_num').val();
        if (jump_num.trim() === "") {
            jump_num = 1;
        } else {
            current_page_num = jump_num;
        }
        $.getJSON('/_get_participle', {
            // 空
            start_index: jump_num,
        }, function (data) {
            // 隐藏加载动画
            $('div#loader_div').addClass('hidden');
            //console.log(data.result);
            //console.log(data.count);
            // 保存总页数
            page_count = data.c;
            show = data.r;
            $('b#page_count').html(page_count);

            $('b#current_page_num').html(current_page_num);
            set_table(data.r);
        });
    }

    function pre_p() {
        console.log(current_page_num);
        if (current_page_num <= 1) {
            // 下面会减一，导致下标错误，所以设成循环的
            current_page_num = parseInt(page_count/10) + 2;
        }
        $.getJSON('/_get_participle', {
            start_index: current_page_num - 1,
            },
            function (data) {
            //console.log(data.result);
            // 根据得到的数据设置表格内容
            set_table(data.r);
            current_page_num--;
            $('b#current_page_num').html(current_page_num);
            //$('div#loader_div').removeClass('hidden');
        });
    }

    function next_p() {
        if (current_page_num >= parseInt(page_count/10) + 1) {
          // 下面会减一，导致下标错误，所以设成循环的
            current_page_num = 0;
        }
        $.getJSON('/_get_participle', {
                start_index: current_page_num + 1,
            },
            function (data) {
            // console.log(data.result);
            // 根据得到的数据设置表格于当前页码
            set_table(data.r);
            current_page_num++;
            $('b#current_page_num').html(current_page_num);
            //$('div#loader_div').removeClass('hidden');
        });
    }

    $(function () {
        do_part_btn.bind('click', do_part);
    });

    $(function () {
        load_part_btn.bind('click', load_part)
    });

    // 文档载入完成后执行
    $(function() {
    pre_btn.bind('click', pre_p);
    });
    // 文档载入完成后执行
    $(function() {
    next_btn.bind('click', next_p);
    });