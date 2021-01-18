import React from 'react';
import './Cards.css';
import CardItem from './CardItem';

function Cards() {
  return (
    <div className='cards'>
      <h1>Community Dashboard</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem
              src='images/Supermarket.jpg'
              text='Supermarkets near You'
              label='View'
              path='/services'
            />
            <CardItem
              src='images/img-9.jpg'
              text='Shelters near You'
              label='View'
              path='/services'
            />
          </ul>
          <ul className='cards__items'>
            <CardItem
              src='images/safeway.jpeg'
              text='Delivery #20101: Jan 28, 2021'
              label='Safeway Market, Davis, CA'
              path='/services'
            />
            <CardItem
              src='images/tj.png'
              text='Delivery #34103: Jan 29, 2021'
              label="Trader Joe's, Davis, CA"
              path='/products'
            />
            <CardItem
              src='images/nugget.jpeg'
              text='Delivery #21423: Jan 20, 2021'
              label='Nugget Market, Davis, CA'
              path='/sign-up'
            />
          </ul>


          <ul className='cards__items'>
            <CardItem
              src='images/starbucks.png'
              text='Delivery #190: Jan 19, 2021'
              label='Starbucks Bakery, Davis, CA'
              path='/services'
            />
            <CardItem
              src='images/kobe.jpg'
              text='Delivery #12831: Jan 27, 2021'
              label="Kobe Mini Mart, Davis, CA"
              path='/products'
            />
            <CardItem
              src='images/fastandeasy.jpg'
              text='Delivery #31272: Jan 18, 2021'
              label='Fast and Easy Market, Davis, CA'
              path='/sign-up'
            />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Cards;
