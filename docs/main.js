import { asyncRun } from "./py-worker.js";

const resultElement = document.getElementById("result");
const allowedElement = document.getElementById("allowedips");
const disallowedElement = document.getElementById("disallowedips");
const calcButton = document.getElementById("calc");

calcButton.addEventListener("click", async () => {
    try {
        calcButton.disabled = true;
        resultElement.hidden = false;
        resultElement.innerHTML = '<span class="loader"></span>';
        const { results, error } = await asyncRun({a: allowedElement.value.split(","), d: disallowedElement.value.split(",")});
        if (results) {
            console.log("pyodideWorker return results: ", results);
            resultElement.innerText = "AllowedIPs = " + results.split(",").join(", ");
        } else if (error) {
            console.log("pyodideWorker error: ", error);
            resultElement.innerText = "Error: " + error;
        }
    } catch (e) {
        console.log(
            `Error in pyodideWorker at ${e.filename}, Line: ${e.lineno}, ${e.message}`,
        );
        resultElement.innerText = "An error occurred.";
    } finally {
        calcButton.disabled = false;
    }
})
