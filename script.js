const handleSubmit = async (e) => {
  e.preventDefault();
  if (!codeInput.trim()) {
    onError(new Error('Please provide code to scan'));
    return;
  }

  setIsLoading(true);
  try {
    const response = await fetch("http://localhost:5000/scan/code", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ code: codeInput })
    });

    const data = await response.json();
    setResults(data);
    onScanComplete(data);
  } catch (err) {
    onError(err);
  } finally {
    setIsLoading(false);
  }
};
