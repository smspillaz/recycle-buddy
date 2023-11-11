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
  const [responseError, setResponseError] = useState(null);
  const [responseStream, setResponseStream] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = async (e) => {
    const file = e.target.files[0];

    // Check if a file is selected
    if (file) {
      setLoading(true);

      // The result property contains the data as a base64 encoded string
      let data = new FormData();
      data.append('img', file);

      // Send base64 image to the server
      try {
        const response = await fetch(
          'http://localhost:8080/api/vision',
          {
            method: 'POST',
            body: data
          }
        );

        const responseData = await response.json();
        setResponseStream(responseData);
      } catch (error) {
        console.error('Error uploading image:', error);
        setResponseError('Error uploading image. Please try again.');
      } finally {
        setLoading(false);
      }

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
                <div>
                  <div>
                    {responseError && <p>{responseError}</p>}
                  </div>
                  <div>
                    {responseStream && (
                      <div style={{textAlign: "left"}}>
                        {responseStream.map(({ stream, options, instructions }) => (
                          <div>
                            <ul>
                              <li><a style={{fontWeight: 'bold'}}>{stream}</a>: {instructions}</li>
                              <ul>
                                {options.map(o => (
                                  <li>{o}</li>
                                ))}
                              </ul>
                            </ul>
                          </div>
                        ))}
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      </Container>
    </div>
  );
};

export default ImageUpload;
