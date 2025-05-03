// src/components/HeartDiseaseForm.jsx
import { useState } from 'react';
import './HeartDiseaseForm.css';

const HeartDiseaseForm = ({ onSubmit, loading }) => {
  const [formData, setFormData] = useState({
    age: '',
    sex: '1', 
    chestPainType: '1', 
    bp: '', 
    cholesterol: '',
    maxHR: '', 
    exerciseAngina: '0', 
    stDepression: '',
    slopeOfST: '1', 
    numberOfVesselsFluro: '0', 
    thallium: '3', 
    ekgResults: '0',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit(formData);
  };

  return (
    <div className="form-container">
      <h2>Heart Disease Prediction</h2>
      <p className="form-description">
        Fill in the form below with patient medical data to predict heart disease risk.
      </p>
      
      <form onSubmit={handleSubmit}>
        <div className="form-row">
          <div className="form-group">
            <label htmlFor="age">Age</label>
            <input
              type="number"
              id="age"
              name="age"
              value={formData.age}
              onChange={handleChange}
              min="20"
              max="100"
              required
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="sex">Sex</label>
            <select
              id="sex"
              name="sex"
              value={formData.sex}
              onChange={handleChange}
              required
            >
              <option value="1">Male</option>
              <option value="0">Female</option>
            </select>
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="bp">Blood Pressure (mmHg)</label>
            <input
              type="number"
              id="bp"
              name="bp"
              value={formData.bp}
              onChange={handleChange}
              min="80"
              max="220"
              required
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="cholesterol">Cholesterol (mg/dl)</label>
            <input
              type="number"
              id="cholesterol"
              name="cholesterol"
              value={formData.cholesterol}
              onChange={handleChange}
              min="100"
              max="600"
              required
            />
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="maxHR">Maximum Heart Rate</label>
            <input
              type="number"
              id="maxHR"
              name="maxHR"
              value={formData.maxHR}
              onChange={handleChange}
              min="60"
              max="220"
              required
            />
          </div>
          
          <div className="form-group">
            <label htmlFor="stDepression">ST Depression</label>
            <input
              type="number"
              id="stDepression"
              name="stDepression"
              value={formData.stDepression}
              onChange={handleChange}
              min="0"
              max="10"
              step="0.1"
              required
            />
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="chestPainType">Chest Pain Type</label>
            <select
              id="chestPainType"
              name="chestPainType"
              value={formData.chestPainType}
              onChange={handleChange}
              required
            >
              <option value="0">Type 1</option>
              <option value="1">Type 2</option>
              <option value="2">Type 3</option>
              <option value="3">Type 4</option>
            </select>
          </div>
          
          <div className="form-group">
            <label htmlFor="ekgResults">EKG Results</label>
            <select
              id="ekgResults"
              name="ekgResults"
              value={formData.ekgResults}
              onChange={handleChange}
              required
            >
              <option value="0">Normal</option>
              <option value="1">ST-T Wave Abnormality</option>
              <option value="2">Left Ventricular Hypertrophy</option>
            </select>
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="exerciseAngina">Exercise Induced Angina</label>
            <select
              id="exerciseAngina"
              name="exerciseAngina"
              value={formData.exerciseAngina}
              onChange={handleChange}
              required
            >
              <option value="0">No</option>
              <option value="1">Yes</option>
            </select>
          </div>
          
          <div className="form-group">
            <label htmlFor="slopeOfST">Slope of ST</label>
            <select
              id="slopeOfST"
              name="slopeOfST"
              value={formData.slopeOfST}
              onChange={handleChange}
              required
            >
              <option value="0">Upsloping</option>
              <option value="1">Flat</option>
              <option value="2">Downsloping</option>
            </select>
          </div>
        </div>

        <div className="form-row">
          <div className="form-group">
            <label htmlFor="numberOfVesselsFluro">Number of Vessels (fluro)</label>
            <select
              id="numberOfVesselsFluro"
              name="numberOfVesselsFluro"
              value={formData.numberOfVesselsFluro}
              onChange={handleChange}
              required
            >
              <option value="0">0</option>
              <option value="1">1</option>
              <option value="2">2</option>
              <option value="3">3</option>
            </select>
          </div>
          
          <div className="form-group">
            <label htmlFor="thallium">Thallium</label>
            <select
              id="thallium"
              name="thallium"
              value={formData.thallium}
              onChange={handleChange}
              required
            >
              <option value="0">Normal</option>
              <option value="1">Fixed Defect</option>
              <option value="2">Reversible Defect</option>
            </select>
          </div>
        </div>

        <button 
          type="submit" 
          className="submit-button"
          disabled={loading}
        >
          {loading ? 'Processing...' : 'Predict Heart Disease Risk'}
        </button>
      </form>
    </div>
  );
};

export default HeartDiseaseForm;