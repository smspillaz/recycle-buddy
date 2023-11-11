import React, { useState } from 'react';
import {
  Button,
  CircularProgress,
  AppBar,
  Toolbar,
  Typography,
  Container,
  TextField,
} from '@mui/material';
import './ImageUpload.css'; // Import a CSS file for additional styling

const ImageUpload = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [base64Image, setBase64Image] = useState(null);
  const [responseMessage, setResponseMessage] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = async (e) => {
    const file = e.target.files[0];

    // Check if a file is selected
    if (file) {
      setLoading(true);

      const reader = new FileReader();

      // Set up the FileReader callback
      reader.onloadend = async () => {
        // The result property contains the data as a base64 encoded string
        const base64Result = reader.result;
        setBase64Image(base64Result);

        // Send base64 image to the server
        try {
          const response = await fetch('YOUR_API_ENDPOINT', {
            method: 'POST',
            headers: {
              'Content-Type': 'application/json',
            },
            body: JSON.stringify({ base64Image: base64Result }),
          });

          const responseData = await response.json();
          setResponseMessage(responseData.message);
        } catch (error) {
          console.error('Error uploading image:', error);
          setResponseMessage('Error uploading image. Please try again.');
        } finally {
          setLoading(false);
        }
      };

      // Read the file as a data URL, triggering the onloadend callback
      reader.readAsDataURL(file);

      // Set the selected image for display
      setSelectedImage(URL.createObjectURL(file));
    }
  };

  return (
    <div>
      <AppBar position="static" color="primary">
        <Toolbar>
          <Typography variant="h6">Uncle Sam and eco</Typography>
        </Toolbar>
      </AppBar>
      <Container maxWidth="md" style={{ marginTop: '20px' }}>
        <div className="image-upload-container">
          <TextField
            type="file"
            label="Choose Image"
            onChange={handleImageChange}
            InputLabelProps={{ shrink: true }}
          />
          {selectedImage && (
            <div className="image-preview">
              <h3>Selected Image:</h3>
              <img src={selectedImage} alt="Selected" />
              {loading ? (
                <CircularProgress style={{ marginTop: 10 }} />
              ) : (
                responseMessage && <p>{responseMessage}</p>
              )}
            </div>
          )}
        </div>
      </Container>
    </div>
  );
};

export default ImageUpload;
