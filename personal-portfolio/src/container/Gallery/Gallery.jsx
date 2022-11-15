import React from 'react';
import { NavLink } from 'react-bootstrap';
import { BsInstagram, BsArrowLeftShort, BsArrowRightShort } from 'react-icons/bs';

import SubHeading  from '../../components/SubHeading/SubHeading';
import { images } from '../../constants';
import './Gallery.css';

const Gallery = () => {
  const scrollRef = React.useRef(null);

  const scroll = (direction) => {
    const { current } = scrollRef;

    if (direction === 'left') {
      current.scrollLeft -= 300;
    } else {
      current.scrollLeft += 300;
    }
  };

  return (
    <div className="app__gallery flex__center">
      <div className="app__gallery-content">
        <h1 className="headtext__cormorant">Our Dishes</h1>
        <p className="p__opensans" style={{ color: '#AAAAAA', marginTop: '2rem' }}>Our Dishes Contains Differents Ingredients Such Protien, Fiber, Carbohydrates,Calcium According To Differents Diets Such Vegan Diet, Paleo Diet, High.
       
        <br></br>  If Nothing Interests You, You Can Do a Custom Order. </p>
        <button type="button" className="custom__button"> <NavLink href="/custom"></NavLink> Custom Order
        <br></br></button>

      </div>
      <div className="app__gallery-images">
        <div className="app__gallery-images_container" ref={scrollRef}>
          {[images.gallery01, images.gallery02, images.gallery03, images.gallery04].map((image, index) => (
            <div className="app__gallery-images_card flex__center" key={`gallery_image-${index + 1}`}>
              <img src={image} alt="gallery_image" />
            </div>
          ))}
        </div>
        <div className="app__gallery-images_arrows">
          <BsArrowLeftShort className="gallery__arrow-icon" onClick={() => scroll('left')} />
          <BsArrowRightShort className="gallery__arrow-icon" onClick={() => scroll('right')} />
        </div>
      </div>
    </div>
  );
};

export default Gallery;
