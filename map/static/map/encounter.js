// Namespace EotEGMT, sub-namespace Encounter
var EotEGMT = EotEGMT || {};

EotEGMT.Encounter = {
    // Properties
    
    // Assigned during init() on window load
    drawContext: null,
    map: null,
    tokens: null,
    canvas: null,
    isDragging: false,
    
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

        this.bounds = function(point) {
            var max = new E.Point(
                    this.image.width + this.position.x,
                    this.image.height + this.position.y
                    );
            var bounds = false;
            bounds = bounds || (
                point.x >= this.position.x && point.x <= max.x &&
                point.y >= this.position.y && point.y <= max.y
                );
            return bounds;
        }

        this.move = function(point) {
            var width_half = this.image.width / 2;
            var height_half = this.image.height / 2;
            
            this.position.x = point.x - width_half;
            this.position.y = point.y - height_half;
        }
    },

    // Methods
    init: function() {
        console.log("init()");
        E.canvas = document.getElementById('drawable');

        // Wrap the raw image URLs inside of Token objects then load the image
        E.map = new E.Token(encounterData.mapImageURL);
        E.map.load();
        E.tokens = [];
        
        encounterData.characterImageURLList.forEach(function(url) {
            E.tokens.push(new E.Token(url));
            E.tokens[E.tokens.length - 1].load();
        });

        // Retrieve and store the canvas' 2d drawing context
        E.drawContext = E.canvas.getContext('2d');

        // Mess with the positions of the tokens, for debugging
        E.tokens[0].position = new E.Point(200, 100);
        E.tokens[1].position = new E.Point(550, 180);

        // Register mouse event listeners to enable click+drag behavior for tokens
        E.canvas.addEventListener("mousedown", function(e) {
            E.isDragging = true;
        }, false);
        E.canvas.addEventListener("mousemove", E.mouseMoveTokens, false);
        E.canvas.addEventListener("mouseup", function(e) {
            E.isDragging = false;
        }, false);
        E.canvas.addEventListener("mouseleave", function(e) {
            E.isDragging = false;
        }, false);
    },

    doDraw: function() {
        E.drawContext.clearRect(0, 0, E.canvas.width, E.canvas.height);

        // Draw the map first, then tokens on to.
        E.map.draw(E.drawContext);
        for(var i = 0; i < E.tokens.length; ++i) {
            E.tokens[i].draw(E.drawContext);
        }
    },

    mouseMoveTokens: function(ev) {
        if(!E.isDragging) return;
        var new_loc = new E.Point(0, 0);

        // Get the position of the event in DOM coordinates
        if(ev.x != undefined && ev.y != undefined){ // IE, Chrome, Safari properties
            new_loc.x = ev.x;
            new_loc.y = ev.y;
        } else {    // Firefox-specific properties
            new_loc.x = ev.clientX + document.body.scrollLeft + 
                document.documentElement.scrollLeft;
            new_loc.y = ev.clientY + document.body.scrollTop + 
                document.documentElement.scrollTop;
        }

        // Convert to canvas coordinates
        var offset = new E.Point(E.canvas.offsetLeft, E.canvas.offsetTop);
        new_loc.x -= offset.x;
        new_loc.y -= offset.y;

        // Iterate over the tokens, if the new event targets a token, move it
        for(var i = 0; i < E.tokens.length; ++i) {
            if(E.tokens[i].bounds(new_loc)){
                E.tokens[i].move(new_loc);
                E.doDraw();
                return;
            }
        }
    }

};
var E = EotEGMT.Encounter;


window.onload = E.init;
