// webworker.js

// Setup your project to serve `py-worker.js`. You should also serve
// `pyodide.js`, and all its associated `.asm.js`, `.json`,
// and `.wasm` files as well:
importScripts("https://cdn.jsdelivr.net/pyodide/v0.29.4/full/pyodide.js");

async function loadPyodideAndPackages() {
  self.pyodide = await loadPyodide();
}
let pyodideReadyPromise = loadPyodideAndPackages();

self.onmessage = async (event) => {
  // make sure loading is done
  await pyodideReadyPromise;
  const { id, ...context } = event.data;
  try {
    await pyodide.runPythonAsync(`
        from pyodide.http import pyfetch
        response = await pyfetch("./wg.py")
        with open("script.py", "wb") as f:
            f.write(await response.bytes())
        `);
    pkg = pyodide.pyimport("script");
    let results = await pkg.calculate_wg_allowedips(context.a, context.d).join(",");
    self.postMessage({ results, id });
  } catch (error) {
    self.postMessage({ error: error.message, id });
  }
};
