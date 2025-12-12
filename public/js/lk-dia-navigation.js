var menuIsVisible = false;
var mainMenuContainer;

function toggleMenuContainer(){
  let toggleButton = document.getElementById("toggle-mobile-menu-container");

  if(menuIsVisible){
    //change the toggle mobile menu button to the menu icon
    toggleButton.classList.remove("close-out-icon-mode");
    //style.backgroundImage = `url(../media/img/mobile-menu-icon-black.png)`;

    mainMenuContainer.style.opacity = 0;
    mainMenuContainer.style.height = 0;

    setTimeout(function(){
      mainMenuContainer.style.display = "none";
    }, 505);

    menuIsVisible = false;
  }
  else{
    //change the toggle mobile menu button to the "x" or "close" icon
    toggleButton.classList.add("close-out-icon-mode");
    //toggleButton.style.backgroundImage = `url(../media/img/close-menu-icon-black.png)`;

    mainMenuContainer.style.display = "block";

    setTimeout(function(){
      mainMenuContainer.style.opacity = 1.0;
      mainMenuContainer.style.height = "400px";
    }, 50);

    menuIsVisible = true;
  }
}

function addNavigationControllers(){
  document.getElementById("toggle-mobile-menu-container").addEventListener("click", function(){
    toggleMenuContainer();
  });

  document.getElementById("title-name-container").addEventListener("click", function(){
    window.location.href = "https://lemba-kongo.com";
  })

  document.getElementById("boutique-button-container").addEventListener("click", function(){
    window.location.href = "./browse";
  });

  document.getElementById("maison-button-container").addEventListener("click", function(){
    window.location.href = "./maison";
  });

  document.getElementById("contact-button-container").addEventListener("click", function(){
    window.location.href = "./contact";
  });
}

function initScene(){
  mainMenuContainer = document.getElementById("main-menu-container");
  addNavigationControllers();
}
