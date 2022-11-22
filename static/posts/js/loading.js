function setThumbnail(event) {
    var reader = new FileReader();

    reader.onload = function(event) {
      var img = document.createElement("img");
      img.setAttribute("src", event.target.result);
      document.querySelector("div#PhotoPlusBox").appendChild(img);
    };

    reader.readAsDataURL(event.target.files[0]);
  }