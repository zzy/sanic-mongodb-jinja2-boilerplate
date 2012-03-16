/* 
Ouds.us by Thinker Union Software (ThinkerUnion.com)
Copyright (c) 2007 ThinkerUnion.com. Please don't steal.
*/

function start(){
    setInterval(server_time, 1000);
    food();
    wood();
    ore();
    gold();
    people();
}

function curent_time(){
    clock = now.getHours() + ":";
    mm = now.getMinutes();
    if(mm <= 9) clock += "0";
    clock += mm + ":";
    ss = now.getSeconds();
    if(ss <= 9) clock += "0";
    return clock + ss;
}

function server_time(){
    document.getElementById("server_current_time").innerHTML = curent_time();
    now.setSeconds(now.getSeconds()+1)
}

function food(){
    food_stock_object = document.getElementById("food_stock");
    food_stock_value = parseInt(food_stock_object.innerHTML);
    food_storage_value = parseInt(document.getElementById("food_storage").innerHTML);
    food_speed_value = parseInt(document.getElementById("food_speed").innerHTML);
    if(food_stock_value < food_storage_value && food_speed_value > 0){
        setTimeout(food, 3600/food_speed_value*1000);
        food_stock_object.innerHTML = food_stock_value + 1;
    }
}

function wood(){
    wood_stock_object = document.getElementById("wood_stock");
    wood_stock_value = parseInt(wood_stock_object.innerHTML);
    wood_storage_value = parseInt(document.getElementById("wood_storage").innerHTML);
    wood_speed_value = parseInt(document.getElementById("wood_speed").innerHTML);
    if(wood_stock_value < wood_storage_value && wood_speed_value > 0){
        setTimeout(wood, 3600/wood_speed_value*1000);
        wood_stock_object.innerHTML = wood_stock_value + 1;
    }
}

function ore(){
    ore_stock_object = document.getElementById("ore_stock");
    ore_stock_value = parseInt(ore_stock_object.innerHTML);
    ore_storage_value = parseInt(document.getElementById("ore_storage").innerHTML);
    ore_speed_value = parseInt(document.getElementById("ore_speed").innerHTML);
    if(ore_stock_value < ore_storage_value && ore_speed_value > 0){
        setTimeout(ore, 3600/ore_speed_value*1000);
        ore_stock_object.innerHTML = ore_stock_value + 1;
    }
}

function gold(){
    gold_stock_object = document.getElementById("gold_stock");
    gold_stock_value = parseInt(gold_stock_object.innerHTML);
    gold_storage_value = parseInt(document.getElementById("gold_storage").innerHTML);
    gold_speed_value = parseInt(document.getElementById("gold_speed").innerHTML);
    if(gold_stock_value < gold_storage_value){
        setTimeout(gold, 3600/gold_speed_value*1000);
        gold_stock_object.innerHTML = gold_stock_value + 1;
    }
}

function people(){
    people_stock_object = document.getElementById("people_stock");
    people_stock_value = parseInt(people_stock_object.innerHTML);
    people_storage_value = parseInt(document.getElementById("people_storage").innerHTML);
    people_speed_value = parseInt(document.getElementById("people_speed").innerHTML);
    if(people_stock_value < people_storage_value){
        setTimeout(people, 3600/people_speed_value*1000);
        people_stock_object.innerHTML = people_stock_value + 1;
    }
}

function time_format(s){
    if(s >= 0){
        hours = Math.floor(s/(60*60));
        minutes = Math.floor(s/60)%60;
        seconds = s%60;
        t = hours + ":";
        if(minutes <= 9) t += "0";
        t += minutes + ":";
        if(seconds <= 9) t += "0";
        t += seconds;
    }
    else t = "0:00:0x";
    return t;
}

function event_timer(time_remain, id){
    tr = parseInt(time_remain) + 2;
    event_id = document.getElementById(id);
    if (tr == 0){
        window.location.reload();
    }
    else{
        event_id.innerHTML = time_format(tr);
        time_remain -= 1;
        setTimeout("event_timer(" + time_remain + ",'" + id + "')", 1000);
    }
}


