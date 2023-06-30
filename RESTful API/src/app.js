const express = require("express");
const app = express();
const student=require("./routers/student");
app.use(express.json());
app.use(student);
require("./db/conn");
const portno = 8000;

app.listen(portno, (err) => {
    console.log("Port Number Listing")
    console.log(err);
})