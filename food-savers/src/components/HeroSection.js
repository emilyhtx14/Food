import React from 'react';
import '../App.css';
import { Button } from './Button';
import './HeroSection.css';

function HeroSection() {
  return (
    <div className='hero-container'>
      <video src='/videos/prettycity.mp4' autoPlay loop muted />
      <h1>FOOD SAVERS</h1>
      <p>1 in 10 Americans don't know where their next meal will come from.
        
      </p>
      <div className='hero-btns'>
        <Button
          className='btns'
          buttonStyle='btn--primary'
          buttonSize='btn--large'
        >
          ABOUT
        </Button>
        <Button
          className='btns'
          buttonStyle='btn--primary'
          buttonSize='btn--large'
          onClick={console.log('hey')}
        >
          DONATE 
        </Button>
      </div>
    </div>
  );
}

export default HeroSection;
