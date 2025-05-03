// src/components/Header.jsx
import './Header.css';
import { Link } from 'react-router-dom';

const Header = () => {
  return (
    <header className="app-header">
      <div className="header-container">
        <h1>MediSense</h1>
        <p>Multiple Disease Prediction System</p>
      </div>
      <nav className="header-nav">
        <Link to="/" className="active">Heart Disease</Link>
        <Link to="/diabetes">Diabetes</Link>
        <Link to="/lungs">Lung Disease</Link>
        <Link to="/about">About</Link>
        <Link to="/medical-image">Medical-Image</Link>
      </nav>
    </header>
  );
};

export default Header;
