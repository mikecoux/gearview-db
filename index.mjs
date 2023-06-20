/*
Run this file to start the express API
$ node index.mjs
*/

import express from "express";
import cors from "cors";
import "express-async-errors";
import products from "./routes/products.mjs";
import dotenv from "dotenv";
dotenv.config();

const PORT = process.env.PORT || 5050;
const app = express();

app.use(cors());
app.use(express.json());

// Load the routes
app.use("/products", products);

// Global error handling
app.use((err, _req, res, next) => {
  res.status(500).send("Uh oh! An unexpected error occured.")
})

// start the Express server
app.listen(PORT, () => {
  console.log(`Server is running on port: ${PORT}`);
});