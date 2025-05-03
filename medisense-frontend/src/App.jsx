import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { useState } from 'react';
import Header from './components/Header';
import HeartDiseaseForm from './components/HeartDiseaseForm';
import ResultDisplay from './components/ResultDisplay';
import MedicalImagePage from './components/MedicalImagePage'; // new component
import './App.css';

function App() {
  return (
    <Router>
      <div className="app-container">
        <Header />
        <main className="main-content">
          <Routes>
            <Route path="/" element={<HeartDiseaseFormWrapper />} />
            <Route path="/medical-image" element={<MedicalImagePage />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}


function HeartDiseaseFormWrapper() {
  const [predictionResult, setPredictionResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const API_URL = "http://127.0.0.1:5000/predict";

  const handlePrediction = async (formData) => {
    setLoading(true);
    setError(null);

    try {
      const response = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) throw new Error(`HTTP error: ${response.status}`);
      const result = await response.json();
      setPredictionResult(result);
    } catch (error) {
      setError("Prediction failed.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <>
      <HeartDiseaseForm onSubmit={handlePrediction} disabled={loading} />
      {loading && <div>Loading...</div>}
      {error && <div className="error">{error}</div>}
      {predictionResult && <ResultDisplay result={predictionResult} />}
    </>
  );
}
export default App