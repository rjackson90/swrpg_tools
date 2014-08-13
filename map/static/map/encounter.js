console.log("Loaded encounter.js");
console.log("There are "+encounterData.characterImageURLList.length+" characters on this map");

// Draw function
function draw() {
    // Gain access to the 2D drawing context for the canvas on the page
    var canvas = document.getElementById('drawable');
    if(!canvas) {
        console.log("failed to retrieve element 'drawable'");
        return null;
    }
    var context = canvas.getContext('2d');
    if(!context){
        console.log("Failed to get 2d context");
        return null;
    } else {
        console.log("Got context!");
    }

    // Create new Images, define draw calls
    
    var loadFunc = function(x, y, img){
        return function() {
            context.drawImage(img, x, y);
        };
    };

    var mapImg = new Image();
    var char1Img = new Image();
    var char2Img = new Image();

    mapImg.onload = loadFunc(0, 0, mapImg);
    char1Img.onload = loadFunc(200, 150, char1Img);
    char2Img.onload = loadFunc(600, 180, char2Img);

    // Begin image download
    mapImg.src = encounterData.mapImageURL;
    char1Img.src = encounterData.characterImageURLList[0];
    char2Img.src = encounterData.characterImageURLList[1];
};

// Wait until the window is finished loading to draw canvas
window.onload=draw;


