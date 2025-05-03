import { useState, useEffect } from 'react';
import './MedicalImagePage.css';

const MedicalImagePage = () => {
  const [imageFile, setImageFile] = useState(null);
  const [imagePreview, setImagePreview] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [detectionType, setDetectionType] = useState('pneumonia'); // 'pneumonia' or 'brain-tumor'

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    if (file) {
      setImageFile(file);
      setResult(null);
      
      // Create image preview
      const reader = new FileReader();
      reader.onloadend = () => {
        setImagePreview(reader.result);
      };
      reader.readAsDataURL(file);
    }
  };

  const handleSubmit = async () => {
    if (!imageFile) return;

    const formData = new FormData();
    formData.append('image', imageFile);

    setLoading(true);
    try {
      // Choose endpoint based on detection type
      const endpoint = detectionType === 'pneumonia' 
        ? "http://127.0.0.1:5000/predict_pneumonia" 
        : "http://127.0.0.1:5000/predict_brain_tumor";
        
      const response = await fetch(endpoint, {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setResult(data);
    } catch (err) {
      setResult({ error: "Prediction failed. Please try again." });
    } finally {
      setLoading(false);
    }
  };

  const parseConfidence = (confidence) => {
    if (typeof confidence === 'string') {
      
      const numValue = parseFloat(confidence.replace('%', '')) / 100;
      return isNaN(numValue) ? 0 : numValue;
    }
    return !confidence || isNaN(confidence) ? 0 : confidence;
  };

  const getConfidenceClass = (confidence) => {
    if (!confidence || isNaN(confidence)) return 'low';
    if (confidence >= 0.7) return 'high';
    if (confidence >= 0.4) return 'medium';
    return 'low';
  };

  const changeDetectionType = (type) => {
    setDetectionType(type);
    setResult(null);
  };

 
  const getTitle = () => {
    return detectionType === 'pneumonia' 
      ? 'Pneumonia Detection' 
      : 'Brain Tumor Detection';
  };

  // Get appropriate instruction based on detection type
  const getInstruction = () => {
    return detectionType === 'pneumonia' 
      ? 'Upload a chest X-ray image for analysis' 
      : 'Upload a brain MRI scan for analysis';
  };

  // Get tumor color class based on tumor type
  const getTumorClass = (tumorType) => {
    switch(tumorType?.toLowerCase()) {
      case 'meningioma': return 'meningioma';
      case 'glioma': return 'glioma';
      case 'pituitary': return 'pituitary';
      case 'no tumor': return 'no-tumor';
      default: return '';
    }
  };

  return (
    <div className="medical-container">
      <header className="medical-header">
        <h2>Medical Image Analysis</h2>
        <p>AI-powered diagnostic assistance tool</p>
      </header>

      <div className="detection-type-selector">
        <div className="detection-type-tabs">
          <div 
            className={`detection-tab ${detectionType === 'pneumonia' ? 'active' : ''}`}
            onClick={() => changeDetectionType('pneumonia')}
          >
            Pneumonia
          </div>
          <div 
            className={`detection-tab ${detectionType === 'brain-tumor' ? 'active' : ''}`}
            onClick={() => changeDetectionType('brain-tumor')}
          >
            Brain Tumor
          </div>
        </div>
      </div>

      <div className="upload-section">
        <h3>{getTitle()}</h3>
        <p>{getInstruction()}</p>
        
        <div className="file-input-wrapper">
          <input 
            type="file" 
            accept="image/*" 
            onChange={handleImageChange} 
            className="file-input" 
            id="file-input"
          />
          <label htmlFor="file-input" className="file-input-label">
            <div className="file-input-icon">📁</div>
            <div className="file-input-text">
              {imageFile ? 'Change image' : `Choose ${detectionType === 'pneumonia' ? 'an X-ray image' : 'an MRI scan'}`}
            </div>
          </label>
        </div>
        
        {imagePreview && (
          <div className="image-preview">
            <img src={imagePreview} alt="Medical image preview" style={{ maxWidth: '100%', maxHeight: '300px', borderRadius: '8px' }} />
            <div className="file-name">{imageFile.name}</div>
          </div>
        )}
        
        <button 
          onClick={handleSubmit} 
          disabled={!imageFile || loading} 
          className="predict-button"
        >
          {loading ? (
            <>
              <span className="loading-spinner"></span>
              Processing...
            </>
          ) : (
            `Analyze ${detectionType === 'pneumonia' ? 'X-ray' : 'MRI'}`
          )}
        </button>
      </div>

      {result && (
        <div className={`result-section ${result.error ? 'error' : ''}`}>
          {result.error ? (
            <div className="error-message">
              <span className="error-icon">⚠️</span>
              {result.error}
            </div>
          ) : detectionType === 'pneumonia' ? (
            /* Pneumonia Results */
            <>
              <div className="result-header">Analysis Results</div>
              <div className="result-content">
                <div className="result-info">
                  <span className="result-label">Diagnosis:</span>
                  <span className={`result-value ${result.prediction === 'Pneumonia' ? 'positive' : 'negative'}`}>
                    {result.prediction}
                  </span>
                </div>
                <div className="result-info">
                  <span className="result-label">Confidence:</span>
                  <span className="result-value">
                    {typeof result.confidence === 'string' 
                      ? result.confidence 
                      : (result.confidence && !isNaN(result.confidence) 
                        ? `${(result.confidence * 100).toFixed(1)}%` 
                        : 'Unavailable')}
                  </span>
                </div>
              </div>
              
              <div className="confidence-bar">
                <div 
                  className={`confidence-bar-fill ${getConfidenceClass(parseConfidence(result.confidence))}`}
                  style={{ width: `${parseConfidence(result.confidence) * 100}%` }}
                />
              </div>
              
              <div className="detection-description">
                <strong>About this detection:</strong> Pneumonia is an infection that inflames the air sacs in one or both lungs. 
                The AI analyzes patterns in chest X-rays that may indicate fluid accumulation in the lungs typically associated with pneumonia.
              </div>
              
              <div className="result-footer" style={{ marginTop: '1rem', fontSize: '0.85rem', color: '#718096' }}>
                This is an automated analysis. Please consult with a medical professional for diagnosis.
              </div>
            </>
          ) : (
            /* Brain Tumor Results */
            <>
              <div className="result-header">Brain Tumor Analysis Results</div>
              
              <div className="tumor-result">
                <div className={`tumor-classification ${getTumorClass(result.tumor_type)}`}>
                  {result.tumor_type || 'Analysis Complete'}
                </div>
                
                <div className="result-content">
                  <div className="result-info">
                    <span className="result-label">Confidence:</span>
                    <span className="result-value">
                      {typeof result.confidence === 'string' 
                        ? result.confidence 
                        : (result.confidence && !isNaN(result.confidence) 
                          ? `${(result.confidence * 100).toFixed(1)}%` 
                          : 'Unavailable')}
                    </span>
                  </div>
                </div>
                
                <div className="confidence-bar">
                  <div 
                    className={`confidence-bar-fill ${getConfidenceClass(parseConfidence(result.confidence))}`}
                    style={{ width: `${parseConfidence(result.confidence) * 100}%` }}
                  />
                </div>
              </div>
              
              <div className="detection-description">
                <strong>About this detection:</strong> Brain tumor classification analyzes MRI scans to identify potential 
                tumors and their types. The main categories include Meningioma (typically benign tumors arising from the meninges), 
                Glioma (tumors that occur in the brain and spinal cord), and Pituitary (tumors that form in the pituitary gland).
              </div>
              
              <div className="result-footer" style={{ marginTop: '1rem', fontSize: '0.85rem', color: '#718096' }}>
                This analysis is preliminary. Medical diagnosis should be conducted by healthcare professionals.
              </div>
            </>
          )}
        </div>
      )}
    </div>
  );
};

export default MedicalImagePage;