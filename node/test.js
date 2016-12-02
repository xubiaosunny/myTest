'use strict';

var fs = require('fs');

fs.readFile('test.txt','utf-8',function(err,data){
    if(err){
        console.log("error");
        console.log(err);
    }else{
        console.log(data);
        // console.log(Buffer(data,'utf-8'));
    }
});
fs.readFile('test.jpg',function(err,data){
    if(err){
        console.log("error");
        console.log(err);
    }else{
        console.log(data);
    }
});