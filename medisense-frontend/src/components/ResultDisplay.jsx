// src/components/ResultDisplay.jsx
import './ResultDisplay.css';

const ResultDisplay = ({ result }) => {
  const { prediction, probability } = result;
  const riskLevel = prediction === 1 ? 'High' : 'Low';
  const probabilityPercentage = Math.round(probability * 100);
  
  return (
    <div className={`result-container ${prediction === 1 ? 'high-risk' : 'low-risk'}`}>
      <h2>Prediction Result</h2>
      
      <div className="result-card">
        <div className="result-header">
          <h3>Heart Disease Risk: <span className="result-value">{riskLevel}</span></h3>
        </div>
        
        <div className="probability-bar-container">
          <div className="probability-label">Probability: {probabilityPercentage}%</div>
          <div className="probability-bar">
            <div
              className="probability-fill"
              style={{ width: `${probabilityPercentage}%` }}
            ></div>
          </div>
        </div>
        
        <div className="result-description">
          {prediction === 1 ? (
            <p>
              The model predicts a <strong>high risk</strong> of heart disease. 
              Please consult with a healthcare professional for further evaluation and advice.
            </p>
          ) : (
            <p>
              The model predicts a <strong>low risk</strong> of heart disease. 
              However, maintain a healthy lifestyle and regular check-ups for preventive care.
            </p>
          )}
        </div>
        
        <div className="result-disclaimer">
          <p>
            <strong>Disclaimer:</strong> This prediction is based on a machine learning model and should 
            not be considered as medical advice. Always consult with qualified healthcare 
            providers for diagnosis and treatment decisions.
          </p>
        </div>
      </div>
    </div>
  );
};

export default ResultDisplay;