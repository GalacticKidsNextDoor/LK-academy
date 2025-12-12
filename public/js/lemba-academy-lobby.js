var imageCache, startSlideShow; 

let currentImageIndex = -1;
let maxImageIndex, bgImageLayerContainer;

document.addEventListener("DOMContentLoaded", function(){
    init();

    startSlideShow = setInterval(function(){
        backgroundImageSlideShow()
    }, 10000);
});

function init(){
    imageCache = [
        "./media/img/lions-united-0.png",
        "./media/img/lions-united-1.png",
        "./media/img/lions-united-2.png",
        "./media/img/lions-united-3.png",
        "./media/img/lions-united-4.png",
        "./media/img/lions-united-5.png"
    ];
    bgImageLayerContainer = document.getElementById("background-image-container");
    maxImageIndex = imageCache.length;
    
    addButtonHandlers();
    
    console.log('v. 0.1.2');
}

function addButtonHandlers(){
    document.getElementById("shop-option-button-container").addEventListener("click", function(){
        window.open("https://lemba-kongo.com/shop", "_blank");
    });
    
    document.getElementById("academy-option-button-container").addEventListener("click", function(){
        window.open("https://lemba-kongo.com/academy", "_blank");
    });
}

function backgroundImageSlideShow(){
    ++currentImageIndex;
    bgImageLayerContainer.style.backgroundImage = `url(${imageCache[currentImageIndex]})`;
    if(currentImageIndex+1===maxImageIndex){
        currentImageIndex = -1;
    }
}