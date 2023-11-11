// ImageUpload.js
import React, { useState } from 'react';
import axios from 'axios';

const ImageUpload = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [response, setResponse] = useState(null);

  const handleImageChange = (e) => {
    const file = e.target.files[0];
    setSelectedImage(file);
  };

  const handleImageUpload = async () => {
    const formData = new FormData();
    formData.append('image', selectedImage);

    try {
      const response = await axios.post('YOUR_API_ENDPOINT', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResponse(response.data);
    } catch (error) {
      console.error('Error uploading image:', error);
    }
  };

  return (
    <div>
      <input type="file" onChange={handleImageChange} />
      <button onClick={handleImageUpload}>Upload Image</button>
      {response && <div>API Response: {JSON.stringify(response)}</div>}
    </div>
  );
};

export default ImageUpload;
