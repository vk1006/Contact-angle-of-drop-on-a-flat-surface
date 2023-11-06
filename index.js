const reader = new FileReader();

var imgUrl;

reader.onloadend = function() {
    imgUrl = reader.result;
}

document.getElementById('formFile').addEventListener("change", () => {
    const image = document.querySelector('input[type="file"]').files[0];
    reader.readAsDataURL(image);
});


document.getElementById('imageForm').addEventListener('submit', (e) => {
    e.preventDefault();
  
    // const formData = new FormData();
    
    // formData.append('image', imgUrl);

    const formData = {
        'photo': imgUrl.split(",")[1],
        'threshold': 20
    }

    console.log(formData['photo']);

    fetch('http://127.0.0.1:5000/post', {
      method: 'POST',
      body: formData,
    })
    .then(response => {
      if (response.ok) {
        return response.json();
      } else {
        throw new Error('File upload failed');
      }
    })
    .then(data => {
      console.log('Server response:', data);
    })
    .catch(error => {
      console.error('Error uploading file:', error);
    });

  });
  