import { asyncRun } from "./py-worker.js";

const resultElement = document.getElementById("result");
const allowedElement = document.getElementById("allowedips");
const disallowedElement = document.getElementById("disallowedips");
const calcButton = document.getElementById("calc");
const clearAllButton = document.getElementById("clear-all");

function updateClearButton(input) {
    if (!input) return;
    const container = input.closest(".relative") || input.parentElement;
    const clearBtn = container ? container.querySelector(".clear-btn") : null;
    if (clearBtn) {
        if (input.value.trim() !== "") {
            clearBtn.classList.remove("hidden");
        } else {
            clearBtn.classList.add("hidden");
        }
    }
}

[allowedElement, disallowedElement].forEach((input) => {
    if (input) {
        input.addEventListener("input", () => updateClearButton(input));
        updateClearButton(input);
    }
});

calcButton.addEventListener("click", async () => {
    try {
        calcButton.disabled = true;
        resultElement.hidden = false;
        resultElement.innerHTML = '<span class="loader"></span>';
        const allowedList = allowedElement.value.split(",").map(s => s.trim()).filter(Boolean);
        const disallowedList = disallowedElement.value.split(",").map(s => s.trim()).filter(Boolean);
        const { results, error } = await asyncRun({ a: allowedList, d: disallowedList });
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
});

document.querySelectorAll(".preset-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
        const targetId = btn.getAttribute("data-target");
        const val = btn.getAttribute("data-value");
        const input = document.getElementById(targetId);
        if (input) {
            input.value = val;
            updateClearButton(input);
            input.focus();
        }
    });
});

document.querySelectorAll(".clear-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
        const targetId = btn.getAttribute("data-target");
        const input = document.getElementById(targetId);
        if (input) {
            input.value = "";
            updateClearButton(input);
            input.focus();
        }
    });
});

if (clearAllButton) {
    clearAllButton.addEventListener("click", () => {
        allowedElement.value = "";
        disallowedElement.value = "";
        updateClearButton(allowedElement);
        updateClearButton(disallowedElement);
        resultElement.hidden = true;
        resultElement.innerText = "";
        allowedElement.focus();
    });
}
