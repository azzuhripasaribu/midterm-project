$(document).ready(()=>{
    let Current_path = window.location.href;
    let center_JSON_path = Current_path + "json"
    let areas_JSON_path = Current_path + "areas"
    $.get(center_JSON_path,(data)=>{
        for(var i = 0; i < data.length; i++) {
            let center = data[i].fields;
            let name = center.name;
            let website = center.website;
            let email = center.email;
            pk = data[i].pk;
            $("<li class=\"list-group-item shadow-sm mb-3 py-4 border-top rounded-3\"><div class=\"row\"><h2>"+name+"</h2></div><div class=\"row\"><div class=\"col\">Website:<p><a href=\""+website+"\">"+website+"</a></p>email:<p>"+email+"</p></div><div class=\"col text-center\">areas:<ul class=\"list-group\" id=\"areas-"+pk+"\"></ul></div></div></li>").appendTo("#center-list")
        }
    });

    $.get(areas_JSON_path,(data)=>{
        for(var i = 0; i < data.length; i++) {
            let area = data[i].fields;
            centers = area.center
            for(var j = 0; j < centers.length; j++){
                $("<li class=\"list-group-item  \" style=\"background-color:#bf4aa8; color:#FFFFFF;\">"+area.name+"</li>").appendTo("#areas-" + centers[j])
            }
        }
    });
});