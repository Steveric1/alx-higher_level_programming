$(document).ready(function (){
    $("INPUT#btn_translate").click(function (){
        $("DIV#hello").empty();
        const len = $("INPUT#btn_translate").val();
        $.ajax({
            type: "GET",
            url: "https://www.fourtonfish.com/hellosalut/hello/" + len,
            success: function (data) {
                $("DIV#hello").append(data.hello);
            }
        });
    });
});
