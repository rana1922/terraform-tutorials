const express = require("express");
const path = require("path");

const app = express();

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "templates"));

app.use(express.static(path.join(__dirname, "public")));
app.use(express.json());

app.get("/", (req, res) => {
    res.render("index");
});

app.listen(3000, "0.0.0.0", () => {
    console.log("Frontend running on port 3000");
});