import { asyncRun } from "./py-worker.js";

const resultElement = document.getElementById("result");
const allowedElement = document.getElementById("allowedips");
const disallowedElement = document.getElementById("disallowedips");

document.getElementById("calc").addEventListener("click", async () => {
    try {
        resultElement.hidden = false;
        const { results, error } = await asyncRun({a: allowedElement.value.split(","), d: disallowedElement.value.split(",")});
        if (results) {
            console.log("pyodideWorker return results: ", results);
            resultElement.innerText = "AllowedIPs = " + results.split(",").join(", ");
        } else if (error) {
            console.log("pyodideWorker error: ", error);
        }
    } catch (e) {
        console.log(
            `Error in pyodideWorker at ${e.filename}, Line: ${e.lineno}, ${e.message}`,
        );
    }
})
