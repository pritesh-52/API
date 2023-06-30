const mongoess=require("mongoose");
const validator=require("validator");


const studentschma=new mongoess.Schema({
    name:{
        type:String,
        required:true,
        minlength:3
    },
    email:{
        type:String,
        required:true,
        unique:[true,"Email Id Already Present"],
        validate(value)
        {
            if(!validator.isEmail(value)){
                throw new Error("Invalid Email");
            }
        }
    },
    phoneno:
    {
        type:Number,
        min:10,
        required:true,  
    },
    address:
    {
        type:String,
        required:true,
    }
});

const StudentData=new mongoess.model("Studentdata",studentschma);


module.exports=StudentData;