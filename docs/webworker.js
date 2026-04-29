// webworker.js

// Setup your project to serve `py-worker.js`. You should also serve
// `pyodide.js`, and all its associated `.asm.js`, `.json`,
// and `.wasm` files as well:
importScripts("https://cdn.jsdelivr.net/pyodide/v0.26.2/full/pyodide.js");

async function loadPyodideAndPackages() {
  self.pyodide = await loadPyodide();
}
let pyodideReadyPromise = loadPyodideAndPackages();

self.onmessage = async (event) => {
  // make sure loading is done
  await pyodideReadyPromise;
  // Don't bother yet with this line, suppose our API is built in such a way:
  const { id, ...context } = event.data;
  // Now is the easy part, the one that is similar to working in the main thread:
  try {
    await pyodide.runPythonAsync(`
        from pyodide.http import pyfetch
        response = await pyfetch("wg.py")
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
