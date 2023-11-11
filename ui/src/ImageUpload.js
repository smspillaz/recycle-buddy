import React, { useState } from 'react';
import {
  Button,
  CircularProgress,
  AppBar,
  Toolbar,
  Typography,
  Container,
  TextField,
  ToggleButton,
  ToggleButtonGroup
} from '@mui/material';
import './ImageUpload.css'; // Import a CSS file for additional styling

const ImageUpload = () => {
  const [selectedImage, setSelectedImage] = useState(null);
  const [responseError, setResponseError] = useState(null);
  const [responseStream, setResponseStream] = useState(null);
  const [disposeMode, setDisposeMode] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleImageChange = async (e) => {
    const file = e.target.files[0];

    // Check if a file is selected
    if (file) {
      // Set the selected image for display
      setSelectedImage({
          url: URL.createObjectURL(file),
          file
      });
    }
  };

  const handleDisposeModeChange = async (e, mode) => {
    setDisposeMode(mode);
    if (selectedImage.file) {
      setLoading(true);

      // The result property contains the data as a base64 encoded string
      let data = new FormData();
      data.append('img', selectedImage.file);

      // Send base64 image to the server
      try {
        const response = await fetch(
          'https://junction-recycling-j4yundcgda-lz.a.run.app/api/vision',
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
    }
  }

  return (
    <div>
      <AppBar position="static" color="primary">
        <Toolbar>
          <Typography variant="h6">EcoScan</Typography>
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
            <div>
              <div className="image-preview">
                <h3>Selected Image:</h3>
                <img src={selectedImage.url} alt="Selected" />
              </div>
              <div>
              <ToggleButtonGroup
                value={disposeMode}
                exclusive
                onChange={handleDisposeModeChange}
              >
                <ToggleButton value="donate">
                  {"Donate"}
                </ToggleButton>
                <ToggleButton value="waste">
                  {"Dispose"}
                </ToggleButton>
              </ToggleButtonGroup>
              </div>
            </div>
          )}
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
      </Container>
    </div>
  );
};

export default ImageUpload;
