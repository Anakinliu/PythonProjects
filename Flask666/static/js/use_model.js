let tt;
function get_res() {

    let input_r = $('textarea#review').val();
    input_r = input_r.trim();
    if (input_r === "") {
        $('<div>').appendTo('.page-header')
                             .addClass('alert alert-danger')
                             .html('😂你还没输入啊😂')
                             .show().delay(1000).fadeOut();
        return;
    }
    $('div#loader_div').removeClass('hidden');
    $.getJSON('/_get_pre', {
        // 空
        input_review:input_r,
    },
    function (data) {
        tt = data;
        $('h3#max_prob').html(data.res);
        for (let i=0;i<data.probs.length;i++){
            let id = 'td#'+(i+1);
            $(id).html(data.probs[i]);
        }
        $('div#loader_div').addClass('hidden');
    });
}
$(function () {
    $('button#pull_btn').bind('click', get_res);
});
