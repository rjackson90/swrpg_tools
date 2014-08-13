// Namespace EotEGMT, sub-namespace Encounter
var EotEGMT = EotEGMT || {};

EotEGMT.Encounter = {
    // Properties
    
    // Assigned during init() on window load
    drawContext: null,
    map: null,
    tokens: null,
    
    // Objects
    Point: function(X, Y) {
        this.x = X;
        this.y = Y;
    },

    Token: function(url) {
        this.image_url = url;
        this.loaded = false;
        this.image = new Image();
        this.position = new E.Point(0, 0);

        this.draw = function(ctx) {
            if(this.loaded && ctx != null) {
                ctx.drawImage(this.image, this.position.x, this.position.y);
            }
        };

        this.load = function() {
            var self = this;
            this.image.addEventListener("load", function() {
                self.loaded = true;
                E.doDraw();
            }, false);
            this.image.src = this.image_url;
        };
    },

    // Methods
    init: function() {
        console.log("init()");

        // Wrap the raw image URLs inside of Token objects then load the image
        E.map = new E.Token(encounterData.mapImageURL);
        E.map.load();
        E.tokens = [];
        
        encounterData.characterImageURLList.forEach(function(url) {
            E.tokens.push(new E.Token(url));
            E.tokens[E.tokens.length - 1].load();
        });

        // Retrieve and store the canvas' 2d drawing context
        E.drawContext = document.getElementById('drawable').getContext('2d');

        // Mess with the positions of the tokens, for debugging
        E.tokens[0].position = new E.Point(200, 100);
        E.tokens[1].position = new E.Point(550, 180);
    },

    doDraw: function() {
        // Draw the map first, then tokens on to.
        E.map.draw(E.drawContext);
        for(var i = 0; i < E.tokens.length; ++i) {
            E.tokens[i].draw(E.drawContext);
        }
    }

};
var E = EotEGMT.Encounter;


window.onload = E.init;
