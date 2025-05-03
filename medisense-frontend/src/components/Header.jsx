// src/components/Header.jsx
import { useState } from 'react';
import './Header.css';
import { Link, useLocation } from 'react-router-dom';

const Header = () => {
  const [showMenu, setShowMenu] = useState(false);
  const location = useLocation();

  const toggleMenu = () => {
    setShowMenu(!showMenu);
  };

  const getLinkClass = (path) =>
    location.pathname === path ? 'active' : '';

  return (
    <header className="app-header">
      <div className="header-container">
        <h1>MediSense</h1>
        <p>Multiple Disease Prediction System</p>

        {/* Hamburger icon */}
        <div className="hamburger" onClick={toggleMenu}>
          <span></span>
          <span></span>
          <span></span>
        </div>

        {/* Navigation links */}
        <nav className={`header-nav ${showMenu ? 'show' : ''}`}>
          <Link to="/" className={getLinkClass('/')}>Heart Disease</Link>
          <Link to="/diabetes" className={getLinkClass('/diabetes')}>Diabetes</Link>
          <Link to="/lungs" className={getLinkClass('/lungs')}>Lung Disease</Link>
          <Link to="/medical-image" className={getLinkClass('/medical-image')}>Medical-Image</Link>
          <Link to="/about" className={getLinkClass('/about')}>About</Link>
        </nav>
      </div>
    </header>
  );
};

export default Header;
