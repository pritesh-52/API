const mongoes=require("mongoose");
mongoes.connect("mongodb://127.0.0.1:27017/studentsapi").then(()=>console.log("Connection sucess")).catch((err)=>console.log(err));
