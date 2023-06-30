const express=require("express");
const StudentData = require("../models/students");
const router=new express.Router();


//insert data using async and await method 
router.post("/students", async (req, res) => {
    try {
        const adddata = new StudentData(req.body);
        const newdata = await adddata.save();
        res.status(201).send(newdata);
    } catch (e) {
        res.status(400).send(e);
    }
});

//get all student data 
router.get("/getstudents", async (req, res) => {
    try {
        const getstudents = await StudentData.find();
        res.send(getstudents);
    } catch (e) {
        res.send(e);
    }
})


//get the indivual student data
router.get("/getstudent/:id", async (req, res) => {
    try {
        const _id = await req.params.id;
        const getstudent = await StudentData.findById(_id);

        if (!getstudent) {
            res.status(404).send("Record not available");
        }
        else {
            res.send(getstudent);
        }


    }
    catch (e) {
        res.send(e);
    }

})

//Delete the data 
router.delete("/students/:id", async (req, res) => {
    try {
        const _id = req.params.id;
        const deletedata = await StudentData.findByIdAndDelete(_id);
        if (!req.params.id) {
            return res.status(400).send();
        }
        res.send(deletedata);
    } catch (e) {
        res.send(e)
    }
})


//Update The Data
router.patch("/students/:id",async(req,res)=>{
    try
    {
        const _id=req.params.id;
        const updatedata = await StudentData.findByIdAndUpdate(_id,req.body);
        res.send(updatedata);
        //updatedata.save();

    }
    catch(e)
    {
        res.send(e);
    }

})

module.exports=router;